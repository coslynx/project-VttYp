filename: welcomeMessages.py

import discord

class WelcomeMessages:
    def __init__(self, client):
        self.client = client

    async def send_welcome_message(self, member):
        # Customize the welcome message here
        welcome_channel = discord.utils.get(member.guild.text_channels, name="welcome")
        await welcome_channel.send(f"Welcome {member.mention} to our server! Enjoy your stay.")

    async def on_member_join(self, member):
        await self.send_welcome_message(member)

    async def on_ready(self):
        print('Bot is ready!')

    async def on_disconnect(self):
        print('Bot disconnected')

    async def on_error(self, event, *args, **kwargs):
        print('An error occurred')

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('Invalid command used.')

    async def on_message(self, message):
        if message.author == self.client.user:
            return

        if message.content == 'hello':
            await message.channel.send('Hello! How can I help you today?')

    async def on_message_delete(self, message):
        author = message.author
        content = message.content
        channel = message.channel
        await channel.send(f'{author}\'s message: {content} was deleted.')

    async def on_message_edit(self, before, after):
        author = before.author
        content_before = before.content
        content_after = after.content
        channel = before.channel
        await channel.send(f'{author} edited their message from "{content_before}" to "{content_after}".')

    async def on_member_remove(self, member):
        goodbye_channel = discord.utils.get(member.guild.text_channels, name="goodbye")
        await goodbye_channel.send(f"{member.display_name} has left the server. Goodbye!")

    async def on_member_ban(self, guild, user):
        ban_channel = discord.utils.get(guild.text_channels, name="ban-logs")
        await ban_channel.send(f"{user.display_name} has been banned from the server.")

    async def on_member_unban(self, guild, user):
        unban_channel = discord.utils.get(guild.text_channels, name="ban-logs")
        await unban_channel.send(f"{user.display_name} has been unbanned from the server.")

    async def on_guild_join(self, guild):
        general_channel = discord.utils.get(guild.text_channels, name="general")
        if general_channel:
            await general_channel.send("Thanks for adding me to your server! Type !help for a list of commands.")
        else:
            print("General channel not found in the guild.")