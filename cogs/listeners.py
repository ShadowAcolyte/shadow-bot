import discord
import util
from macro import macro_list
from discord.ext import commands


class Listener(commands.Cog):
    def __init__(self, bot: commands.AutoShardedBot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.reference is not None:
            ref_message: discord.Message = await util.message.get_message_reference(
                message
            )
        # macros
        if message.content.startswith("++"):
            if macro_content := macro_list.get(message.content[2:]):
                if message.reference is None:
                    await message.reply(macro_content)
                else:
                    await ref_message.reply(macro_content)

        # good bot messages
        if (
            message.content.lower().startswith("good bot")
            and message.reference is not None
            and ref_message.author.id == self.bot.user.id
        ):
            await message.reply("Thanks! ≧◡≦")
        # bad bot messages
        if (
            message.content.lower().startswith("bad bot")
            and message.reference is not None
            and ref_message.author.id == self.bot.user.id
        ):
            await message.reply("Sowwy! o(╥﹏╥)~")


async def setup(bot: commands.AutoShardedBot):
    await bot.add_cog(Listener(bot))
