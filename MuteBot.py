import requests
import json
import time
from datetime import datetime
import asyncio
import aiohttp
import os
import discord
from discord.utils import get

toggle = False
client = discord.Client()
discordToken = ""

async def toggleMute(person, flag):
    if flag == True:
        await client.server_voice_state(person,mute=False)
    else:
        await client.server_voice_state(person,mute=True)

@client.event
async def on_message(message):
    
    server = client.get_server('764614850285535312')

    if str(message.channel) != 'Direct Message with Logman':
        print(message.channel)
        print(message)
        print('returning')
        return

    userId = message.author.id
    user = server.get_member(userId)
    voicechannel = user.voice.voice_channel

    global toggle

    channel = discord.utils.get(client.get_all_channels(), server__name=str(server), name=str(voicechannel))

    member_ids = channel.voice_members

    for x in member_ids:
        await toggleMute(member_ids[0],toggle)     
    
    if toggle == True:
        toggle = False
    else:
        toggle = True


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    #print(discord.version_info)
    
client.run(discordToken)    