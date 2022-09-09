# This example requires the 'members' and 'message_content' privileged intents to function.

import discord
from discord.ext import commands
from dotenv import load_dotenv
import os
import random

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

description = """Trivia bot in Discord"""

intents = discord.Intents.default()
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix='?', description=description, intents=intents)

general = "general"

@bot.event
async def on_message(message):
    """Creates a private channel for a team on the user's first post in #general."""
    if message.channel.name != general: return
    if message.author.bot: return
    if any(channel_num(channel.name) is None or message.author in channel.members for channel in team_channels(message.channel.guild)): return

    overwrites = {
        message.channel.guild.default_role: discord.PermissionOverwrite(read_messages=False),
        message.channel.guild.me: discord.PermissionOverwrite(read_messages=True),
        message.author: discord.PermissionOverwrite(read_messages=True)
    }
    channelID = max(team_channels(message.channel.guild), default=0)+1
    channel = await message.channel.guild.create_text_channel(str(channelID)+"-"+message.content.replace(" ","-"),overwrites=overwrites)

def team_channels(guild):
    return (channel for channel in guild.text_channels if channel_num(channel.name) is not None)

def channel_num(channel_name):
    return parse_int(channel_name.split("-")[0])

def parse_int(s: str):
    return int(s) if s and s.isdigit() else None

bot.run(TOKEN)
