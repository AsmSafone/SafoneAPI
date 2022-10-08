"""
SafoneAPI v1.0
Copyright (c) 2022 AsmSafone

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import time
import asyncio
import aiohttp
import aiofiles
from io import BytesIO
from typing import List
from dotmap import DotMap
from base64 import b64decode
from pyrogram.types import Message, User


class SafoneAPI:
    """
    SafoneAPI class to access all the endpoints of api

    """

    def __init__(self) -> None:
        self.api = "https://api.safone.tech/"
        self.session = aiohttp.ClientSession

    def _get_fn(self, type: str) -> str:
        return f"{str(round(time.time()))}.{type}".rstrip()

    def _get_name(self, user: User) -> str:
        return f"{user.first_name} {user.last_name or ''}".rstrip()

    def _parse_result(self, response):
        type = response.get("type")
        response = DotMap(response)
        if type and "/" in type:
            response = BytesIO(b64decode(response.image.encode("utf-8")))
            response.name = self._get_fn(type.split("/")[1])
        return response

    async def _fetch(self, route, timeout=30, **params):
        try:
            async with self.session() as client:
                resp = await client.get(self.api + route, params=params, timeout=timeout)
                if resp.status == 400:
                    raise InvalidRequest(
                        "Invalid Request, Please read docs: https://api.safone.tech/redoc"
                    )
                if resp.status == 422:
                    raise GenericApiError(
                        "Api Call Failed, Please report this: https://api.safone.tech/report"
                    )
                response = await resp.json()
        except asyncio.TimeoutError:
            raise TimeoutError(
                "Internal Server Timeout, Failed to communicate with api server"
            )
        except aiohttp.ContentTypeError:
            raise InvalidContent(
                "Invalid Content Type, Please report this: https://api.safone.tech/report"
            )
        return self._parse_result(response)

    async def _post_data(self, route, data, timeout=30):
        try:
            async with self.session() as client:
                resp = await client.post(self.api + route, data=data, timeout=timeout)
                if resp.status == 400:
                    raise InvalidRequest(
                        "Invalid Request, Please read docs: https://api.safone.tech/redoc"
                    )
                if resp.status == 422:
                    raise GenericApiError(
                        "Api Call Failed, Please report this: https://api.safone.tech/report"
                    )
                response = await resp.json()
        except asyncio.TimeoutError:
            raise TimeoutError(
                "Internal Server Timeout, Failed to communicate with api server"
            )
        except aiohttp.ContentTypeError:
            raise InvalidContent(
                "Invalid Content Type, Please report this: https://api.safone.tech/report"
            )
        return self._parse_result(response)

    async def _post_json(self, route, json, timeout=30):
        try:
            async with self.session() as client:
                resp = await client.post(self.api + route, json=json, timeout=timeout)
                if resp.status == 400:
                    raise InvalidRequest(
                        "Invalid Request, Please read docs: https://api.safone.tech/redoc"
                    )
                if resp.status == 422:
                    raise GenericApiError(
                        "Api Call Failed, Please report this: https://api.safone.tech/report"
                    )
                response = await resp.json()
        except asyncio.TimeoutError:
            raise TimeoutError(
                "Internal Server Timeout, Failed to communicate with api server"
            )
        except aiohttp.ContentTypeError:
            raise InvalidContent(
                "Invalid Content Type, Please report this: https://api.safone.tech/report"
            )
        return self._parse_result(response)

    async def advice(self):
        """
        Returns An Object.

                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("advice")

    async def astronomy(self):
        """
        Returns An Object.

                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("astronomy")

    async def bully(self):
        """
        Returns An Object.

                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("bully")

    async def fact(self):
        """
        Returns An Object.

                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("fact")

    async def joke(self):
        """
        Returns An Object.

                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("joke")

    async def meme(self):
        """
        Returns An Object.

                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("meme")

    async def quote(self, type: str = ""):
        """
        Returns An Object.

                Parameters:
                        type (str): Type of result (text/image) [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("quote", type=type)

    async def truth(self, category: str = ""):
        """
        Returns An Object.

                Parameters:
                        category (str): Truth category [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("truth", category=category)

    async def dare(self, category: str = ""):
        """
        Returns An Object.

                Parameters:
                        category (str): Dare category [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("dare", category=category)

    async def apps(self, query: str, limit: int = 10):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                        limit (int): Limit the results [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("apps", query=query, limit=limit)

    async def anime(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("anime/search", query=query)

    async def manga(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("anime/manga", query=query)

    async def character(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("anime/character", query=query)

    async def anime_news(self, limit: int = 10):
        """
        Returns An Object.

                Parameters:
                        limit (int): Limit the results [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("anime/news", limit=limit)

    async def anime_pics(self, type: str, nsfw: bool = False):
        """
        Returns An Object.

                Parameters:
                        type (str): Anime content type
                        nsfw (bool): Whether include nonsafe content [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with filename

        """
        if nsfw:
            return await self._fetch("anime/nsfw/" + type)
        return await self._fetch("anime/sfw/" + type)

    async def xda(self, query: str, limit: int = 10):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                        limit (int): Limit the results [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("xda", query=query, limit=limit)

    async def npm(self, query: str, limit: int = 10):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                        limit (int): Limit the results [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("npm", query=query, limit=limit)

    async def logo(self, text: str, color: str = ""):
        """
        Returns An Object.

                Parameters:
                        text (str): Text to make logo
                        color (str): Logo text color [OPTIONAL]
                Returns:
                        Result object (BytesIO): Results which you can access with filename

        """
        return await self._fetch("logo", text=text, color=color)

    async def write(self, text: str):
        """
        Returns An Object.

                Parameters:
                        text (str): Text to make logo
                Returns:
                        Result object (BytesIO): Results which you can access with filename

        """
        return await self._fetch("write", text=text)

    async def udemy(self, type: str, page: int = 1, limit: int = 10):
        """
        Returns An Object.

                Parameters:
                        type (str): Type of course
                        page (int): Page no to parse [OPTIONAL]
                        limit (int): Limit the results [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("udemy/" + type, page=page, limit=limit)

    async def ubuntu(self, query: str, limit: int = 10):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                        limit (int): Limit the results [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("ubuntu", query=query, limit=limit)

    async def google(self, query: str, limit: int = 10):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                        limit (int): Limit the results [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("google", query=query, limit=limit)

    async def github(self, query: str, limit: int = 10):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                        limit (int): Limit the results [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("github", query=query, limit=limit)

    async def youtube(self, query: str, limit: int = 10):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                        limit (int): Limit the results [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("youtube", query=query, limit=limit)

    async def playlist(self, query: str, limit: int = 10):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                        limit (int): Limit the results [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("playlist", query=query, limit=limit)

    async def wall(self, query: str, limit: int = 10):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                        limit (int): Limit the results [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("wall", query=query, limit=limit)

    async def news(self, category: str = "", limit: int = 10):
        """
        Returns An Object.

                Parameters:
                        category (str): News category [OPTIONAL]
                        limit (int): Limit the results [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("news", category=category, limit=limit)

    async def reddit(self, query: str, limit: int = 10, subreddit: list = [], nsfw: bool = False):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                        limit (int): Limit the results [OPTIONAL]
                        subreddit (list): Subreddits to include [OPTIONAL]
                        nsfw (bool): Whether include nonsafe content [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("reddit", query=query, limit=limit, subreddit=subreddit, nsfw=nsfw)

    async def urban(self, query: str, limit: int = 10):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                        limit (int): Limit the results [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("urban", query=query, limit=limit)

    async def unsplash(self, query: str, limit: int = 10):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                        limit (int): Limit the results [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("unsplash", query=query, limit=limit)

    async def weather(self, city: str, type: str = "text"):
        """
        Returns An Object.

                Parameters:
                        city (str): Name of the city
                        type (str): Type of result (text/image) [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("weather", city=city, type=type)

    async def dictionary(self, query: str, limit: int = 10):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                        limit (int): Limit the results [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("dictionary", query=query, limit=limit)

    async def carbon(self, code: str, **kwargs):
        """
        Returns An Object.

                Parameters:
                        code (str): Code to make carbon
                        kwagrs (dict): Extra args for styling
                Returns:
                        Result object (BytesIO): Results which you can access with filename

        """
        if "code" not in kwargs:
            kwargs["code"] = code

        return await self._post_json("carbon", json=kwargs)

    async def rayso(self, text: str, title: str = "", theme: str = None, dark_mode: bool = False):
        """
        Returns An Object.

                Parameters:
                       text (str): Rayso content or text
                       title (str): Rayso title [OPTIONAL]
                       theme (str): Rayso theme name [OPTIONAL]
                       dark_mode (bool): Whether dark mode [OPTIONAL]
                Returns:
                        Result object (BytesIO): Results which you can access with filename

        """
        json = dict(
                text=text,
                title=title,
                theme=theme,
                dark_mode=dark_mode,
            )
        return await self._post_json("rayso", json=json)

    async def chatbot(self, query: str, user_id: int = 0, bot_name: str = "", bot_master: str = ""):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to compute
                        user_id (int): Unique user_id [OPTIONAL]
                        bot_name (str): Your bot_name [OPTIONAL]
                        bot_master (str): Developer name [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation
        """
        return await self._fetch("chatbot", query=query, user_id=user_id, bot_name=bot_name, bot_master=bot_master)

    async def lyrics(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("lyrics", query=query)

    async def wiki(self, query: str, limit: int = 10):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                        limit (int): Limit the results [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("wiki", query=query, limit=limit)

    async def ipinfo(self, ip: str):
        """
        Returns An Object.

                Parameters:
                        ip (str): IP to search
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("ipinfo", ip=ip)

    async def covidinfo(self, country: str):
        """
        Returns An Object.

                Parameters:
                        country (str): Country name
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("covidinfo", country=country)

    async def countryinfo(self, country: str):
        """
        Returns An Object.

                Parameters:
                        country (str): Country name
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("countryinfo", country=country)

    async def fakeinfo(self, gender: str = ""):
        """
        Returns An Object.

                Parameters:
                        gender (str): Gender of person [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("fakeinfo", gender=gender)

    async def acronym(self, word: str):
        """
        Returns An Object.

                Parameters:
                        word (str): Word to search
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("acronym", word=word)

    async def currency(self, origin: str, target: str, amount: int):
        """
        Returns An Object.

                Parameters:
                        origin (str): origin of currency
                        target (str): targeted currency to convert
                        amount (int): amount of currency to convert
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("currency", origin=origin, target=target, amount=amount)

    async def spam_scan(self, text: str = None, message: Message = None):
        """
        Returns An Object.
                Parameters:
                        text (str): Text to process
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        if isinstance(message, Message):
            text = message.text or message.caption or ""
        if not text:
            raise InvalidRequest("Please provide a text or ~pyrogram.types.Message")

        json = dict(text=text)
        return await self._post_json("spam", json=json)

    async def nsfw_scan(self, url: str = None, file: str = None):
        """
        Returns An Object.

                Parameters:
                        url (str): URL to scan [OPTIONAL]
                        file (str): File path of an image to scan [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        if not file and not url:
            raise InvalidRequest("Please provide a file path or URL")
        if not file:
            return await self._fetch("nsfw", image=url)
        async with aiofiles.open(file, mode="rb") as f:
            file = await f.read()
        return await self._post_data("nsfw", data={"image": file})

    async def ocr_scan(self, url: str = None, file: str = None):
        """
        Returns An Object.

                Parameters:
                        url (str): URL to scan [OPTIONAL]
                        file (str): File path of an image to scan [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        if not file and not url:
            raise InvalidRequest("Please provide a file path or URL")
        if not file:
            return await self._fetch("ocr", image=url)
        async with aiofiles.open(file, mode="rb") as f:
            file = await f.read()
        return await self._post_data("ocr", data={"image": file})

    async def proxy(self, type: str, country: str = "", limit: int = 10):
        """
        Returns An Object.

                Parameters:
                        type (str): Type of proxy
                        country (str): Country code [OPTIONAL]
                        limit (int): Limit the results [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("proxy/" + type, country=country, limit=limit)

    async def tmdb(self, query: str = "", limit: int = 10, tmdb_id: int = 0):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                        limit (int): Limit the results [OPTIONAL]
                        tmdb_id (str): Specific TMDb ID [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        if not query and not tmdb_id:
            raise InvalidRequest("Please provide a query or TMDb ID")

        return await self._fetch("tmdb", query=query, limit=limit, tmdb_id=tmdb_id)

    async def quotly(self, messages: List[Message]):
        """
        Returns An Object.

                Parameters:
                        messages (List[Message]): List of ~pyrogram.types.Message
                Returns:
                        Result object (BytesIO): Results which you can access with filename

        """
        if not isinstance(messages, list):
            messages = [messages]

        json = {
            "type": "quote",
            "format": "webp",
            "backgroundColor": "#1b1429",
            "width": 512,
            "height": 768,
            "scale": 2,
            "messages": [
                {
                    "entities": [
                        {
                            "type": entity.type.name.lower(),
                            "offset": entity.offset,
                            "length": entity.length,
                        }
                        for entity in message.entities
                    ]
                    if message.entities
                    else [],
                    "chatId": message.forward_from.id
                    if message.forward_from
                    else message.from_user.id,
                    "avatar": True,
                    "from": {
                        "id": message.from_user.id,
                        "username": message.from_user.username
                        if message.from_user.username
                        else "",
                        "photo": {
                            "small_file_id": message.from_user.photo.small_file_id,
                            "small_photo_unique_id": message.from_user.photo.small_photo_unique_id,
                            "big_file_id": message.from_user.photo.big_file_id,
                            "big_photo_unique_id": message.from_user.photo.big_photo_unique_id,
                        }
                        if message.from_user.photo
                        else "",
                        "type": message.chat.type.name.lower(),
                        "name": self._get_name(message.from_user),
                    }
                    if not message.forward_from
                    else {
                        "id": message.forward_from.id,
                        "username": message.forward_from.username
                        if message.forward_from.username
                        else "",
                        "photo": {
                            "small_file_id": message.forward_from.photo.small_file_id,
                            "small_photo_unique_id": message.forward_from.photo.small_photo_unique_id,
                            "big_file_id": message.forward_from.photo.big_file_id,
                            "big_photo_unique_id": message.forward_from.photo.big_photo_unique_id,
                        }
                        if message.forward_from.photo
                        else "",
                        "type": message.chat.type.name.lower(),
                        "name": self._get_name(message.forward_from),
                    },
                    "text": message.text if message.text else "",
                    "replyMessage": (
                        {
                            "name": self._get_name(
                                message.reply_to_message.from_user
                            ),
                            "text": message.reply_to_message.text,
                            "chatId": message.reply_to_message.from_user.id,
                        }
                        if message.reply_to_message
                        else {}
                    )
                    if len(messages) == 1
                    else {},
                }
                for message in messages
            ],
        }
        return await self._post_json("quotly", json=json)

    async def translate(self, text: str, origin: str = "", target: str = "en"):
        """
        Returns An Object.

                Parameters:
                        text (str): Text to translate
                        origin (str): Language code of origin language [OPTIONAL]
                        target (str): Language code of target language [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("translate", text=text, origin=origin, target=target)

    async def figlet(self, text: str, font: str = ""):
        """
        Returns An Object.

                Parameters:
                        text (str): Some text
                        font (str): Font name [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("figlet", text=text, font=font)

    async def pypi(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Exact package name
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("pypi", query=query)

    async def image(self, query: str, limit: int = 10):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                        limit (int): Limit the results [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("image", query=query, limit=limit)

    async def qrcode(self, text: str):
        """
        Returns An Object.

                Parameters:
                        text (str): Some text
                Returns:
                        Result object (BytesIO): Results which you can access with filename

        """
        return await self._fetch("qrcode", text=text)

    async def shortlink(self, url: str, domain: str = ""):
        """
        Returns An Object.

                Parameters:
                        url (str): Long url
                        domain (str): Domain [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("shortlink", url=url, domain=domain)

    async def bypasslink(self, url: str, domain: str = ""):
        """
        Returns An Object.

                Parameters:
                        url (str): Short url
                        domain (str): Domain [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("bypasslink", url=url, domain=domain)

    async def skcheck(self, key: str):
        """
        Returns An Object.

                Parameters:
                        key (str): Stripe key
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("skcheck", key=key)

    async def spellcheck(self, text: str):
        """
        Returns An Object.

                Parameters:
                        text (str): Some text
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("spellcheck", text=text)

    async def tgsticker(self, query: str, limit: int = 10):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                        limit (int): Limit the results [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("tgsticker", query=query, limit=limit)

    async def torrent(self, query: str, limit: int = 10):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                        limit (int): Limit the results [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("torrent", query=query, limit=limit)

    async def stackoverflow(self, query: str, limit: int = 10):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                        limit (int): Limit the results [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("stackoverflow", query=query, limit=limit)

    async def webshot(self, url: str, width: int = 1920, height: int = 1080, full: bool = False):
        """
        Returns An Object.
                Parameters:
                    url (str): The website url with http
                    width (int): Width of webshot [OPTIONAL]
                    height (int): Height of webshot [OPTIONAL]
                    full (bool): Whether capture full page [OPTIONAL]
                Returns:
                        Result object (BytesIO): Results which you can access with filename

        """
        if not url.startswith("http"):
            url = "http://" + url

        json = dict(
                url=url,
                width=width,
                height=height,
                full=full,
            )
        return await self._post_json("webshot", json=json)

    async def paste(self, content: str, title: str = None, format: bool = False):
        """
        Returns An Object.
                Parameters:
                    content (str): Content to paste
                    title (str): Title of the page [OPTIONAL]
                    format (bool): Whether paste in code format [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """

        json = dict(
                content=content,
                title=title,
                code=format,
            )
        return await self._post_json("paste", json=json)

    async def spotify(self, user: str = None, email: str = None, pswd: str = None):
        """
        Returns An Object.
                Parameters:
                    user (str): New account username [OPTIONAL]
                    email (str): New account email [OPTIONAL]
                    pswd (str|int): New account password [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """

        json = dict(
                user=user,
                email=email,
                pswd=pswd,
            )
        return await self._post_json("spotify", json=json)

    async def execute(self, language: str = None, code: str = None, stdin: str = "", args: list = []):
        """
        Returns An Object.
                Parameters:
                    language (str): Programming language [OPTIONAL]
                    code (str): Code to execute [OPTIONAL]
                    stdin (str): STDIN for the code [OPTIONAL]
                    args (list): arguments to pass in cli [OPTIONAL]
                Returns:
                    Result object:
                        result.output, result.output `if language is passed`,
                        else a list of supported languages is returned
        """
        if not language:
            return await self._fetch("execute/languages")

        json = dict(
                language=language,
                code=code,
                stdin=stdin,
                args=args,
            )
        return await self._post_json("execute", json=json)

    async def telegraph(self, file: str = None, title: str = None, content: str = None, author_name: str = None, author_url: str = None):
        """
        Returns An Object.
                Parameters:
                    file (str): File path of a media [OPTIONAL]
                    title (str): Page title [OPTIONAL]
                    content (str): Page content [OPTIONAL]
                    author_name (str): Page author name [OPTIONAL]
                    author_url (str): Page author url [OPTIONAL]
                Returns:
                    Result object (str): Results which you can access with dot notation

        """
        if not file and not title:
            raise InvalidRequest("Please provide a file path or title")
        if not file:
            json = dict(
                title=title,
                content=content,
                author_name=author_name,
                author_url=author_url,
            )
            return await self._post_json("telegraph/text", json=json)
        async with aiofiles.open(file, mode="rb") as f:
            file = await f.read()
        return await self._post_data("telegraph/media", data={"media": file})


class InvalidRequest(Exception):
    """Incase request params is invalid"""
    pass

class InvalidContent(Exception):
    """Incase returned content is invalid"""
    pass

class GenericApiError(Exception):
    """Incase api returns validation error"""
    pass
