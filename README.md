# YomiBot

A Discord frame data bot for Your Only Move Is HUSTLE. Currently running version 0.3.2, using Python 3.10.
Requires the following python libraries: os, json, discord, dotenv, discord.ext
Heavily based off of my previous BolboBot project, which in turn was based on the [old Tekken 7 frame bot](https://github.com/BKNR/mokujin) by BKNR.

Frame data acquired from Bowser, the [YomiHustle wiki](https://wiki.gbl.gg/w/YomiHustle), the character specific discords, and my own knowledge.

To use type "![CHARACTERNAME] [MOVE NAME]" in a Discord chat e.g. !cowboy horizontal slash
The bot can also be pinged to find out what version it's running and game version it's updated for.

## To install and run your own instance of YomiBot
- Download the files and extract to any particular location
- Create a Discord bot using the Discord Applications portal
- Create a file in the YomiBot folder called .env
- Inside the .env you should only have 2 lines:
>\# .env</p>
>DISCORD_TOKEN=[YOUR TOKEN HERE]
- Run yomibot.py to connect to discord
- The permissions integer for YomiBot is 115712

## The files
yomibot.py - The main body of the program.
alias.py - A giant dictionary. Used to check for move and character aliases so the user can type common alises or shortened names.
[CHARCTERNAME].json - Contains a specific character's movelist and the data for all those moves.
