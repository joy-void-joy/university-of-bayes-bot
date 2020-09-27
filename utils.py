from discord.ext import commands
import discord 
import urllib
import io
import colorsys

from traceback import format_exc
import sys

class Utils(commands.Cog): 
    @staticmethod
    async def find_or_create_role(guild, name, **kwargs):
        try:
            print([i for i in guild.roles if i.name == name])
            result = next(i for i in guild.roles if i.name == name)
        except StopIteration:
            result = await guild.create_role(name=name, **kwargs)
        return result

    @staticmethod
    async def send_embed(ctx: commands.Context, message: discord.Message, delete: bool =False, footer: str="", link="", title="", image=""):
        """Util function to send an embed for quoting or other purposes"""
        tosend = discord.Embed(description=message.content, timestamp=message.created_at) 
        tosend.title = title
        tosend.url = link

        if message.author:
            tosend.color = message.author.color if message.author.color != discord.Color.default() else discord.Embed.Empty
            tosend.set_author(name=message.author.display_name, icon_url=message.author.avatar_url)

        if footer:
            tosend.set_footer(icon_url=ctx.author.avatar_url, text=footer)
     
        if not image:
            try:
                image = [i.url for i in message.embeds] + [i.proxy_url for i in message.attachments]
            except ValueError:
                pass

        if image:
            if message.content:
                tosend.set_thumbnail(url=image)
            else :
                tosend.set_image(url=image)

        ### Sending
        await ctx.send(embed=tosend)

        if delete:
            try:
                await ctx.message.delete()
            except discord.errors.NotFound:
                pass

    @staticmethod
    def download_avatar(user: discord.Member, path: str):
        """Download the avatar of a user to path"""
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(str(user.avatar_url), filename=path)
        return path

    @staticmethod
    #TODO: Split this up
    async def print_error(ctx, func=format_exc): 
        to_print = func()
        list_messages = [to_print[i:i+1900] for i in range(0, len(to_print), 1900)]
        for i in list_messages:
            await ctx.send\
            ( 
                f"```python\n"
                f"{i}\n"
                f"```"
            )

def setup(bot):
    bot.add_cog(Utils())
    bot.utils = bot.get_cog(Utils.__name__)
