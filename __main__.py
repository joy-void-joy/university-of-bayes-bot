import os
import discord
from environs import Env
from discord.ext import commands
from dataclasses import dataclass

description = """
Your description here
""" 

bot = commands.Bot\
(
    command_prefix="plz ",
    description=description,
)

### Classses
@dataclass
class MessageInfo:
    author: discord.Member = discord.Embed.Empty
    content: str = discord.Embed.Empty
    created_at = discord.Embed.Empty
bot.MessageInfo = MessageInfo

@dataclass
class AvatarInfo:
    avatar_url: str = ''
bot.AvatarInfo = AvatarInfo

### Config reload
def reload_config():
    Env.read_env('.env.default')
    Env.read_env('.env', override=True)
bot.reload_config = reload_config

### Login info
@bot.listen('on_ready')
async def login():
    print('--------------')
    print(bot.user.name)
    print(bot.user.id)
    print('--------------')

    ### Loading
    bot.load_extension('utils') 
    bot.load_extension('config') 
    bot.load_extension('admin')
    bot.load_extension('feedback')

### Running
env = Env()
bot.reload_config()
bot.run(env.str('token')) 
