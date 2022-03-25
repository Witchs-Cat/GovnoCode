import sys
import asyncio
import discord
from discord.ext import commands
from discord.utils import get


def check_prefix(bot, msg):
    user_id = bot.user.id
    base = ["."] #сюды префиксы
    return base


initial_extensions = [
    "modules.poni",
]

class SelfBot(commands.AutoShardedBot):
    
    def __init__(self, token = None, loop = None):
        super().__init__(command_prefix=check_prefix, self_bot = True, loop = loop)
        self.token = token

        for extension in initial_extensions:
            try:
                self.load_extension(extension)
            except Exception as e:
                print(f'Не удалось добавить модуль {extension}.', file=sys.stderr)
                print(e)


    async def on_ready(self):
        channel = self.get_channel(507148096099319808)
        embed = discord.Embed(
            colour = discord.Colour.from_rgb(255, 165, 0),
            description= f"""🗂 Набор в клан [WinRAR[W-R]](https://clck.ru/XvmYU).
```
🔴 Требования для вступления:
🔻54%+ побед;
🔻1400+ среднего урона по аккаунту;
🔻5к+ боев;
```"""
        )
        await channel.send(embed = embed)

    async def on_message(self,message):
        ctx = await self.get_context(message)
        if ctx.command == None:
            return
        await self.process_commands(message)

    def run(self):
        if self.token is None:
            print("Токен отсутсвует")
            return
        super().run(self.token,reconnect=True, bot = False)
