from discord.ext import commands
import discord
import typing

class Feedback(commands.Cog):
    """Make anonymous feedback/messages"""

    def __init__(self, bot):
        self.bot = bot
        self.config = bot.config

    @commands.command()
    async def feedback(self, ctx, chan: typing.Optional[discord.TextChannel], *, message):
        """Send a message in a channel. Default to #feedback"""
        chan = chan or await self.config.channel('feedback_chan', ctx=ctx)
        await chan.send(message)

    @commands.Cog.listener('on_message')
    async def om_feedback(self, message):
        """Treat private message as feedback to send"""
        if not isinstance(message.channel, discord.DMChannel) or message.author.bot or message.content.startswith(self.bot.command_prefix):
            return
        message.content = f"{self.bot.command_prefix}{self.feedback.name} {message.content}"
        subcontext = await self.bot.get_context(message)
        await self.bot.invoke(subcontext)


def setup(bot):
    feedback = bot.add_cog(Feedback(bot))
