import discord

loop = 1
client = discord.Client()

@client.event
async def on_ready():
    print('CONSOLE: We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$lfeed'):
        while loop == 1:
            await message.channel.send(input('CONSOLE: Append to message: '))

client.run('TOKEN GOES HERE')
