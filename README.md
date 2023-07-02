# SafoneAPI

Asynchronous Python Wrapper For SafoneAPI

[![Python](http://forthebadge.com/images/badges/made-with-python.svg)](https://python.org)
[![GitHub](https://forthebadge.com/images/badges/built-by-developers.svg)](https://github.com/)

[![Issues](https://img.shields.io/github/issues/AsmSafone/SafoneAPI?style=for-the-badge&color=orange)](https://github.com/AsmSafone/SafoneAPI/issues)
[![Forks](https://img.shields.io/github/forks/AsmSafone/SafoneAPI?style=for-the-badge&color=orange)](https://github.com/AsmSafone/SafoneAPI/fork)
[![Stars](https://img.shields.io/github/stars/AsmSafone/SafoneAPI?style=for-the-badge&color=orange)](https://github.com/AsmSafone/SafoneAPI)
[![LICENSE](https://img.shields.io/github/license/AsmSafone/SafoneAPI?color=orange&style=for-the-badge)](https://github.com/AsmSafone/SafoneAPI)
[![Contributors](https://img.shields.io/github/contributors/AsmSafone/SafoneAPI?style=for-the-badge&color=orange)](https://github.com/AsmSafone/SafoneAPI)


## Installation

```sh
$ pip install safoneapi
```

## Usage

For Example, to search on github:

```py
import asyncio
from SafoneAPI import SafoneAPI


async def main():
    api = SafoneAPI()
    resp = await api.github("AsmSafone")
    print(resp.results)


asyncio.run(main())
```

## Documentation

There is no documentation as of now!
However, you can take help from the docstrings this way:

```py
from SafoneAPI import SafoneAPI

print(help(SafoneAPI.carbon))
```

For more checkout [API Playground](https://api.safone.me/docs) or [Read Docs](https://api.safone.me/redoc).

## List of APIs

- Advice
- Astronomy
- AI Chatbot
- Apps Search
- Anime Search
- Manga Search
- Character Search
- Anime Pics (SFW & NSFW)
- Code Executor (Piston)
- CC Generator
- ChatGPT Chatbot
- DALL-E Imaginator
- Spam Detector
- NSFW Detector
- Quotly Sticker
- Carbon Imager
- Rayso Imager
- Anime News
- Global News
- Note Writer
- Random Memes
- Random Facts
- Random Jokes
- Random Bully
- Random Quote
- Spell Checker
- Google Search
- Github Search
- Figlet Generator
- Google Translator
- Currency Converter
- Internet Acronyms
- Dictionary Search
- Urban Dictionary Search
- Fake Info Generator
- Ip Fraud Checker
- Bin Info Search
- Covid Info Search
- Country Info Search
- Image Search
- Reddit Search
- Logo Maker
- OCR Reader
- Proxy Finder
- TMDb Search
- Lyrics Search
- Npm Package Search
- PyPi Package Search
- QR Code Generator
- Question-Answering ASQ
- Spotify Account Creator
- Telegram Sticker Search
- Short Link Generator
- Short Link Bypasser
- Torrent Search
- Truth or Dare
- Udemy Course Finder
- Wallpaper Search
- Wikipedia Search
- Weather Info
- Ubuntu Search
- Unsplash Search
- YouTube Search
- Playlist Search
- Stripe Key Checker
- Stackoverflow Search
- Xda-developer Search
- Website Screenshot
- Special Pastebin
- Telegraph Pasting
- Telegraph File Uploader

## Note

1. I'll add more features soon.
2. If you're stuck somewhere, [AsmSupport](https://t.me/AsmSupport) are there to help.
