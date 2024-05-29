import discord
from discord.ext import commands, tasks
import datetime

class ScheduledMessages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.scheduled_messages.start()

    @tasks.loop(seconds=60)
    async def scheduled_messages(self):
        current_time = datetime.datetime.now().strftime("%H:%M")
        # Add your scheduled messages logic here
        if current_time == "08:00":
            channel = self.bot.get_channel(1234567890)  # Replace with your channel ID
            await channel.send("Good morning everyone!")
        elif current_time == "12:00":
            channel = self.bot.get_channel(1234567890)  # Replace with your channel ID
            await channel.send("Lunch time!")
        elif current_time == "18:00":
            channel = self.bot.get_channel(1234567890)  # Replace with your channel ID
            await channel.send("Time for dinner!")

    @scheduled_messages.before_loop
    async def before_scheduled_messages(self):
        await self.bot.wait_until_ready()

def setup(bot):
    bot.add_cog(ScheduledMessages(bot))