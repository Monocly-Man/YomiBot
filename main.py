# Your Only Move Is HUSTLE Bot (yomibot), by Monocly Man
# Created 14th of January 2023 in python version 3.10.something
# Last edited 14th January 2023

# Largely based off a previous project called bolbobot
# Basically same bot but a different game
import os
import json
import discord
from dotenv import load_dotenv
from discord.ext import commands

import alias

# Variables
__version__ = str("0.3.2, images coming later")
__gamever__ = str("0.10.12, ninja and cowboy only")
dirname = os.path.dirname(__file__)
imglink = str("https://wiki.gbl.gg/images/f/fa/YH_Cowboy_HSlash.png")


# Functions
def get_move(move_name, character):
    filepath = dirname + "/" + character + ".json"
    if not filepath:
        return discord.Embed(title="Move not found in {}'s movelist".format(character), colour=0x1f3c80)
    with open(filepath) as movelist_file:
        contents = movelist_file.read()
    movelist_json = json.loads(contents)

    move_details = list(filter(lambda x: (x['Move'].lower() == move_name), movelist_json))

    return move_details[0]


def move_embed(move):
    embed = discord.Embed(title=move['Move'], colour=0x1f3c80)
    embed.set_thumbnail(url=imglink)

    # Shut the fuck up I know it's ugly i cbf to make it nicer
    embed.add_field(name='Start Up \u200B', value=move['Startup'], )
    embed.add_field(name='IASA \u200B', value=move['IASA'])
    embed.add_field(name='Active \u200B', value=move['Active'])
    embed.add_field(name='Damage', value=move['Damage'])
    embed.add_field(name='Resource', value=move['Resource'])
    embed.add_field(name='Proration', value=move['Proration'])
    embed.add_field(name='Notes', value=move['Notes'])

    return embed


# Main
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
# intents = discord.Intents.default()
# intents.message_content = True

bot = commands.Bot(command_prefix='y! ')  # , intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord! Running version {__version__}\n'
          f'----------------------------------------'
          )


@bot.event
async def on_message(ctx):
    if ctx.author.bot:
        return

    elif bot.user.mentioned_in(ctx) and ctx.mention_everyone is False:
        await ctx.channel.send("Running YomiBot version {}\n"
                               "Updated for game version {}\n".format(__version__, __gamever__))
        return

    elif not ctx.content.startswith("!"):
        return

    message = ctx.content.replace("!", "").lower()
    character, move = message.split(" ", 1)

    # Searches alias.py for the character
    character_alias = list(filter(lambda x: (character in x["alias"]), alias.CHARACTER_NAMES))
    if character_alias:
        character = character_alias[0]["name"]
        # Searches alias.py for aliases
        move_alias = list(filter(lambda x: (move in x["alias"]), alias.MOVE_NAMES))
        if move_alias:
            move = move_alias[0]["name"]
            # I know using try except is lazy and bad but i am lazy and bad
            try:
                response = move_embed(get_move(move, character))
            except IndexError:
                response = discord.Embed(title="Move found but no data found", colour=0x1f3c80)

        else:
            response = discord.Embed(title="Move not found", colour=0x1f3c80)

    else:
        response = discord.Embed(title="Character not found", colour=0x1f3c80)

    await ctx.channel.send(embed=response)  # , delete_after=20)


@bot.command(name="version", help="Gets the current bot version and game version the bot is updated for.")
async def version(ctx):
    await ctx.channel.send("Running YomiBot version {}\n"
                           "Updated for game version {}\n".format(__version__, __gamever__))
    return


# Runs bot
bot.run(TOKEN)
