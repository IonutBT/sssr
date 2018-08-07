import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random

Client = discord.Client()
bot = commands.Bot(command_prefix="yg!")
lines = open(r'accounts.txt').read().splitlines()

@bot.event
async def on_ready():
    print("The bot is online!")

@bot.command(pass_context=True)
async def gen(ctx):
    userName = ctx.message.author.name
    userID = ctx.message.author.id

    if ctx.message.server:
        await bot.delete_message(ctx.message)
    myline = random.choice(lines)
    split = myline.partition(":")
    
    embed=discord.Embed(title="Minecraft Account", color=0xf45eff)
    embed.set_thumbnail(url="http://www.minecraft4all.com/images/pic02.png")
    embed.add_field(name="Email:", value=split[0], inline=False)
    embed.add_field(name="Password:", value=split[2], inline=False)
    await bot.send_message(ctx.message.author, embed=embed)

    print("{} Typed yg!gen".format(userName))

bot.run("NDc2MzU4OTA3MzA5MDY0MTky.DkscPw.w34WVpxIsp_nvpZh8rFe3tyRO1E")
