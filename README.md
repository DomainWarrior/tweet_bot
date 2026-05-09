# tweet_bot

> Python Twitter automation bot — auto-tweet, auto-follow, auto-retweet, and more.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python)
![Tweepy](https://img.shields.io/badge/Tweepy-API-1DA1F2?style=flat-square&logo=twitter)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

> **Note:** Built against Twitter API v1.1. Twitter deprecated free v1.1 access in 2023 — a Twitter developer account with Elevated or Basic access is now required.

---

## Features

- Auto-tweet on a timer
- Auto-follow back followers
- Tweet from a text file (skips duplicates)
- Auto favorite & retweet by hashtag
- Auto-reply when mentioned

---

## Setup

### 1. Get API credentials

Create an app at [developer.twitter.com](https://developer.twitter.com) and copy your keys.

### 2. Configure environment

```bash
cp .env.example .env
# Fill in your Twitter keys in .env
```

### 3. Install & run

```bash
pip install tweepy python-dotenv
python main.py
```

---

## Project structure

| File | Purpose |
|------|---------|
| `credentials.py` | Loads API keys from env vars |
| `config.py` | Creates authenticated Tweepy API instance |
| `main.py` | Entry point |
| `autotweet.py` | Scheduled tweeting |
| `autoreply.py` | Mention auto-reply |
| `favretweet.py` | Auto like & retweet by hashtag |
| `followingfollowers.py` | Auto follow-back |
| `.env.example` | Credential template |

---

## License

MIT © [DomainWarrior](https://github.com/DomainWarrior)