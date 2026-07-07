# Old: Generator that yields control
def generator_ex():
    yield 1
    yield 2
    yield 3

gen = generator_ex()
print(next(gen))
print(next(gen))
print(next(gen))


# async/await is the same idea, but cleaner:
# New: Coroutine that pauses and resumes

import asyncio
import time

async def fetch_data(name: str, delay: int) -> int:
    print(f'{name} : starting {delay}')
    await asyncio.sleep(delay)
    print(f'{name} finished!')
    return delay

async def main():
    # in sequential
    print('-----sequence-----')
    start = time.time()
    await fetch_data('A', 2)
    await fetch_data('B', 1)
    await fetch_data('C', 3)
    seq_finish = time.time() - start
    print(f'sequence finished in {seq_finish:.1f}')

    # Concurrency
    print('-----Concurrency-----')
    start_con = time.time()
    await asyncio.gather(
        fetch_data("A", 3),
        fetch_data("B", 2),
        fetch_data("c", 1)
    ) 
    con_finish = time.time() - start_con
    print(f'concurrency finished in {con_finish:.1f}')

    print(f'speed up by : {seq_finish/con_finish:.1f}x')



asyncio.run(main())