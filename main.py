# https://github.com/boehs/Verifly

import discord
import genkey
try:
    import config
except:
    print("Plese rename democonfig to config")

client = discord.Client()
users = []

@client.event
async def on_ready():
    print('Bot is ready. make sure you have created "users.txt" and "keys.txt" in your bots working directory')
    with open("urls.txt", "r") as file:
        for line in file.readlines():
            users.append(line.rstrip('\n'))

@client.event
async def on_member_join(member):
    if not member.guild == config.base:
        key = genkey(6, False)
        await client.send_message(member.id, "**PLEASE READ, YOU HAVE BEEN KICKED!** \n Your Unique Key: " + key + "\n join " + config.server + " and enter your key in #verify without ANYTHING ELSE. \n you will be kicked from vefifly, and you will be able to join your server. \n you MUST agree to discord TOS before prociding")
        await member.kick(reason="Has not verified")

client.run(config.token)