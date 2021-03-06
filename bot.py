import discord 
import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()

intents.members = True

client = commands.Bot(command_prefix = '.', intents = intents)

@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

try:
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')
except FileNotFoundError:
    for filename in os.listdir('/cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')

# client.run(os.getenv('TOKEN'))
client.run(os.getenv('TOKEN'))