import asyncio
import discord
from discord.ext import commands

class Puppet(commands.Bot):
    def __init__(self, token:str, data, target_users, invitation):
        super().__init__(command_prefix = None, self_bot = True)
        self.loop_is_run = False
        self.token = token
        self._data = data
        self._target_users = target_users
        self._invitation = invitation

    
    async def on_ready(self):
        print(f"logined as {self.user}")

    async def on_message(self, message):
        user = message.author

        if user.bot:
            return
        if user.id == self.user.id:
            return
        if await self._target_users.any(user.id):
            return
        if self._data.invited_users.any(user.id):
            return
        if self._data.ignored_users.any(user.id):
            return

        try:
            profile = await user.profile()
        except:
            return
        else:
            guild_ids = [guild.id for guild in profile.mutual_guilds]
            if self._data.ignored_guilds.any_common(guild_ids):
                return
        
        await self._target_users.add(user.id)
        print(f"{user} добавлен в очерель.")

    async def _spam_loop(self): 
        while self.loop_is_run:
            was_attempt_to_send = False
            try:
                user_id = await self._target_users.next()
                if user_id == None:
                    continue

                user = await self.fetch_user(user_id)
                if user == None:
                    continue

                was_attempt_to_send = True
                text = self._invitation.text
                emb = self._invitation.embed
                await user.send(text, embed = emb)
                self._data.invited_users.add(user.id)
            except Exception as e:
                print(f"error: {e}")

            finally:
                sleep_time = 65 if was_attempt_to_send else 5
                await asyncio.sleep(sleep_time)

    async def join_to_guild(self, url):
        if not self.is_ready():
            await self.wait_for("ready")
        invite = await self.fetch_invite(url)
        await invite.accept()

    async def start(self):
        self.loop_is_run = True
        await asyncio.gather(
            self._spam_loop(),
            super().start(self.token, reconnect = True, bot = False)
        )