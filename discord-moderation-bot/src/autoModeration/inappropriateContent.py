import discord

class InappropriateContent:
    def __init__(self, client):
        self.client = client

    async def detect_inappropriate_content(self, message):
        # Implement logic to detect inappropriate content in messages
        if "inappropriate" in message.content:
            await message.delete()
            await message.channel.send(f"{message.author.mention}, please refrain from using inappropriate language.")

def setup(client):
    inappropriate_content = InappropriateContent(client)
    client.add_cog(inappropriate_content)