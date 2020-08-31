import discord
from discord.ext import commands

class Moderation(commands.Cog):

	def __init__(self, bot):
		self.bot = bot

	@commands.command(name='кик',
		aliases=['kick', 'кикнуть'],
		description='Вы можете кикнуть кого то с сервера',
		usage='[юзер] [причина]'
	) 
	@commands.has_permissions(kick_members=True)
	async def kicking(self, ctx, member: discord.member, reason=None):
		if not member:
			return await ctx.send(embed = discord.Embed(description = f'**:warning: Правильное использование команды: `kick @пользователь причина`', color=0x800080))
		if member.id == ctx.guild.owner.id:
			return await ctx.send(embed = discord.Embed(description = f'**:warning: Данный пользователь, {member.mention}, является создателем этого сервера!**', color=0x800080))
		if member.id == ctx.guild.me.id:
			return await ctx.send(embed = discord.Embed(description = f'**:warning: Я не могу кикнуть самого себя!**', color=0x800080))
		if ctx.author.top_role.position < member.top_role.position:
			return await ctx.send(embed = discord.Embed(description = f'**:warning: Эм... Это троллинг? Ты не можешь кикнуть человека с позицией выше твоей!**', color=0x800080))
		if member.id == ctx.author.id:
			return await ctx.send(embed = discord.Embed(description = f'**:warning: Напомню, суицид - это не выход!**', color=0x800080))
		if member.top_role > ctx.guild.me.top_role:
			return await ctx.send(embed = discord.Embed(description = f'**:warning: Я не могу кикнуть {member.mention}, так как его роль выше моей!**', color=0x800080))
			await ctx.guild.kick(member=member, reason=reason)

		if reason is None:
			embed1 = discord.Embed(title=f"{ctx.author.name} кикнул {member.name}", description=f"Причина не указана.")
			await ctx.send(embed=embed1)

		else:
			embed = discord.Embed(title=f"{ctx.author.name} кикнул {member.name}", description=f" Причина кика: { reason } ")
			await ctx.send(embed=embed)





def setup(bot):
	bot.add_cog(Moderation(bot))

