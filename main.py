# -*- coding: utf-8 -*-

import discord
import random
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import requests
import os

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith("!team"):
        name_list = list(message.author.voice.channel.members)
        await message.channel.send(message.author.voice.channel.members)
        random.shuffle(name_list)
        A = []
        B = []
        for i in range(len(name_list)):
            if i % 2 == 0:
                n = str(name_list[i]).split("#")
                A.append(n[0])
            else:
                n = str(name_list[i]).split("#")
                B.append(n[0])
        A = "A: " + ', '.join(A)
        B = "B: " + ', '.join(B)
#        await client.send_message(message.channel, A)
        await message.channel.send(A)
#        await client.send_message(message.channel, B)
        await message.channel.send(B)
        
#    if message.content.startswith("wait"):
#        await client.send_file(message.channel, "D:\\discord\\wait.jpg")

#    if message.author.name=="SFN":
#        await client.send_file(message.channel, "D:\\discord\\unknown.png")

client.run(str(os.environ.get('BOT_TOKEN')))
