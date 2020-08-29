import discord # импортируем discord.py | pip install discord.py
from discord.ext import commands # discord.ext - фреймворк для создания команд боту, идёт вместе с discord.py
import asyncio # для работы с await / asyncio

class cat(commands.Cog): # создаём класс с когом
	
	def __init__(self, bot): # инициализация кога
		self.bot = bot # создание переменной бота

	@commands.command(name='кот')
	async def cat(self, ctx):
		response = requests.get('https://aws.random.cat/meow')
		data = response.json()
		await message.channel.send(data['file'])

def setup(bot): # функция
	bot.add_cog(cat(bot)) # добавляем ког 
	print(f"Ког cat готов!") # запуск кога