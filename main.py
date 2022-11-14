import telegram_bot_fronted.main
import asyncio
import os

async def django_excute():
    path = os.getcwd() + "\little_archemy_backend"
    os.chdir(path)
    os.system("py manage.py runserver")
    pass

async def bot_execute():
    telegram_bot_fronted.main.recive_message
    pass


async def dual_execute():
    await asyncio.gather(django_excute(),bot_execute())

       
asyncio.run(dual_execute())