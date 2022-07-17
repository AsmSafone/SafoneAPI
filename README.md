# SafoneAPI

Asynchronous Python Wrapper For SafoneAPI

[![Python](http://forthebadge.com/images/badges/made-with-python.svg)](https://python.org)
[![GitHub](https://forthebadge.com/images/badges/built-by-developers.svg)](https://github.com/)

## Requirements

- Python 3.8 or newer.

## Installation

```sh
$ pip install safoneapi
```

## Usage

For Example, to search on google, you can do this

```py
import asyncio
from SafoneAPI import SafoneAPI


async def main():
    api = SafoneAPI()
    resp = await api.google("AsmSafone")
    print(resp.results)


asyncio.run(main())
```

## List of APIs

- AI Chatbot
- Apps Search
- Anime (SFW & NSFW)
- Code Executor (Piston)
- Spam Detector
- NSFW Detector
- Quotly Sticker
- Carbon Imager
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
- Google Translator
- Reddit Search
- Currency Converter
- Internet Acronyms
- Urban Dictionary Search
- Fake Info Generator
- Info Searcher
- Image Search
- Logo Maker
- Proxy Finder
- TMDb Search
- Lyrics Search
- Npm Package Search
- PyPi Package Search
- QR Code Generator
- Spotify Account Creator
- Telegram Sticker Search
- Short Link Generator
- Torrent Search
- Truth or Dare
- Udemy Discount Course
- Wallpaper Search
- Wikipedia Search
- YouTube Search
- Playlist Search
- Webshot Screenshot

## Note

1. I'll add more features soon.
2. If you're stuck somewhere, [AsmSupport](https://t.me/AsmSupport) are there to help.