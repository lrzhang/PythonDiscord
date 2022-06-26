# bot.py
import os
import discord
client = discord.Client(intents=discord.Intents.all())

#=====
TODAYS_SERVER_NAME = ""  # THIS SHOULD BE THE NAME OF THE CHANNEL WE WANT TODAY
ADMIN_CHANNEL_NAME = ""  # NAME OF CHANNEL THAT MESSAGES ARE SENT TO
ENTRY_MESSAGE = """RESERVATIONS are back! We will again be reserving two thirds of our seating for trivia playing patrons with the rest on a first come, first served basis.  Team size is limited to 10, but we are happy to arrange larger teams next to each other if they reserve early enough that we can make that arrangement.  Teams MUST have one player there by 6: 45 or your table WILL be given away to any waiting customers.

Thursdays are inside only for the time being, but there is music on the patio and we are actively working to figure out how to make it work with our good neighbors.

Patio is open, weather permitting, and I will make an announcement to let you know if we will be seating the patio for trivia by 5: 30."""

TOKEN = ""  # ENTER BOT TOKEN HERE
#=====

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

    global ADMIN_USER
    ADMIN_USER = client.get_user(104405951099961344)
    
    global ADMIN_CHANNEL
    global QUIZ_GUILD
    for guild in client.guilds:
        if guild.name == TODAYS_SERVER_NAME:
            QUIZ_GUILD = guild
            for channel in guild.channels:
                if channel.name == ADMIN_CHANNEL_NAME:
                    ADMIN_CHANNEL = channel

    print('Guild name is {0} and channel name is {1}'.format(QUIZ_GUILD.name, ADMIN_CHANNEL.name))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.name.startswith('team'):
        # Send to specific user
        # await ADMIN_USER.send(message.content)

        # Send to private channel
        await ADMIN_CHANNEL.send("{0} - {1}".format(message.channel.name, message.content))

    # if message.content.startswith('$hello'):
    #     await message.channel.send('Hello!')


@client.event
async def on_member_join(member):
    await member.send(ENTRY_MESSAGE)

client.run(TOKEN) 
