import discord

class AutomatedKickBan(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        if ctx.message.author.guild_permissions.kick_members:
            await member.kick(reason=reason)
            await ctx.send(f'{member.mention} has been kicked.')
        else:
            await ctx.send('You do not have permission to kick members.')

    @commands.command()
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        if ctx.message.author.guild_permissions.ban_members:
            await member.ban(reason=reason)
            await ctx.send(f'{member.mention} has been banned.')
        else:
            await ctx.send('You do not have permission to ban members.')

def setup(client):
    client.add_cog(AutomatedKickBan(client))