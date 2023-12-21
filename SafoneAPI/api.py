"""
SafoneAPI v1.0
Copyright (c) 2023 AsmSafone

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
from dotmap import DotMap
from base64 import b64decode
from typing import Union, List
from pyrogram.types import Message, User

from .errors import (
    TimeoutError,
    InvalidContent,
    InvalidRequest,
    GenericApiError,
    ConnectionError,
    RateLimitExceeded,
)
from aiohttp.client_exceptions import (
    ContentTypeError,
    ClientConnectorError,
)


class SafoneAPI:
    """
    SafoneAPI class to access all the endpoints
    Documentation: https://api.safone.dev/docs
    Support Group: https://t.me/AsmSupport
    Updates Channel: https://t.me/AsmSafone

    """

    def __init__(self, api: str = None, session: aiohttp.ClientSession = None):
        self.api = api or "https://api.safone.dev/"
        self.session = session or aiohttp.ClientSession

    def _get_name(self, user: User) -> str:
        return f"{user.first_name} {user.last_name or ''}".rstrip()

    def _get_fname(self, type: str, count: int = 0) -> str:
        return f"{str(round(time.time()))}_{count}.{type}".rstrip()

    def _decode_image(self, image: str, type: str, index: int) -> BytesIO:
        img_bytes = BytesIO(b64decode(image.encode("utf-8")))
        img_bytes.name = self._get_fname(type.split("/")[1], index)
        return img_bytes

    def _parse_result(self, response: dict) -> Union[DotMap, List[BytesIO]]:
        type = response.get("type")
        error = response.get("error")
        response = DotMap(response)
        if not error:
            response.success = True
        if type and "/" in type:
            if isinstance(response.image, list):
                response = [
                    self._decode_image(image, type, idx)
                    for idx, image in enumerate(response.image)
                ]
            else:
                response = self._decode_image(response.image, type, 0)
        return response

    async def _fetch(self, route, timeout=60, **params):
        try:
            async with self.session() as client:
                resp = await client.get(self.api + route, params=params, timeout=timeout)
                if resp.status == 429:
                    raise RateLimitExceeded
                elif resp.status in (502, 503):
                    raise ConnectionError
                response = await resp.json()
                if resp.status == 400:
                    raise InvalidRequest(response.get("docs"))
                elif resp.status == 422:
                    raise GenericApiError(response.get("error"))
        except asyncio.TimeoutError:
            raise TimeoutError
        except ContentTypeError:
            raise InvalidContent
        except ClientConnectorError:
            raise ConnectionError
        return self._parse_result(response)

    async def _post_data(self, route, data, timeout=60):
        try:
            async with self.session() as client:
                resp = await client.post(self.api + route, data=data, timeout=timeout)
                if resp.status == 429:
                    raise RateLimitExceeded
                elif resp.status in (502, 503):
                    raise ConnectionError
                response = await resp.json()
                if resp.status == 400:
                    raise InvalidRequest(response.get("docs"))
                elif resp.status == 422:
                    raise GenericApiError(response.get("error"))
        except asyncio.TimeoutError:
            raise TimeoutError
        except ContentTypeError:
            raise InvalidContent
        except ClientConnectorError:
            raise ConnectionError
        return self._parse_result(response)

    async def _post_json(self, route, json, timeout=60):
        try:
            async with self.session() as client:
                resp = await client.post(self.api + route, json=json, timeout=timeout)
                if resp.status == 429:
                    raise RateLimitExceeded
                elif resp.status in (502, 503):
                    raise ConnectionError
                response = await resp.json()
                if resp.status == 400:
                    raise InvalidRequest(response.get("docs"))
                elif resp.status == 422:
                    raise GenericApiError(response.get("error"))
        except asyncio.TimeoutError:
            raise TimeoutError
        except ContentTypeError:
            raise InvalidContent
        except ClientConnectorError:
            raise ConnectionError
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
                        Result object (BytesIO): Results which you can access with filename

        """
        return await self._fetch("meme")

    async def asq(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to ask
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("asq", query=query)

    async def llama(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to ask to llama
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("llama", query=query)

    async def shazam(self, file: str):
        """
        Returns An Object.

                Parameters:
                        file (str): File path of song
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        async with aiofiles.open(file, mode="rb") as f:
            file = await f.read()
        return await self._post_data("shazam", data={"media": file})

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
                        Result object (BytesIO): Results which you can access with filename

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

    async def morse(self, text: str, type: str):
        """
        Returns An Object.

                Parameters:
                        text (str): Text to convert
                        type (str): Type of conversion (encode/decode)
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("morse/" + type, text=text)

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

    async def imagine(self, text: str, limit: int = 1, version: int = 1):
        """
        Returns An Object.

                Parameters:
                        text (str): Describe in text
                        limit (int): Limit the results [OPTIONAL]
                        version (int): Version of imagine [OPTIONAL]
                Returns:
                        Result object (List[BytesIO]): Results which you can access with filename

        """
        return await self._fetch("imagine", text=text, limit=limit, version=version)

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

    async def rayso(self, code: str, title: str = "", theme: str = None, dark_mode: bool = False):
        """
        Returns An Object.

                Parameters:
                       code (str): Rayso content
                       title (str): Rayso title [OPTIONAL]
                       theme (str): Rayso theme name [OPTIONAL]
                       dark_mode (bool): Whether dark mode [OPTIONAL]
                Returns:
                        Result object (BytesIO): Results which you can access with filename

        """
        json = dict(
                code=code,
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

    async def bininfo(self, bin: int):
        """
        Returns An Object.

                Parameters:
                        bin (int): Bin to search
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("bininfo", bin=bin)

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

    async def fakeinfo(self, country: str = ""):
        """
        Returns An Object.

                Parameters:
                        country (str): Country code or iso [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("fakeinfo", country=country)

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
                        origin (str): Origin of currency
                        target (str): Targeted currency to convert
                        amount (int): Amount of currency to convert
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("currency", origin=origin, target=target, amount=amount)

    async def spam_scan(self, message: Union[Message, str]):
        """
        Returns An Object.

                Parameters:
                        message (Union[Message, str]): Message to process
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        if isinstance(message, Message):
            message = message.text or message.caption or ""

        if not message:
            raise InvalidRequest("Please provide a text or ~pyrogram.types.Message")

        json = dict(message=message)
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

    async def removebg(self, url: str = None, file: str = None):
        """
        Returns An Object.

                Parameters:
                        url (str): URL to scan [OPTIONAL]
                        file (str): File path of an image to scan [OPTIONAL]
                Returns:
                        Result object (BytesIO): Results which you can access with filename

        """
        if not file and not url:
            raise InvalidRequest("Please provide a file path or URL")

        if not file:
            return await self._fetch("removebg", image=url)

        async with aiofiles.open(file, mode="rb") as f:
            file = await f.read()
        return await self._post_data("removebg", data={"image": file})

    async def proxy(self, type: str, country: str = "all", limit: int = 10):
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

    async def imdb(self, query: str = "", limit: int = 10, imdb_id: str = None):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                        limit (int): Limit the results [OPTIONAL]
                        imdb_id (str): Specific IMDb ID [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        if not query and not imdb_id:
            raise InvalidRequest("Please provide a query or IMDb ID")

        return await self._fetch("imdb", query=query, limit=limit, imdb_id=imdb_id)

    async def tmdb(self, query: str = "", limit: int = 10, tmdb_id: int = 0):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                        limit (int): Limit the results [OPTIONAL]
                        tmdb_id (int): Specific TMDb ID [OPTIONAL]
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

    async def ccgen(self, bins: List[Union[str, int]], limit: int = 10):
        """
        Returns An Object.

                Parameters:
                        bins (List[Union[str, int]]): List of bins
                        limit (int): Limit the number of cards [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        if isinstance(bins, list):
            bins = ",".join(map(str, bins))

        return await self._fetch("ccgen", bins=bins, limit=limit)

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

    async def paraphrase(self, text: str):
        """
        Returns An Object.

                Parameters:
                        text (str): Some text
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        json = dict(text=text)
        return await self._post_json("paraphrase", json=json)

    async def grammarly(self, text: str):
        """
        Returns An Object.

                Parameters:
                        text (str): Some text
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        json = dict(text=text)
        return await self._post_json("grammarly", json=json)

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

    async def spotify(self, query: str, limit: int = 10):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                        limit (int): Limit the results [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("spotify", query=query, limit=limit)

    async def translate(self, text: str, source: str = "auto", target: str = "en"):
        """
        Returns An Object.

                Parameters:
                        text (str): Text to translate
                        source (str): Language code of source language [OPTIONAL]
                        target (str): Language code of target language [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        json = dict(
                text=text,
                source=source,
                target=target,
            )
        return await self._post_json("translate", json=json)

    async def bard(self, message: Union[Message, str], dialog_messages: list = []):
        """
        Returns An Object.

                Parameters:
                        message (Union[Message, str]): ~pyrogram.types.Message or text
                        dialog_messages (list): List of chat messages as dict(user, bot) [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation
    
            """
        formated_messages = []

        if isinstance(message, Message):
            if message.command:
                message = " ".join(message.command[1:])
            elif message.text:
                message = message.text.strip()
            elif message.caption:
                message = message.caption.strip()

        for dialog_message in dialog_messages:
            if (
                isinstance(dialog_message, Message)
                and dialog_message.from_user and dialog_message.text
            ):
                k = "bot" if dialog_message.from_user.is_bot else "user"
                formated_messages.append({k: dialog_message.text.strip()})
            elif isinstance(dialog_message, dict):
                formated_messages.append(dialog_message)

        if not message:
            raise InvalidRequest("Please provide a text or ~pyrogram.types.Message")

        json = dict(
                message=message,
                dialog_messages=formated_messages,
            )
        return await self._post_json("bard", json=json)

    async def paste(self, content: str, title: str = None, language: str = None, ephemeral: bool = False):
        """
        Returns An Object.

                Parameters:
                        content (str): Text content to paste
                        title (str): Title of the page [OPTIONAL]
                        language (str): Language for highlight [OPTIONAL]
                        ephemeral (bool): Whether one-time view [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        json = dict(
                content=content,
                title=title,
                language=language,
                ephemeral=ephemeral,
            )
        return await self._post_json("paste", json=json)

    async def write(self, text: str, page: str = None, font: str = None, color: str = "black"):
        """
        Returns An Object.

                Parameters:
                        text (str): Text to write
                        page (str): Page name [OPTIONAL]
                        font (str): Font name [OPTIONAL]
                        color (str): Color of text [OPTIONAL]
                Returns:
                        Result object (List[BytesIO]): Results which you can access with filename

        """
        json = dict(
                text=text,
                page=page,
                font=font,
                color=color,
            )
        return await self._post_json("write", json=json)

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

    async def logo(self, text: str, color: str = "", keyword: str = "", limit: int = 10, version: int = 1):
        """
        Returns An Object.

                Parameters:
                        text (str): Text to make logo
                        color (str): Logo text color [OPTIONAL]
                        keyword (str): Logo keywords [OPTIONAL]
                        limit (int): Limit the results [OPTIONAL]
                        version (int): Version of logo [OPTIONAL]
                Returns:
                        Result object (BytesIO): Results which you can access with filename

        """
        return await self._fetch("logo", text=text, color=color, keyword=keyword, limit=limit, version=version)

    async def webshot(self, url: str, width: int = 1920, height: int = 1080, delay: float = 0.1, full: bool = False):
        """
        Returns An Object.

                Parameters:
                        url (str): The website url with http
                        width (int): Width of webshot [OPTIONAL]
                        height (int): Height of webshot [OPTIONAL]
                        delay (float): Delay in seconds [OPTIONAL]
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
                delay=delay,
                full=full,
            )
        return await self._post_json("webshot", json=json)

    async def chatgpt(self, message: Union[Message, str], chat_mode: str = None, dialog_messages: list = [], version: int = 3):
        """
        Returns An Object.

                Parameters:
                        message (Union[Message, str]): ~pyrogram.types.Message or text
                        chat_mode (str): Modes like 'assistant', 'code_assistant' etc [OPTIONAL]
                        dialog_messages (list): List of chat messages as dict(user, bot) [OPTIONAL]
                        version (int): The GPT model version (3 = gpt-3.5 and 4 = gpt-4) [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        formated_messages = []

        if isinstance(message, Message):
            if message.command:
                message = " ".join(message.command[1:])
            elif message.text:
                message = message.text.strip()
            elif message.caption:
                message = message.caption.strip()

        for dialog_message in dialog_messages:
            if (
                isinstance(dialog_message, Message)
                and dialog_message.from_user and dialog_message.text
            ):
                k = "bot" if dialog_message.from_user.is_bot else "user"
                formated_messages.append({k: dialog_message.text.strip()})
            elif isinstance(dialog_message, dict):
                formated_messages.append(dialog_message)

        if not message:
            raise InvalidRequest("Please provide a text or ~pyrogram.types.Message")

        json = dict(
                message=message,
                version=version,
                chat_mode=chat_mode,
                dialog_messages=formated_messages,
            )
        return await self._post_json("chatgpt", json=json)

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
