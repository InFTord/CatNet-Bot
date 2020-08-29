import discord # импортируем discord.py | pip install discord.py
from discord.ext import commands # discord.ext - фреймворк для создания команд боту, идёт вместе с discord.py

import json # модуль для работы с json

import asyncio # для работы с await и async

import requests # для работы с сайтами


config = json.load(open("config.json")) # конфиг


bot = commands.Bot(command_prefix=f'{config["prefix"]}') # создаём переменную с ботом под названием bot, выставляя стандартный префикс !, можно поменять


@bot.event
async def on_ready(): # ивент в библиотеке discord.py, который срабатывает когда бот включается
	print(f"Бот вошёл в сеть. Аккаунт: {bot.user}, ID аккаунта: {bot.user.id}") # вывод в консоль информации о том, что бот был запущен 


bot.run(f'{config["token"]}') # запуск бота, надо вставить токен бота который можно получить зайдя в https://discord.com/developers/applications в приложение вашего бота