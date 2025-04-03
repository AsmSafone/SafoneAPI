# SafoneAPI

### Asynchronous Python Wrapper For SafoneAPI

[![Python](http://forthebadge.com/images/badges/made-with-python.svg)](https://python.org)
[![GitHub](https://forthebadge.com/images/badges/built-by-developers.svg)](https://github.com/)

[![Issues](https://img.shields.io/github/issues/AsmSafone/SafoneAPI?style=for-the-badge&color=orange)](https://github.com/AsmSafone/SafoneAPI/issues)
[![Forks](https://img.shields.io/github/forks/AsmSafone/SafoneAPI?style=for-the-badge&color=orange)](https://github.com/AsmSafone/SafoneAPI/fork)
[![Stars](https://img.shields.io/github/stars/AsmSafone/SafoneAPI?style=for-the-badge&color=orange)](https://github.com/AsmSafone/SafoneAPI)
[![LICENSE](https://img.shields.io/github/license/AsmSafone/SafoneAPI?color=orange&style=for-the-badge)](https://github.com/AsmSafone/SafoneAPI)
[![Contributors](https://img.shields.io/github/contributors/AsmSafone/SafoneAPI?style=for-the-badge&color=orange)](https://github.com/AsmSafone/SafoneAPI)


## 📦 Installation

```sh
pip install safoneapi
```

## 🚀 Quick Start

Here's a simple example to get you started:

```python
import asyncio
from SafoneAPI import SafoneAPI

async def main():
    api = SafoneAPI()
    resp = await api.github("AsmSafone")
    print(resp.results)

asyncio.run(main())
```

## 📖 Documentation

For detailed documentation:

1. Use Python's built-in help:
```python
from SafoneAPI import SafoneAPI
print(help(SafoneAPI.logo))
```

2. Visit our online resources:
- [API Playground](https://api.safone.co/docs)
- [Read the Docs](https://api.safone.co/redoc)

## 🛠️ Available APIs

- AI Chatbot
- Advice
- Anime News (MAL)
- Anime Pics (SFW & NSFW)
- Anime Search
- Apps Search
- ASQ
- Astronomy
- Background Remover
- Bard AI Chatbot
- Bin Info Search
- Bing Image Search
- Carbon Generator
- CC Generator
- Character Search
- ChatGPT Chatbot
- Code Executor (Piston)
- Country Info Search
- Covid Info Search
- Currency Converter
- Fake Info Generator
- Figlet Generator
- Github Search
- Global News (BBC)
- Google Image Search
- Google Search
- Google Translator
- Grammarly Checker
- Image Generator (SFW & NSFW)
- Image Recognition
- IMDb Movie Search
- Internet Acronyms
- Ip Fraud Checker
- LLama-2 AI Chatbot
- Logo Maker
- Lyrics Search
- Manga Search
- Morse Code Decoder
- Morse Code Encoder
- Note Writer
- Npm Package Search
- NSFW Detector
- OCR/Text Scanner
- Paraphraser Tool
- Proxy Finder (HTTP)
- PyPi Package Search
- QR Code Generator
- Quotly Sticker
- Random Bully
- Random Excuses
- Random Facts
- Random Insult
- Random Jokes
- Random Memes
- Random Motivation
- Random Quote
- Random Riddle
- Rayso Generator
- Reddit Search
- Short Link Bypasser
- Short Link Generator
- Song Finder (Shazam)
- Spam Detector
- Special Pastebin
- Spell Checker
- Spotify Song Search
- Stackoverflow Search
- Stripe Key Checker
- Subtitle Search
- Telegraph File Uploader
- Telegraph Pasting
- Telegram Sticker Search
- TMDb Search
- Torrent Search
- TradingView TA
- Truth or Dare Game
- Ubuntu Search
- Udemy Course Coupon Finder
- Unsplash Image Search
- Urban Dictionary Search
- Voice/Speech Generator
- Wallpaper Search
- Weather Information
- Website Screenshot
- Wikipedia Search
- Xda-developer Search
- YouTube Playlist Search
- YouTube Video Search

## 💬 Support

Need help? Reach out to us:
- Join our [Telegram Support Group](https://t.me/AsmSupport)
- Open an [Issue](https://github.com/AsmSafone/SafoneAPI/issues)

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
