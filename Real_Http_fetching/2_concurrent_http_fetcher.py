import asyncio
import aiohttp
import time

start_time = None

async def fetch_url(session, url):
    """Fetch a single URL, return (url, content_length)"""
    global start_time
    elapsed = time.time() - start_time
    print(f"[{elapsed:.2f}s] Starting {url}")
    
    try:
        async with session.get(url, timeout=aiohttp.ClientTimeout(total=10)) as resp:
            text = await resp.text()
            elapsed = time.time() - start_time
            print(f"[{elapsed:.2f}s] Finished {url}: {len(text)} bytes")
            return url, len(text)
    except Exception as e:
        elapsed = time.time() - start_time
        print(f"[{elapsed:.2f}s] Error {url}: {type(e).__name__}")
        return url, f"Error: {type(e).__name__}"

async def fetch_multiple(urls):
    """Fetch multiple URLs concurrently"""
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        return results

async def main():
    global start_time
    urls = [
        "https://api.github.com/users/github",
        "https://api.github.com/users/google",
        "https://api.github.com/users/microsoft",
        "https://api.github.com/users/facebook",
        "https://api.github.com/users/netflix",
    ]
    
    print(f"Fetching {len(urls)} URLs concurrently...\n")
    
    start_time = time.time()
    start = time.time()
    results = await fetch_multiple(urls)
    conc_time = time.time() - start
    
    print(f"\nTotal time: {conc_time:.2f}s")

asyncio.run(main())