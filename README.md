#  Teto Gallery — Kasane Teto Art Collection

> A full-stack web gallery and Telegram bot for browsing Kasane Teto (重音テト) artwork.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-3.0-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## About

This project was built to practice full-stack development and server infrastructure.  
It consists of three components working together:

- **Web gallery** — browse 40 artworks in the browser
- **REST API** — Flask backend serving images as JSON
- **Telegram bot** — get a random artwork with `/teto` command

The main goal was to learn:
- Python web development
- REST API design with Flask
- Telegram Bot API
- Nginx as a static file server
- Docker containerization
- Frontend-to-backend communication

## Tech Stack

**Backend:**
- Python 3.12
- Flask (REST API)
- python-telegram-bot

**Frontend:**
- HTML5 / CSS3 / Vanilla JavaScript
- Responsive design, modal viewer, CSS grid

**Infrastructure:**
- Nginx (static file server)
- Docker
- ngrok (local tunnel for bot webhook)

## Project Structure

```
Teto_telegrambot/
├── api.py              # Flask REST API
├── bot.py              # Telegram bot
├── templates/          # HTML/CSS/JS (frontend)
├── images/             # Artwork files
├── download.sh         # Image downloader script
├── download_more.sh    # Extended downloader
└── requirements.txt
```

## Getting Started

### Requirements
- Python 3.12+
- Telegram Bot Token

### Installation

```bash
git clone https://github.com/Yonory/Teto_telegrambot.git
cd Teto_telegrambot

python3 -m venv venv
source venv/bin/activate   # Linux/Mac
pip install -r requirements.txt
```

### Download images (optional)

```bash
chmod +x download.sh
./download.sh
```

### Run Flask API

```bash
python api.py
```

API available at: `http://localhost:8000`

### Run Telegram Bot

```bash
# Set your bot token in bot.py
python bot.py
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/images` | List all images |
| GET | `/images/random` | Get random image |

## Telegram Bot Commands

| Command | Description |
|---------|-------------|
| `/start` | Welcome message |
| `/teto` | Get a random Kasane Teto artwork |

## What I Learned

- How Telegram bots work with webhook and polling
- How to build and serve a REST API with Flask
- How Nginx serves static files
- How Docker containerizes a Python application
- Frontend and backend communication via fetch API
- Git and GitHub workflow

## License

This project is created for educational purposes.
