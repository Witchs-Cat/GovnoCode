from asyncio import Lock

class UserIdsDispenser:
    _queue = []
    _all = []
    _lock = Lock()

    async def add(self, user_id:int):
        async with self._lock:
            if not user_id in self._all:
                self._queue.append(user_id)
                self._all.append(user_id)


    async def next(self):
        async with self._lock:
            if len(self._queue) == 0:
                return None

            return self._queue.pop(0)
        
    async def any(self, _id):
        async with self._lock:
            return _id in self._all

    def __len__(self):
        return len(self._queue)