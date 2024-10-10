import asyncio
import logging as log
from telegram import start_bot

log.basicConfig(level=log.INFO)


async def main() -> None:
    await start_bot()


if __name__ == "__main__":
    asyncio.run(main())
