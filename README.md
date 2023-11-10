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

print(help(SafoneAPI.logo))
```

For more checkout [API Playground](https://api.safone.dev/docs) or [Read Docs](https://api.safone.dev/redoc).

## List of APIs

- ASQ
- Advice
- Astronomy
- AI Chatbot
- Apps Search
- Anime Search
- Anime News (MAL)
- Anime Pics (SFW & NSFW)
- Bard AI Chatbot
- Bin Info Search
- Bing Image Search
- Bing Image Creator
- CC Generator
- Carbon Imager
- ChatGPT Chatbot
- Character Search
- Covid Info Search
- Currency Converter
- Country Info Search
- Code Executor (Piston)
- DALL-E Image Creator
- Figlet Generator
- Fake Info Generator
- Google Search
- Github Search
- Global News (BBC)
- Grammarly Checker
- Google Translator
- Google Image Search
- IMDb Search
- Ip Fraud Checker
- Internet Acronyms
- Image Background Remover
- LLama-2 AI
- Logo Maker
- Lyrics Search
- Manga Search
- Morse Code Encoder
- Morse Code Decoder
- Note Writer
- NSFW Detector
- Npm Package Search
- OCR/ Text Reader
- Paraphraser Tool
- Proxy Finder (HTTP)
- PyPi Package Search
- Quotly Sticker
- QR Code Generator
- Reddit Search
- Rayso Imager
- Random Memes
- Random Facts
- Random Jokes
- Random Bully
- Random Quote
- Spell Checker
- Spam Detector
- Special Pastebin
- Stripe Key Checker
- Song Finder (Shazam)
- Short Link Bypasser
- Short Link Generator
- Stackoverflow Search
- Spotify Song Search
- TMDb Search
- Torrent Search
- Truth or Dare Game
- Telegraph Pasting
- Telegraph File Uploader
- Telegram Sticker Search
- Ubuntu Search
- Unsplash Search
- Udemy Course Finder
- Urban Dictionary Search
- Word Dictionary Search
- Wallpaper Search
- Wikipedia Search
- Website Screenshot
- Weather Informatiom
- Xda-developer Search
- YouTube Video Search
- YouTube Playlist Search

## Note

1. I'll add more features soon.
2. If you're stuck somewhere, [AsmSupport](https://t.me/AsmSupport) are there to help.
