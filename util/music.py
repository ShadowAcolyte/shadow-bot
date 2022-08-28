import discord
from discord.ext import commands


class Music(commands.Cog):
    def __init__(self, bot: commands.AutoShardedBot) -> None:
        self.bot = bot


async def setup(bot: commands.AutoShardedBot):
    await bot.add_cog(Music(bot))
