"""Ког с ошибками"""
import discord
from discord.ext import commands
import toml_config  # я не помню откуда питон ищет модули, вроде из места запуска

# На этом моменте может что ни будь сломаться т.к. не проверял, но должно работать

conf = toml_config.load_config()["messages"]["errors"]

PREFIX = toml_config.load_config()["bot"]["prefix"]

SUCCESS_LINE = conf["success_line"]["emoji"] * conf["success_line"]["repeat"] + "\n "
SUCCESS_COLOR = conf["success_line"]["color"]

STANDART_LINE = conf["standard_line"]["emoji"] * conf["standard_line"]["repeat"] + "\n⠀"
STANDART_COLOR = conf["standard_line"]["color"]

ERROR_LINE = conf["error_line"]["emoji"] * conf["error_line"]["repeat"] + "\n⠀"
ERROR_COLOR = conf["error_line"]["color"]

INVISIBLE_SYMBOL = conf["invisible_symbol"]


class Errors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        async def own_command_error_message(problem, solution):
            embed = discord.Embed(color=ERROR_COLOR)
            embed.add_field(name="Проблема:", value=f"{problem}")
            embed.add_field(
                name=f"{INVISIBLE_SYMBOL}", value=f"{ERROR_LINE}", inline=False
            )
            embed.add_field(name="Решение:", value=f"{solution}")
            await ctx.send(embed=embed)

        if isinstance(error, commands.CommandNotFound):
            await own_command_error_message(
                "Команда не найдена!",
                "Используйте существующую команду,\nкоторая есть в списке `.help`",
            )
        elif isinstance(error, commands.DisabledCommand):
            await own_command_error_message(
                "Команда отключена!",
                "Используйте другую, активированную\n в данный момент команду",
            )
        elif isinstance(error, commands.CommandOnCooldown):

            def make_readable(seconds):
                hours, seconds = divmod(seconds, 60 ** 2)
                minutes, seconds = divmod(seconds, 60)
                return "{:02}ч : {:02}м : {:02}с".format(
                    round(hours), round(minutes), round(seconds)
                )

            await own_command_error_message(
                "Команда с задержкой!",
                f"Используйте данную команду \nпосле `{make_readable(error.retry_after)}` ⏳",
            )
        elif isinstance(error, commands.MissingPermissions):

            await own_command_error_message(
                    "У Вас недостаточно прав!",
                    "Получите следующие права:\n" + "\n".join(error.missing_perms)
            )

        elif isinstance(error, commands.MissingRequiredArgument):

            await own_command_error_message(
                    "Вы упустили аргументы при\nиспользовании команды!",
                    f"Запишите команду по синтаксису:\n`{PREFIX}{ctx.command.usage}`"
            )
def setup(bot):
    bot.add_cog(Errors(bot))
