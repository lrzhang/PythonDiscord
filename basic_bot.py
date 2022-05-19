# This example requires the 'members' and 'message_content' privileged intents to function.

import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

@bot.command()
async def join(ctx, *team: str):
    """Creates a private channel for a given team."""
    
    overwrites = {
        ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
        ctx.guild.me: discord.PermissionOverwrite(read_messages=True),
        ctx.message.author: discord.PermissionOverwrite(read_messages=True)
    }
    channelID = max(parseInt(channel.name.split("-")[0]) for channel in ctx.guild.text_channels)+1
    channel = await ctx.guild.create_text_channel(str(channelID)+"-"+"-".join(team),overwrites=overwrites)
    # TODO send message in channel
    # TODO check if user already has a private channel and alert them to use that channel

def parseInt(s: str):
    return int(s) if s and s.isdigit() else 0

bot.run("OTc2NjY0NjMxMTY4ODcyNDg4.G7oy8k.1Sd-R7TbmnRnJ-Obkpp4HIVeSrugMbPXzJf-hg")
