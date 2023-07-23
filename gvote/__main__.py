# This example requires the 'message_content' privileged intent to function.

import discord
import random
import asyncio


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        # we do not want the bot to reply to itself
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!!gvote '):
            await message.channel.send('Guess a number between 1 and 10.')


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('token')