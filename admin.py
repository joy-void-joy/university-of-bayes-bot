from discord.ext import commands
import discord
from contextlib import contextmanager
import typing

class Admin(commands.Cog, command_attrs={'hidden': True}):
    """Admin-only commands that make the bot dynamic."""

    def __init__(self, bot):
        self.bot = bot
        self.config = self.bot.config
        self.authorized_ids = self.config.list('authorized_ids', subcast=int)
        self.authorized_guilds = self.config.list('authorized_guilds', subcast=int)
        self.print_error = bot.utils.print_error

        # TODO: This should be an ordered set
        self.modules = {}
        self.command = ""

    async def cog_check(self, ctx):
        return ctx.author.id in self.authorized_ids and ctx.guild.id in self.authorized_guilds

    @commands.command()
    async def clear(self, ctx):
        self.modules = {}

    @commands.command()
    async def print(self, ctx):
        await ctx.send([i for i in self.bot.extensions])

    @contextmanager
    def change_error(self, subcontext, handler): 
        """Function to temporarilly change the error handler of a context"""
        try:
            old_handler = subcontext.command.on_error
        except AttributeError: 
            old_handler = None 

        async def new_error(a, ctx, b):
            if ctx == subcontext:
                await handler(a, ctx, b)
            elif old_handler:
                await old_handler(a, ctx, b)

        subcontext.command.error(new_error)

        try:
            yield subcontext 
        finally:
            if old_handler:
                subcontext.command.error(old_handler)

    @commands.command()
    async def run(self, ctx, *, command=""):
        self.command = command or self.command
        await ctx.invoke(self.load)

        ctx.message.content = f"{self.bot.command_prefix}{self.command}"
        subcontext = await self.bot.get_context(ctx.message)
        if not subcontext.command:
            await ctx.send("Parsing error")
            return

        async def on_error(_, ctx, a):
            await self.print_error(ctx)

        with self.change_error(subcontext, on_error):
            await self.bot.invoke(subcontext)

    @commands.command()
    async def load(self, ctx, *modules):
        """Reloads a module."""
        self.modules.update({m: None for m in modules})
        things_to_try = [self.bot.reload_extension, self.bot.load_extension]

        for module in self.modules:
            for f in things_to_try:
                try:
                    f(module)
                except (commands.ExtensionAlreadyLoaded, commands.ExtensionNotLoaded):
                    pass
                except Exception:
                    await self.print_error(ctx)
                else:
                    await ctx.send(f'{module} \N{OK HAND SIGN}')
                    break

    @commands.command()
    async def haltandcatchfire(self, ctx):
        raise TypeError

def setup(bot):
    bot.add_cog(Admin(bot))
