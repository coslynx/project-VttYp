spamLinks.py:

import discord

class SpamLinks:
    def __init__(self, client):
        self.client = client

    async def check_for_spam_links(self, message):
        spam_links = ["spam.com", "phishing.net", "malware.org"]
        
        for link in spam_links:
            if link in message.content:
                await message.delete()
                await message.channel.send(f"{message.author.mention}, please refrain from posting spam links.")
                break

    async def on_message(self, message):
        if not message.author.bot:
            await self.check_for_spam_links(message)

def setup(client):
    client.add_cog(SpamLinks(client))