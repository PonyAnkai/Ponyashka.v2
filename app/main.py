import disnake
from disnake.ext import commands

import json
import os
from dotenv import dotenv_values

# Load configurate file
with open("./app/config.json", encoding="UTF-8") as fp: config = json.load(fp)
KEYS = dotenv_values()


def main():

    bot = commands.Bot (
        command_prefix=config["PREFIX"], 
        intents=disnake.Intents.all(), 
        activity= disnake.Activity(name="MPG", type= disnake.ActivityType.watching),
        reload=True, 
        help_command=None,
        owner_id=config['OWNER']
    )

    BASEDIR = f"{os.getcwd()}\\"
    for item in os.listdir(BASEDIR + f"app\\cogs\\"):
        try: bot.load_extension(f"cogs.{item.replace('.py', '')}")
        except: pass

    print(">>> BOT LOADED")
    return bot.run(KEYS["DISCORD_API_KEY"])  


if __name__ == "__main__":
    main()