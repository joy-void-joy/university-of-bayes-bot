### This is just a template to copy

from discord.ext import commands

class Example(commands.Cog):
    def __init__(self, bot, authorized_ids=[], authorized_guilds=[]):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        """Called with ``plz hello`` or ``plz run hello`` in the dev server"""
        await ctx.send("Hello world")

def setup(bot):
    bot.add_cog(Example(bot))
