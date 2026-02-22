import disnake
from disnake.ext import commands


class USER(commands.Cog):
    def __init__(self, bot=commands.Bot):
        self.bot = bot



#! LOADED FUNCTIONS
def setup(bot):
    bot.add_cog(USER(bot))