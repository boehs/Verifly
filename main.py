# https://github.com/boehs/Verifly

import discord
import genkey
try:
    import config
except:
    print("Plese rename democonfig to config")
from captcha.image import ImageCaptcha
from PIL.ImageFont import truetype
import os

image = ImageCaptcha(fonts=[r"BOD_R.ttf"])

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

users = []
keys = []

@client.event
async def on_ready():
    print('Bot is ready. make sure you have created "users.txt" and "keys.txt" in your bots working directory')
    with open("users.txt", "r") as file:
        for line in file.readlines():
            users.append(line.rstrip('\n'))
    file.close()
    await client.wait_until_ready()

@client.event
async def on_member_join(member):
    users = []
    with open("users.txt", "r") as file:
        for line in file.readlines():
            users.append(line.rstrip('\n'))
    try:
        valid = users.index(str(member.id))
    except:
        if member.guild.id == config.base:
            pass
        else:
            key = genkey.genkey(6, False)
            image.write(key, 'tempcapcha.png')
            await member.send("**PLEASE READ, YOU HAVE BEEN KICKED!** \n join " + config.server + " and enter your capcha in #verify without ANYTHING ELSE (case sensitive). \n you will be kicked from verifly, and you will be able to join your server. \n you MUST agree to discord TOS before proceeding", file=discord.File("tempcapcha.png"))
            await member.kick(reason="Has not verified")
            os.remove("tempcapcha.png")

@client.event
async def on_message(message):
    if message.guild.id == config.base:
        if message.author == client.user:
            return
        else:
            keys = []
            with open("keys.txt", "r") as keystxt:
                for line in keystxt.readlines():
                    keys.append(line.rstrip('\n'))
            keystxt.close()
            msg = message.content
            try:
                iskey = keys.index(msg)
            except ValueError:
                await message.author.send("Hey mate! that key aint look too valid, sorry. if you think this is a issue, open a issue @ https://github.com/boehs/Verifly")
                await message.delete()
            else:
                keys.remove(str(msg))
                with open("keys.txt", 'w') as output:
                    for row in keys:
                        output.write(str(row) + '\n')
                output.close()
                users = open("users.txt","a")
                users.write(str(message.author.id) + "\n")
                users.close()
                await message.author.send("Hey! thanks so much for verifying. it sucks but we are keeping discord safe! feel free to join the server you were trying to join before! if you still run into issues, open a issue @ https://github.com/boehs/Verifly")
                await message.delete()
                await message.author.kick(reason = "Verified :)")

client.run(config.token)