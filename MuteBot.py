import discord
from discord.utils import get

mute = True
client = discord.Client()

# mute or unmute user
async def toggleMute(user, mute):
    await client.server_voice_state(user, mute=mute)

@client.event
async def on_message(message):
    global mute

    # server specific
    server = client.get_server('870407583721222144')

    # only allow me to command bot :)
    if str(message.channel) != 'Direct Message with Logman':
        return

    # get message info
    userId = message.author.id
    user = server.get_member(userId)
    voicechannel = user.voice.voice_channel

    channel = discord.utils.get(client.get_all_channels(), server__name=str(server), name=str(voicechannel))

    # get members in voice channel
    member_ids = channel.voice_members

    for _, _ in enumerate(member_ids):
        await toggleMute(member_ids[0], mute)     
    
    # alternate between muting or unmuting
    if mute == True:
        mute = False
    else:
        mute = True

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

# get discord token
f=open("token.txt","r")
if f.mode == 'r':
    discordToken = f.read()
    
client.run(discordToken)    