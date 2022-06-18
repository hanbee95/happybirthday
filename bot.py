import os

import asyncio
import discord
from dotenv import load_dotenv
from discord.ext import commands
from time import strftime
from dateutil import parser
from datetime import datetime

#loop = asyncio.get_event_loop()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
#GUILD = os.getenv('DISCORD_GUILD')
ctxg = 0
def time_module():
    print("time module in use")
    while True:
        #print (datetime.now())
        current_time = datetime.now().strftime("%m/%d/%Y, %H:%M")#hour %H min %M sec %S am:pm %p 
        #print (current_time)###
        #print (ctxg)
        if current_time == "06/18/2022, 02:20": # enter the time you wish 
            if ctxg != 0:
                print ("send")
                asyncio.run_coroutine_threadsafe(to_yuumi(ctxg), bot.loop)
            print("time module ended")
            break

client = discord.Client()
bot = commands.Bot(command_prefix='&', description='Happy Birthday Alarm')

@bot.event
async def on_ready():
    #HAN From here to guild fetching
    GUILD = []
    async for guild_fetch in bot.fetch_guilds(limit=150):
        GUILD.append(guild_fetch.name)    
    print(f"Allowed servers: {GUILD}")
    #HAN to here to guild fetching

    for guild in client.guilds:
        print("Was added to the servers list")

    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('-'*20)
    await bot.change_presence(activity=discord.Game(name='&help'))

@bot.command()
async def pre(ctx):
    """storing ctx"""
    await ctx.send("-"*20)
    global ctxg 
    ctxg = ctx
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    asyncio.get_event_loop()    
    time_module()
    
@bot.command()
async def to_yuumi(ctx):
    print ("check")
    """showing image for gift"""
    await ctx.send("생일축하합니다!!!", file=discord.File("유미님생일_20220608.png"))

bot.run(TOKEN)
