import asyncio
from functs import *
from binance.client import Client, AsyncClient



async def main():    
    client  = Client()
    tokens = await get_available_tokens(client)
    asyncio.gather(*[volumeSignal(client,x) for x in tokens])
    return ()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
