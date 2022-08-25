import discord
import os
from macro import macro_list
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot("sh ", intents = intents)

@bot.listen('on_message')
async def on_message(message: discord.Message):
    # macros
    if message.content.startswith('++'):
        if macro_content := macro_list.get(message.content[2:]):
            if message.reference is None:
                await message.reply(macro_content)
            elif message.reference.cached_message is None:
                ref_message: discord.Message = await message.channel.fetch_message(message.reference.message_id)
                await ref_message.reply(macro_content)
            else:
                await message.reference.cached_message.reply(macro_content)

    # good bot messages
    if message.content.lower().startswith("good bot") and message.reference.cached_message.author.id == bot.user.id:
        await message.reply("Thanks! ≧◡≦")
    # bad bot messages
    if message.content.lower().startswith("bad bot") and message.reference.cached_message.author.id == bot.user.id:
        await message.reply("Sowwy! o(╥﹏╥)~")

@bot.command()
async def say(ctx: commands.Context, *, arg: str):
    await ctx.send(arg)

bot.run(os.environ['DISCORD_TOKEN'])
