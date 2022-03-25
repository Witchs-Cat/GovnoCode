import asyncio
from puppeteer import Puppeteer

if __name__ == "__main__":
    puppeteer = Puppeteer()
    asyncio.ensure_future(puppeteer.start())
    loop = asyncio.get_event_loop()
    loop.run_forever()