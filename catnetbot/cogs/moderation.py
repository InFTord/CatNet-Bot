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
	async def kicking(self, ctx, member: discord.Member, *, reason=None):
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
			
		if reason is None:

			embed = discord.Embed(title="Кик", colour = discord.Color.red())
			embed.add_field(name='Кто был кикнут?', value=f"{member.name}", inline=False)
			embed.add_field(name='Кем был выдан кик?', value=f"{ctx.author.name}", inline=False)
			embed.add_field(name='Причина кика?', value="Не указана", inline=False)
			embed.set_footer(text=f"Фан факт, этот кик возможно попадет в КэтНет бота.",icon_url=ctx.message.author.avatar_url)
			await member.kick(reason='Не указана.')
			await ctx.send(embed=embed)

		else:
			embed1 = discord.Embed(title="Кик", colour = discord.Color.red())
			embed1.add_field(name='Кто был кикнут?', value=f"{member.name}", inline=False)
			embed1.add_field(name='Кем был выдан кик?', value=f"{ctx.author.name}", inline=False)
			embed1.add_field(name='Причина кика?', value=f"{reason}", inline=False)
			embed1.set_footer(text=f"Фан факт, этот кик возможно попадет в КэтНет бота.",icon_url=ctx.message.author.avatar_url)
			await member.kick(reason=reason)
			await ctx.send(embed=embed1)
	


def setup(bot):
	bot.add_cog(Moderation(bot))

