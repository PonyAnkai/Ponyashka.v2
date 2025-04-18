import disnake
from disnake.ext import commands

import json
from dotenv import dotenv_values

# Load configurate file
with open("./config.json", encoding="UTF-8") as fp: config = json.load()

bot_config = config['bot_settings']
KEYS = dotenv_values()

# setup bot
bot = commands.Bot (
    command_prefix=bot_config['prefix'], 
    intents=disnake.Intents.all(), 
    activity= disnake.Activity(name='DPN', type= disnake.ActivityType.watching),
    reload=True, 
    help_command=None,
    description=bot_config['descriptions'],
    owner_id=bot_config['owner']
)

def main(bot: commands.Bot):

    
    # start this on end
    bot.run(KEYS["DISCORD_API_KEY"])  


if __name__ == "__main__":
    main(bot)