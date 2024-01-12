import os
from typing import Final
from dotenv import load_dotenv
from replies import get_reply
from discord import Intents, Client, Message

#loading discord token
token = load_dotenv(os.getenv('DISCORD_TOKEN'))
print(token)

#setting up bot
#1 setting up intents
intents = Intents.default()
intents.message_content = True
#2 setting up clients
clients = Client(intents=intents)

async def send_message(user_message):
    if not user_message:
        print('Empty message because intents were not enabled')
        return
    is_private = user_message[0] == '?'
    if is_private:
        user_message = user_message[1:]

    try:
        reply = get_reply(user_message)
        await message.author.send(reply) if is_private else message.channel.send(reply)