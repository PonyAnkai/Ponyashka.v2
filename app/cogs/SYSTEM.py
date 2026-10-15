import disnake
from disnake.ext import commands


class SYSTEM(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        activity = disnake.Activity(name="GARM IS ALIVE!", type=disnake.ActivityType.playing)
        await self.bot.change_presence(status=disnake.Status.online, activity=activity)

#! LOADED FUNCTIONS
def setup(bot):
    bot.add_cog(SYSTEM(bot))