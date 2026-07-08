import asyncio
import aiohttp
import time

async def fetch_url(session, url):
    """Fetch a single URL, return (url, content_length)"""
    try:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as resp:
            text = await resp.text()
            return url, len(text)
    except Exception as e:
        return url, f"Error: {type(e).__name__}"

async def fetch_multiple(urls):
    """Fetch multiple URLs concurrently"""
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        return results

async def main():
    urls = [
        "https://api.github.com/users/github",
        "https://api.github.com/users/google",
        "https://api.github.com/users/microsoft",
        "https://api.github.com/users/facebook",
        "https://api.github.com/users/netflix",
    ]
    
    print(f"Fetching {len(urls)} URLs...\n")
    
    # Sequential
    print("--- SEQUENTIAL ---")
    start = time.time()
    results_seq = []
    async with aiohttp.ClientSession() as session:
        for url in urls:
            result = await fetch_url(session, url)
            results_seq.append(result)
    seq_time = time.time() - start
    print(f"Time: {seq_time:.2f}s\n")
    
    # Concurrent
    print("--- CONCURRENT ---")
    start = time.time()
    results_conc = await fetch_multiple(urls)
    conc_time = time.time() - start
    print(f"Time: {conc_time:.2f}s")
    print(f"Speedup: {seq_time / conc_time:.1f}x\n")
    
    print("Results:")
    for url, length in results_conc:
        print(f"  {url}: {length} bytes")

asyncio.run(main())