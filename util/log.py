import datetime
import os

import aiohttp
from discord import Webhook


async def info(msg: str):
    async with aiohttp.ClientSession() as session:
        await Webhook.from_url(os.getenv("WEBHOOK_URL"), session=session,).send(
            f'`{datetime.datetime.now().strftime("[%Y/%m/%d, %H:%M:%S]")} [info] {msg}`',
            username="INFO",
            avatar_url="https://us.123rf.com/450wm/igormalovic/igormalovic1801/igormalovic180100098/"
            "93521399-wooden-log-cartoon-illustration-isolated-on-white.jpg?ver=6",
        )


async def err(msg: str):
    async with aiohttp.ClientSession() as session:
        await Webhook.from_url(os.getenv("WEBHOOK_URL"), session=session,).send(
            f'`{datetime.datetime.now().strftime("[%Y/%m/%d, %H:%M:%S]")} [error] {msg}`',
            username="ERROR",
            avatar_url="https://us.123rf.com/450wm/igormalovic/igormalovic1801/igormalovic180100098/"
            "93521399-wooden-log-cartoon-illustration-isolated-on-white.jpg?ver=6",
        )
