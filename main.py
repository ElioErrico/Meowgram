import logging
import asyncio

from ccat_telegram_bot import CCatTelegramBot

TOKEN = ""

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def main():
    bot = CCatTelegramBot(TOKEN)
    await bot.run()
    
if __name__ == "__main__":
    asyncio.run(main())