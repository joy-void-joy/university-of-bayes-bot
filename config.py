from environs import Env
from discord.ext import commands
import discord

class Config(commands.Cog, command_attrs={'hidden': True}):
    """Module for configuration settings. Complement Admin"""

    def __init__(self, bot):
        self.bot = bot
        self.config = Env()

        ### Parsers for discord types
        @self.config.parser_for('channel')
        def channel_parser(value, ctx):
            return commands.TextChannelConverter().convert(ctx, value)

        bot.config = self.config
        self.bot.reload_config()

        self.authorized_ids = self.config.list('authorized_ids', subcast=int)
        self.authorized_guilds = self.config.list('authorized_guilds', subcast=int)

    async def cog_check(self, ctx):
        return ctx.author.id in self.authorized_ids and ctx.guild.id in self.authorized_guilds

    @commands.command()
    async def reload_config(self, ctx):
        self.bot.reload_config()

    @commands.command()
    async def set(self, ctx, key, value):
        os.environ[key] = value

def setup(bot):
    bot.add_cog(Config(bot))
