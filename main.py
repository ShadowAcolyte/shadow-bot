import discord
import os
import util
import traceback
from discord.ext import commands

intents = discord.Intents.all()

bot = commands.AutoShardedBot(
    command_prefix=os.getenv("BOT_PREFIX", "$"), intents=intents
)


@bot.listen("on_ready")
async def on_ready():
    await util.log.info("Shadow bot v0.3 is now online!")
    await util.log.info(f"Using prefix {os.getenv('BOT_PREFIX', '$')}")

    # load cogs
    for filename in os.listdir("cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
            await util.log.info(f"Loaded cog: {filename}")

    if os.getenv("TESTING_GUILD_ID"):
        guild = discord.Object(int(os.getenv("TESTING_GUILD_ID")))
        bot.tree.copy_global_to(guild=guild)
        await bot.tree.sync(guild=guild)
    else:
        await bot.tree.sync()
    await util.log.info("Slash commands have been synced.")


@bot.event
async def on_command_error(ctx: commands.Context, error):
    error = getattr(error, "original", error)
    if isinstance(error, commands.CommandNotFound):
        await ctx.reply(f"Command {ctx.command} does not exist.")
    output = "".join(traceback.format_exception(error))
    await util.log.err(output)
    print(output)


bot.run(os.getenv("DISCORD_TOKEN"))
