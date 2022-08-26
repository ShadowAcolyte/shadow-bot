import discord
import os
from macro import macro_list
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot("$", intents = intents)

async def get_message_reference(message: discord.Message) -> discord.Message:
    if message.reference.cached_message is not None:
        return message.reference.cached_message
    else:
        return await message.channel.fetch_message(message.reference.message_id)

@bot.listen('on_message')
async def on_message(message: discord.Message):
    if message.reference is not None:
        ref_message: discord.Message = await get_message_reference(message)
    # macros
    if message.content.startswith('++'):
        if macro_content := macro_list.get(message.content[2:]):
            if message.reference is None:
                await message.reply(macro_content)
            else:
                await ref_message.reply(macro_content)

    # good bot messages
    if message.content.lower().startswith("good bot") and message.reference is not None and ref_message.author.id == bot.user.id:
        await message.reply("Thanks! ≧◡≦")
    # bad bot messages
    if message.content.lower().startswith("bad bot") and message.reference is not None and ref_message.author.id == bot.user.id:
        await message.reply("Sowwy! o(╥﹏╥)~")

@bot.command()
async def say(ctx: commands.Context, *, arg: str):
    await ctx.message.delete()
    everyone = ctx.channel.permissions_for(ctx.author).mention_everyone
    if ctx.message.reference is None:
        await ctx.send(arg, allowed_mentions=discord.AllowedMentions(everyone=everyone))
    else:
        ref_message: discord.Message = await get_message_reference(ctx.message)
        await ref_message.reply(arg, allowed_mentions=discord.AllowedMentions(everyone=everyone))

@bot.command()
async def exec(ctx: commands.Context, *, arg: str):
    await ctx.message.delete()

bot.run(os.environ['DISCORD_TOKEN'])
