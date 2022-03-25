import asyncio
from puppet import Puppet
from invitation import Invitation
from users_ids_dispenser import UserIdsDispenser
from database import MongoDb
class Puppeteer:
    _puppets = []
    _tokens = ["OTA2OTQ1MjY2OTg3NDQyMjU4.YYgA6A.-tpmrLIlOoUKoi5bdDFzt22sj1Q"]
    _invites = ["https://discord.gg/wcThUS46", "https://discord.gg/wotblitzru"]
    _invitation = Invitation()
    _target_users = UserIdsDispenser()
    _data = MongoDb()

    def start_puppet(self, token: str):
        puppet = Puppet(token, data = self._data, target_users = self._target_users, invitation=self._invitation)
        asyncio.ensure_future(puppet.start())
        self._puppets.append(puppet)
        for invite in self._invites:
            asyncio.ensure_future(puppet.join_to_guild(invite))

    async def start(self):
        for token in self._tokens:
            self.start_puppet(token)