from asyncio.windows_events import NULL
import discord

client = discord.Client()

adminDM = None

@client.event
async def on_ready():
    global adminDM
    print('We have logged in as {0.user}'.format(client))
    adminUser = await client.fetch_user(265016130802941953)
    adminDM = await adminUser.create_dm()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.name.startswith("answerchannel"):
        if adminDM != None:
            print(message.author.id)
            await adminDM.send(message.content + " (from " + message.channel.name + ")")
    elif message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('OTc2NjY1MDQ4NjgyNDc5NjI3.GbbfYS.uZDTiEyj5eKJvYCqcelmfilYs8Fh9ynmzC1qBQ')
