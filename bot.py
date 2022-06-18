import os
import time
import asyncio
import discord
from dotenv import load_dotenv
from discord.ext import commands
from time import strftime
from dateutil import parser
from datetime import datetime
from zoneinfo import ZoneInfo
import zoneinfo
#loop = asyncio.get_event_loop()

alarmtime = "06/18/2022, 12:25"
# for key in zoneinfo.available_timezones():
#     if key.startswith("America"):
#         print(key)
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
#GUILD = os.getenv('DISCORD_GUILD')
ctxg = 0
def time_module():
    print("time module in use")
    print (alarmtime)
    while True:
        time.sleep(0.5)
        #print (datetime.now())
        current_time = datetime.now(ZoneInfo("America/Chicago")).strftime("%m/%d/%Y, %H:%M")#hour %H min %M sec %S am:pm %p 
        print (current_time)###
        #print (ctxg)
        if current_time == alarmtime: # enter the time you wish 
            #CST 06/18/2022, 07:23, heroku 2022-06-18 12:23
            if ctxg != 0:
                print ("img sent")
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
async def changetime(ctx, *args):
    #print (args)
    global alarmtime
    alarmtime = args[0]+" "+args[1] 

    await ctx.send("alarm time changed to " + alarmtime)

@bot.command()
async def to_yuumi(ctx):
    print ("check")
    """showing image for gift"""
    await ctx.send("생일축하합니다!!!", file=discord.File("유미님생일_20220608.png"))

bot.run(TOKEN)
