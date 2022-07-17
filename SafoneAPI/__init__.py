import aiohttp
import aiofiles
from io import BytesIO
from typing import List
from dotmap import DotMap
from pyrogram.types import Message, User
from asyncio.exceptions import TimeoutError


__version__ = "1.0.1"
__author__ = "AsmSafone"


class SafoneAPI:
    """
    SafoneAPI class to access all the endpoints of api

    """

    def __init__(self) -> None:
        self.api = "https://api.safone.tech/"
        self.session = aiohttp.ClientSession

    def _get_name(self, user: User) -> str:
        return f"{user.first_name} {user.last_name or ''}".rstrip()

    def _get_file(self, data, filename) -> BytesIO:
        try:
            file = BytesIO(data)
            file.name = filename
        except Exception:
            raise
        return file

    async def _fetch(self, route, timeout=30, filename=None, **params):
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
        except TimeoutError:
            raise Exception("Failed to communicate with the server.")
        if filename is not None:
            return self._get_file(await resp.read(), filename)
        return DotMap(await resp.json())

    async def _post_data(self, route, data, timeout=30, filename=None):
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
        except TimeoutError:
            raise Exception("Failed to communicate with the server.")
        if filename is not None:
            return self._get_file(await resp.read(), filename)
        return DotMap(await resp.json())

    async def _post_json(self, route, json, timeout=30, filename=None):
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
        except TimeoutError:
            raise Exception("Failed to communicate with the server.")
        if filename is not None:
            return self._get_file(await resp.read(), filename)
        return DotMap(await resp.json())

    async def advice(self):
        """
        Returns An Object.

                Returns:
                        result object (str): Results which you can access with dot notation

        """
        return await self._fetch("advice")

    async def bully(self):
        """
        Returns An Object.

                Returns:
                        result object (str): Results which you can access with dot notation

        """
        return await self._fetch("bully")

    async def fact(self):
        """
        Returns An Object.

                Returns:
                        result object (str): Results which you can access with dot notation

        """
        return await self._fetch("fact")

    async def joke(self):
        """
        Returns An Object.

                Returns:
                        result object (str): Results which you can access with dot notation

        """
        return await self._fetch("joke")

    async def meme(self):
        """
        Returns An Object.

                Returns:
                        result object (str): Results which you can access with dot notation

        """
        return await self._fetch("meme", filename="meme.png")

    async def quote(self):
        """
        Returns An Object.

                Returns:
                        result object (str): Results which you can access with dot notation

        """
        return await self._fetch("quote")

    async def truth(self):
        """
        Returns An Object.

                Returns:
                        result object (str): Results which you can access with dot notation

        """
        return await self._fetch("truth")

    async def dare(self):
        """
        Returns An Object.

                Returns:
                        result object (str): Results which you can access with dot notation

        """
        return await self._fetch("dare")

    async def aninews(self):
        """
        Returns An Object.

                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("anime/news")

    async def apps(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("apps", query=query)

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

    async def npm(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("npm", query=query)

    async def logo(self, text: str):
        """
        Returns An Object.

                Parameters:
                        text (str): Text to make logo
                Returns:
                        Result object (BytesIO): Results which you can access with filename

        """
        return await self._fetch("logo", text=text, filename="logo.png")

    async def write(self, text: str):
        """
        Returns An Object.

                Parameters:
                        text (str): Text to make logo
                Returns:
                        Result object (BytesIO): Results which you can access with filename

        """
        return await self._fetch("write", text=text, filename="write.png")

    async def google(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("google", query=query)

    async def youtube(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("youtube", query=query)

    async def playlist(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("playlist", query=query)

    async def wall(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("wall", query=query)

    async def news(self, category: str = "all"):
        """
        Returns An Object.

                Parameters:
                        category (str): News category [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("news", category=category)

    async def reddit(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("reddit", query=query)

    async def urban(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("urban", query=query)

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

        return await self._post_json("carbon", json=kwargs, filename="carbon.png")

    async def chatbot(self, query: str, user_id: int = 0):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to compute
                        user_id (int): Unique user_id. [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation
        """
        return await self._fetch("chatbot", query=query, user_id=user_id)

    async def lyrics(self, title: str):
        """
        Returns An Object.

                Parameters:
                        title (str): Title of the song
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("lyrics", title=title)

    async def wiki(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("wiki", query=query)

    async def ipinfo(self, ip: str):
        """
        Returns An Object.

                Parameters:
                        ip (str): Query to search
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("ipinfo", ip=ip)

    async def covidinfo(self, country: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("covidinfo", country=country)

    async def countryinfo(self, country: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("countryinfo", country=country)

    async def fakeinfo(self, gender: str = "male"):
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

    async def spam_scan(self, text: list):
        """
        Returns An Object.
                Parameters:
                        text (str): Text to process.
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        if not isinstance(text, list):
            text = [text]

        json = dict(text=text)
        return await self._post_json("spam", json=json)

    async def nsfw_scan(self, url: str = None, file: str = None):
        """
        Returns An Object.

                Parameters:
                        url (str): URL to scan (Optional)
                        file (str): File path of an image to scan. (Optional)
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        if not file and not url:
            raise Exception("Please provide a file or url")
        if not file:
            return await self._fetch("nsfw", image=url)
        async with aiofiles.open(file, mode="rb") as f:
            file = await f.read()
        return await self._post_data("nsfw", data={"image": file})

    async def proxy(self, type: str):
        """
        Returns An Object.

                Parameters:
                        type (str): Type of proxy, one of: http, socks4, socks5
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("proxy/" + type)

    async def tmdb(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("tmdb", query=query)

    async def quotly(self, messages: List[Message]):
        """
        Returns An Object.

                Parameters:
                        messages ([Message]): Generate quotly stickers.
                Returns:
                        Result object (BytesIO): Results which you can access with filename

        """
        if not isinstance(messages, list):
            messages = [messages]

        payload = {
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
                        "type": message.chat.type,
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
                        "type": message.chat.type,
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
        return await self._post_json("quotly", json=payload, filename="sticker.webp")

    async def translate(self, text: str, target: str = "en"):
        """
        Returns An Object.

                Parameters:
                        text (str): Text to translate
                        target (str): Language code of target language [OPTIONAL]
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("translate", text=text, target=target)

    async def pypi(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Exact package name
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("pypi", query=query)

    async def image(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("image", query=query)

    async def qrcode(self, text: str):
        """
        Returns An Object.

                Parameters:
                        text (str): Some text
                Returns:
                        Result object (BytesIO): Results which you can access with filename

        """
        return await self._fetch("qrcode", text=text, filename="qrcode.png")

    async def shortlink(self, url: str):
        """
        Returns An Object.

                Parameters:
                        url (str): Long url
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("shortlink", url=url)

    async def spellcheck(self, text: str):
        """
        Returns An Object.

                Parameters:
                        text (str): Some text
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("spellcheck", text=text)

    async def tgsticker(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("tgsticker", query=query)

    async def torrent(self, query: str):
        """
        Returns An Object.

                Parameters:
                        query (str): Query to search
                Returns:
                        Result object (str): Results which you can access with dot notation

        """
        return await self._fetch("torrent", query=query)

    async def webshot(self, url: str, width: int = 720, height: int = 1280, full: bool = False):
        """
        Returns An Object.
                Parameters:
                    url (str): The website url with http.
                    width (int)[optional]: Width of webshot.
                    height (int)[optional]: Height of webshot.
                    full (bool)[optional]: Whether capture full page.
                Returns:
                        Result object (BytesIO): Results which you can access with filename

        """
        if not url.startswith("http"):
            url = "http://" + url

        json = dict(
                url=url,
                width=width,
                height=height,
                format="jpeg",
                full=full,
                scale=1,
            )
        return await self._post_json("webshot", json=json, filename="webshot.png")

    async def spotify(self, user: str = None, email: str = None, pswd: str = None):
        """
        Returns An Object.
                Parameters:
                    user (str)[optional]: New account username.
                    email (int)[optional]: New account email.
                    pswd (int)[optional]: New account password.
                Returns:
                        Result object (BytesIO): Results which you can access with filename

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
                    language (str)[optional]: Programming language.
                    code (str)[optional]: Code to execute.
                    stdin (str)[optional]: STDIN for the code.
                    args (list)[optional]: arguments to pass in cli.
                Returns:
                    Result object:
                        result.stdout, result.stdout `if language is passed`,
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


class InvalidRequest(Exception):
    pass

class GenericApiError(Exception):
    pass
