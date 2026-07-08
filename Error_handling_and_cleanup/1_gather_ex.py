import asyncio

async def fetch_data(url):
    # Imagine this fails sometimes
    if "bad" in url:
        raise ValueError("Bad URL")
    await asyncio.sleep(1)
    return "data"

async def main():
    results = await asyncio.gather(
        fetch_data("good.com"),
        fetch_data("bad.com"),  # ← This fails
        fetch_data("good.com"),
    )
    print(results)  # Never reaches here


asyncio.run(main())