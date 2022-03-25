import time
import asyncio
from threading import Thread
from bot import SelfBot

def main():
    bot = SelfBot(token = "mfa.0QnLbg53wjxNg5tmKlEqcGAMxQD_YdKOSrAKlFXsrGx4HiYuwJpZU8p7vYk7z3HyNyx04CK7gF_xzsmt9YBe"  )
    bot.run()

if __name__ == '__main__':
    main()