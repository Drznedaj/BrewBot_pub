import discord
from discord.ext import commands
import random
import time
import asyncio
import datetime

random.seed(time.time())
helps = '```python Hello this is BrewBot 🤖, i serve drinks and such.... 100110 \nBeep BOOP beep 0x01101101111001 \nTo order something from the list use ?\nFor example ?mead\n\n'

bot = commands.Bot(command_prefix='?',description=helps)
bot.remove_command('help')

max_hogs = 10
hog_count = max_hogs

@bot.command()
async def help(ctx):
    await ctx.send(helps+'Menu items:\n\tale - The finest ale in town\n\tmead - Golden mead\n\tstout - Bold dark dwarven stout\n\twhiskey - Fiery whiskey from the depts of hell\n\trum - Beloved by pirates, imported from the Golden Sea islands\n\twine - Bottle, or if you prefer a glass of our signature wine\n\tbread - Made with love\n\thog - Available on request or form friday to sunday while the supply lasts\n\troom - Enjoy your stay, and don\'t forget to tip!```')

@bot.command(help='Finest ale in town')
async def ale(ctx):
    n = random.randint(0,3)
    what = 'tasty ale'
    if n == 1:
        what = 'frothy mug of ale'
    elif n == 2:
        what = 'mug of ale, filled to the brim'
    await ctx.send('BrewBot brings {0.author.mention} a {1}'.format(ctx.message,what))

@bot.command()
async def mead(ctx):
    msg = 'BrewBot brings {0.author.mention} mead'.format(ctx.message)
    n = random.randint(0,100)
    if n > 50:
        msg = 'BrewBot opens a door on his left side torso panel and pulls out a glass. He then brings his finger up and pours some delicious mead into it. There you go {0.author.mention}! beep BOOP'.format(ctx.message)
    await ctx.send(msg)

@bot.command()
async def stout(ctx):
    await ctx.send('BrewBot brings {0.author.mention} stout'.format(ctx.message))

@bot.command()
async def whiskey(ctx):
    await ctx.send('BrewBot brings {0.author.mention} fiery whiskey'.format(ctx.message))

@bot.command()
async def rum(ctx):
    await ctx.send('BrewBot closes his eyes, you hear cogs turning, a small amount of steam flys out from seams of the robots body, after a few seconds a small door opens on the chest pannel and a shot of finest rum rolls out. Here you go {0.author.mention}, enjoy!'.format(ctx.message))

@bot.command()
async def wine(ctx):
    if 'glass' in ctx.message.content:
        msg = 'BrewBot brings {0.author.mention} a glass of wine'.format(ctx.message)
    elif 'bottle' in ctx.message.content:
        msg = 'BrewBot brings {0.author.mention} a bottle of wine'.format(ctx.message)
    else:
        msg = 'Do you want a glass of wine or a bottle, {0.author.mention}?'.format(ctx.message)
    await ctx.send(msg)

@bot.command()
async def bread(ctx):
    await ctx.send('BrewBot brings {0.author.mention} bread'.format(ctx.message))

@bot.command()
async def hog(ctx):
    global hog_count
    msg = 'BrewBot brings {0.author.mention} a hog 100101101'.format(ctx.message)
    if datetime.datetime.today().weekday() >= 4 and hog_count > 0:
        await ctx.send('We currently have {} hogs ranging from 15 to 35 kg, BrewBot shall bring you one as soon as it is ready'.format(hog_count))
        hog_count -= 1
        await asyncio.sleep(3)
        msg = 'BrewBot brings {0.author.mention} a {1}kg hog'.format(ctx.message,random.randint(15,35))
    elif datetime.datetime.today().weekday() < 4 and hog_count == 0:
        hog_count = max_hogs
        msg = 'BrewBot nods, goes behind the bar and pulls out an abacus... You see him calculating something on it. BrewBot then takes a small piece of paper and pulls it through some sort of mechanism on his wrist and pinns it to something behind the bar.'
    elif datetime.datetime.today().weekday() >= 4 and hog_count == 0:
        msg = 'Sorry but we are all out of hogs today'
    else:
        print(hog_count)
        await ctx.send('It will take some time to prepare the hog, please be patient')
        hog_count -= 1
        await asyncio.sleep(60)

    await ctx.send(msg)

@bot.command()
async def room(ctx):
    await ctx.send('Okay {0.author.mention}, here are the keys to your room, enjoy your stay! BEEP BOOP BEEP'.format(ctx.message))

@bot.command()
async def meal(ctx):
    print(ctx.message)
    await ctx.send('BrewBot brings {0.author.mention} a tasty meal'.format(ctx.message))

@bot.event
async def on_command_error(ctx,exception):
    msg = 'ERROR 404 ERROR command not found...'
    if 'bottle' in ctx.message.content:
        msg = 'Did you mean to order a wine bottle {0.author.mention}? You can do that with ?wine bottle 😊'.format(ctx.message)
    elif 'glass' in ctx.message.content:
        msg = 'Did you mean to order a glass of wine {0.author.mention}? You can do that with ?wine glass 😊'.format(ctx.message)

    await ctx.send(msg)

bot.run('token goes here :)')
