import random
import aiohttp
import asyncio
from bs4 import BeautifulSoup
import json

CATEGORIES = [
    "https://habr.com/ru/hubs/programming/",
    "https://habr.com/ru/hubs/python/"
]

with open("proxy.txt") as file:
    PROXY_LIST = "".join(file.readlines()).split("\n")

async def send_request(url, rand_proxy) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url, proxy=f"http://{rand_proxy}") as resp:
            return await resp.text(encoding="utf-8")

async def parse_category(category_url, rand_proxy):
    html_response = await send_request(url=category_url, rand_proxy=rand_proxy)
    soup = BeautifulSoup(html_response, "lxml")
    pagination_block = soup.find("")