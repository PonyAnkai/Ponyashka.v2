import disnake
from disnake.ext import commands

from dotenv import dotenv_values

import asyncio
import json
import os

# Load configurate file
with open("./app/config.json", encoding="UTF-8") as fp: config = json.load(fp)
ENV = dotenv_values()

bot = commands.Bot (
    command_prefix=config["PREFIX"], 
    intents=disnake.Intents.all(), 
    reload=True, 
    help_command=None,
    owner_id=config['OWNER']
)

async def main():
    # Подгрузка модулей бота
    BASEDIR = f"{os.getcwd()}\\"
    for item in os.listdir(BASEDIR + f"app\\cogs\\"):
        try: bot.load_extension(f"cogs.{item.replace('.py', '')}")
        except: 
            if item == "__pycache__": continue 
            print(f"Cog {item} will be not loaded")

    # Основной пулл создания парралельных задач
    bot_task = asyncio.create_task(bot.start(str(ENV["DISCORD_API_KEY"])))

    print(" –"*6 + " BOT START WORKING" + " –"*6)
    await asyncio.gather(bot_task)  

if __name__ == "__main__":
    asyncio.run(main())