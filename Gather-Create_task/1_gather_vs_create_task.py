import asyncio
import time

async def fetch_data(name, delay):
    print(f"{name}: starting")
    await asyncio.sleep(delay)
    print(f"{name}: done")
    return f"{name}({delay}s)"

# Pattern 1: gather (wait for all)
async def pattern_gather():
    print("\n--- GATHER ---")
    start = time.time()
    results = await asyncio.gather(
        fetch_data("A", 2),
        fetch_data("B", 1),
        fetch_data("C", 3),
    )
    elapsed = time.time() - start
    print(f"Results: {results}")
    print(f"Total time: {elapsed:.1f}s")

# Pattern 2: create_task (fire and forget, then wait)
async def pattern_create_task():
    print("\n--- CREATE_TASK ---")
    start = time.time()
    
    task_a = asyncio.create_task(fetch_data("A", 2))
    task_b = asyncio.create_task(fetch_data("B", 1))
    task_c = asyncio.create_task(fetch_data("C", 3))
    
    print("All tasks created and running")
    
    # Wait for them
    result_a = await task_a
    result_b = await task_b
    result_c = await task_c
    
    elapsed = time.time() - start
    print(f"Results: {result_a}, {result_b}, {result_c}")
    print(f"Total time: {elapsed:.1f}s")

async def main():
    await pattern_gather()
    await pattern_create_task()

asyncio.run(main())