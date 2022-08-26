import discord
import util
from discord.ext import commands


class General(commands.Cog):
    def __init__(self, bot: commands.AutoShardedBot) -> None:
        self.bot = bot

    @commands.command(name="say", description="Says stuff")
    async def say(self, ctx: commands.Context, *, arg: str):
        await ctx.message.delete()
        everyone = ctx.channel.permissions_for(ctx.author).mention_everyone
        if ctx.message.reference is None:
            await ctx.send(
                arg, allowed_mentions=discord.AllowedMentions(everyone=everyone)
            )
        else:
            ref_message: discord.Message = await util.message.get_message_reference(
                ctx.message
            )
            await ref_message.reply(
                arg, allowed_mentions=discord.AllowedMentions(everyone=everyone)
            )


async def setup(bot: commands.AutoShardedBot):
    await bot.add_cog(General(bot))
