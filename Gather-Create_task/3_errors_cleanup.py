import asyncio

async def risky_fetch(url, delay):
    print(f"Fetching {url}...")
    await asyncio.sleep(delay)
    
    if "fail" in url:
        raise ValueError(f"Failed to fetch {url}")
    
    return f"Data from {url}"

async def main():
    results = await asyncio.gather(
        risky_fetch("api1.com", 1),
        risky_fetch("fail-api.com", 1),
        risky_fetch("api2.com", 1),
        return_exceptions=True
    )
    
    print("\nResults:")
    for i, result in enumerate(results):
        if isinstance(result, Exception):
            print(f"  [{i}] ERROR: {result}")
        else:
            print(f"  [{i}] SUCCESS: {result}")

asyncio.run(main())