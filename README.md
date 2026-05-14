# Teto Gallery - Kasane Teto Art Collection

> Веб-галерея и Telegram бот для просмотра артов Касанэ Тето (重音テト)

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Flask](https://img.shields.io/badge/Flask-3.0-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

## О проекте

Teto Gallery - это full-stack проект, состоящий из:
-  **Веб-галереи** (HTML/CSS/JS) для просмотра артов в браузере
-  **REST API** (Flask) для управления изображениями
-  **Telegram бота** для получения случайных артов

## Возможности

- Просмотр галереи из 40 артов Касанэ Тето
- Получение случайного арта по кнопке
- Telegram бот с командой `/teto`
- REST API с JSON endpoints
- Адаптивный дизайн (работает на телефоне)
- Модальное окно для просмотра в полный размер

## Технологии

**Backend:**
- Python 3.12
- Flask (REST API)
- python-telegram-bot (Telegram Bot API)

**Frontend:**
- HTML5
- CSS3 (градиенты, анимации, grid layout)
- Vanilla JavaScript (fetch API)

**Data:**
- 40 изображений из Archive.org

### Требования

- Python 3.12+
- pip
- virtualenv

### Установка

1. **Клонируем репозиторий:**
```bash
git clone https://github.com/yonory/teto-project.git
cd teto-project
```

2. **Создаем виртуальное окружение:**
```bash
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# или
venv\Scripts\activate  # Windows
```

3. **Установка зависимости:**
```bash
pip install -r requirements.txt
```

4. **Скачиваем изображения (опционально):**
```bash
chmod +x download.sh
./download.sh
```

### Запуск

**1. Запускаем Flask API:**
```bash
source venv/bin/activate
python api.py
```

API будет доступен на: `http://localhost:8000`

# Добавлю остальную инструкцию позже
