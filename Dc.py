GNU nano 8.7.1                                   dc.py                                   Modified
# Discord Auto Messenger with Token on Termux

import discord
import asyncio

TOKEN = 'YOUR_TOKEN'
CHANNEL_ID = YOUR_ CHANNEL_ID

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    channel = client.get_channel(1466527136155308279)
    while True:
        await channel.send('your message') #Your Message Here
        await asyncio.sleep(10)  # Wait for 25 seconds before sending the next message

client.run(TOKEN)
