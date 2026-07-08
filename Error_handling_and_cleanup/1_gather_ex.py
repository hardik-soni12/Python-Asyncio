import asyncio

async def fetch_data(url):
    # Imagine this fails sometimes
    if "bad" in url:
        raise ValueError("Bad URL")
    await asyncio.sleep(1)
    return "data"

# async def main():
#     results = await asyncio.gather(
#         fetch_data("good.com"),
#         fetch_data("bad.com"),  # ← This fails
#         fetch_data("good.com"),
#     )
#     print(results)  # Never reaches here

async def main():
    results = await asyncio.gather(
        fetch_data("good.com"),
        fetch_data("bad.com"),
        fetch_data("good.com"),
        return_exceptions=True  # ← This line return_exceptions=True = "Give me errors as values, not crashes"
    )
    
    # results = ['data', ValueError(...), 'data']
    # No crash. Exceptions are in the list.
    
    for result in results:
        if isinstance(result, Exception):
            print(f"Error: {result}")
        else:
            print(f"Success: {result}")


asyncio.run(main())