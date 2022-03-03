import discord 
import os
from discord.ext import commands

intents = discord.Intents.default()

intents.members = True
TOKEN = 'OTQ3NTY0NDE0NjkxODQ0MTI2.YhvGIQ.WG7hRl6-yhdbpPm_axJtS0KQTdI'

client = commands.Bot(command_prefix = '.', intents = intents)

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(os.getenv('TOKEN'))