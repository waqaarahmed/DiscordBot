import os
from typing import Final
from dotenv import load_dotenv
from replies import get_reply
from discord import Intents, Client, Message

#loading discord token
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

#setting up bot
#1 setting up intents
intents = Intents.default()
intents.message_content = True
#2 setting up clients
client = Client(intents=intents)

async def send_message(message, user_message):
    if not user_message:
        print('Empty message because intents were not enabled')
        return
    is_private = user_message[0] == '?'
    if is_private:
        user_message = user_message[1:]

    try:
        reply = get_reply(user_message)
        await message.author.send(reply) if is_private else await message.channel.send(reply)
    except Exception as e:
        print(e)
@client.event
async  def on_ready():
    print(f'{client.user} is now running')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    username = str(message.author)
    user_message = message.content
    channel = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)

def main() -> None:
    client.run(token=token)


if __name__ == '__main__':
    main()