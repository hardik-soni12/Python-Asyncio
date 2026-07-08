import asyncio

async def background_job(name, delay):
    print(f"{name}: started")
    await asyncio.sleep(delay)
    print(f"{name}: finished")

async def main():
    # Start a background task (doesn't block you)
    task = asyncio.create_task(background_job("BG", 3))
    
    # Do other stuff while it runs
    print("Main: starting other work")
    await asyncio.sleep(1)
    print("Main: still working...")
    
    # Check if it's done (don't wait)
    print(f"Task done? {task.done()}")
    
    # NOW wait for it
    await task
    print("Main: background task finished, now I can use its result")

asyncio.run(main())