import asyncio
import logging as log
from telegram import start

log.basicConfig(level=log.INFO)


async def main() -> None:
    await start()


if __name__ == "__main__":
    asyncio.run(main())
