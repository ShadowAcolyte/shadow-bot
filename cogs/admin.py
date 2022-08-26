from discord.ext import commands


class Admin(commands.Cog):
    def __init__(self, bot: commands.AutoShardedBot) -> None:
        self.bot = bot


async def setup(bot: commands.AutoShardedBot):
    await bot.add_cog(Admin(bot))
