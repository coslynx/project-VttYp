import discord

class CustomCommands:
    def __init__(self, client):
        self.client = client

    async def execute_custom_command(self, message):
        if message.content.startswith('!custom'):
            command = message.content.split(' ')[1]
            if command == 'hello':
                await message.channel.send('Hello!')
            elif command == 'bye':
                await message.channel.send('Goodbye!')
            # Add more custom commands here as needed

    async def on_message(self, message):
        await self.execute_custom_command(message)