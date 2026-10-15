import disnake
from disnake.ext import commands


class UNTIL(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        await ctx.send("Pong!")

#! LOADED FUNCTIONS
def setup(bot):
    bot.add_cog(UNTIL(bot))