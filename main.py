import discord
import os
import datetime
import traceback
from macro import macro_list
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot_prefix = '$$'

bot = commands.Bot(bot_prefix, intents = intents)

async def get_message_reference(message: discord.Message) -> discord.Message:
    if message.reference.cached_message is not None:
        return message.reference.cached_message
    else:
        return await message.channel.fetch_message(message.reference.message_id)

async def bot_log_info(msg: str):
    await bot.get_channel(1012684225553637476).send(f'`{datetime.datetime.now().strftime("[%Y/%m/%d, %H:%M:%S]")} [info] {msg}`')

async def bot_log_err(msg: str):
    await bot.get_channel(1012684225553637476).send(f'`{datetime.datetime.now().strftime("[%Y/%m/%d, %H:%M:%S]")} [error] {msg}`')

@bot.listen('on_ready')
async def on_ready():
    await bot_log_info('Shadow bot v0.3 is now online!')
    await bot_log_info(f'Using prefix {bot_prefix}')

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

@bot.event
async def on_command_error(ctx, error):
    error = getattr(error, 'original', error)
    output = ''.join(traceback.format_exception(error))
    await bot_log_err(output)
    print(output)

@bot.command()
async def say(ctx: commands.Context, *, arg: str):
    print(1/0)
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
