# bot1.py
import os

from dotenv import load_dotenv
from discord.ext import commands
from googlesearch import search

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content == 'hi':
        await message.channel.send("hey")
    await bot.process_commands(message)


@bot.command()
async def google(ctx, *, name):
    """
    This method return the urls of the first five results of the google search with the given query string <name>
    """
    f = open("storage.txt", "a+")
    f.write(name + '\n')
    f.close()
    for j in search(name, tld="com", num=5, stop=5, pause=2):
        await ctx.send(j)


@bot.command()
async def recent(ctx, *, name):
    """
    This method returns the recent searches having the string <name> in it.
    """
    f = open("storage.txt", "r")
    query_strings = list(f)
    for string in query_strings:
        if name in string:
            await ctx.send(string)


@bot.event
async def on_command_error(ctx, error):
    """
    Handles the exception raised by any of the functions with both.command decorator.
    """
    # In case the query string is not provided
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send('No query string entered.')

bot.run(TOKEN)

