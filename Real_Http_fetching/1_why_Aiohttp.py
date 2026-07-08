# BAD - blocks event loop, requests.get() blocks. It halts the event loop. Bad.
'''
import requests
response = requests.get("https://api.github.com/users/github")
'''

# aiohttp is async-aware:
# GOOD - async, doesn't block
import asyncio
import aiohttp
async def http():
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.github.com/users/github") as resp:
            data = await resp.json()
            
    return data

print(asyncio.run(http()))