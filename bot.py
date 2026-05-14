from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import requests
import logging

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


BOT_TOKEN = "8438003289:AAFJErZSd7hz3gzStG4tUSGVPEPXR682AWw"

# URL API 
API_URL = "http://localhost:8000/api/random"


# --- Команда /start ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Приветствие при запуске бота
    """
    welcome_text = (
        "Привет! Я бот с артами Касанэ Тето!\n\n"
        "Команды:\n"
        "/teto - получить случайный арт Тето\n"
        "/stats - статистика галереи\n"
        "/help - помощь"
    )
    await update.message.reply_text(welcome_text)


# --- Команда /teto (главная!) ---
async def send_teto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    
    try:
        # Показываем что бот "работает"
        await update.message.chat.send_action(action="upload_photo")
        
        # Делаем запрос к нашему API
        logger.info(f"Запрос картинки от {update.effective_user.first_name}")
        response = requests.get(API_URL, timeout=10)
        
        # Проверяем что запрос успешен
        if response.status_code == 200:
            # Отправляем картинку
            await update.message.reply_photo(
                photo=response.content,
                caption=" Тето! | Powered by Teto Gallery"
            )
            logger.info("Картинка отправлена!")
        else:
            await update.message.reply_text(
                f"Ошибка API: статус {response.status_code}\n"
                f"Проверь что Flask сервер запущен!"
            )
            
    except requests.exceptions.ConnectionError:
        # Если API недоступен
        logger.error("Не могу подключиться к API")
        await update.message.reply_text(
            "Не могу подключиться к API.\n\n"
            "Убедись что Flask сервер запущен:\n"
            "```\n"
            "cd ~/teto-project\n"
            "source venv/bin/activate\n"
            "python api.py\n"
            "```",
            parse_mode="Markdown"
        )
    except requests.exceptions.Timeout:
        # Если API не отвечает
        logger.error("Timeout при запросе к API")
        await update.message.reply_text(
            "API слишком долго отвечает.\n"
            "Попробуй ещё раз через несколько секунд."
        )
    except Exception as e:
        # Любая другая ошибка
        logger.error(f"Неожиданная ошибка: {e}")
        await update.message.reply_text(
            f"Произошла ошибка: {e}"
        )


# --- Команда /stats ---
async def stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Показывает статистику галереи
    """
    
    try:
        # Запрашиваем информацию о картинках
        response = requests.get("http://localhost:8000/api/images", timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            stats_text = (
                f"Статистика галереи:\n\n"
                f"Всего изображений: {data['total']}\n"
                f"Веб-галерея: https://zachary-nonpunctual-nimbly.ngrok-free.dev/\n"
                f"API: http://localhost:8000/api/info"
            )
            await update.message.reply_text(stats_text)
        else:
            await update.message.reply_text("Не могу получить статистику")
            
    except Exception as e:
        await update.message.reply_text(f"Ошибка: {e}")


# --- Команда /help ---
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Справка по командам
    """
    help_text = (
        "Справка по командам:\n\n"
        "/start - начало работы\n"
        "/teto - случайный арт Тето \n"
        "/stats - статистика галереи \n"
        "/help - эта справка\n\n"
        "Просто пиши /teto чтобы получать арты!"
    )
    await update.message.reply_text(help_text)


# --- Обработчик неизвестных команд ---
async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Реагирует на неизвестные команды
    """
    await update.message.reply_text(
        " Не знаю такой команды.\n"
        "Попробуй /help чтобы увидеть список команд."
    )


# --- Главная функция ---
def main():
    """
    Запуск бота
    """
    
    logger.info("Запускаю Teto Bot...")
    
    # Проверяем токен
    if BOT_TOKEN == "":
        logger.error("ОШИБКА: Не указан токен бота!")
        logger.error("Открой bot.py и замени BOT_TOKEN на свой токен от @BotFather")
        return
    
    # Создаём приложение
    application = Application.builder().token(BOT_TOKEN).build()
    
    # Регистрируем обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("teto", send_teto))
    application.add_handler(CommandHandler("stats", stats))
    application.add_handler(CommandHandler("help", help_command))
    
    # Обработчик неизвестных команд (должен быть последним)
    from telegram.ext import MessageHandler, filters
    application.add_handler(MessageHandler(filters.COMMAND, unknown))
    
    # Запускаем бота
    logger.info("Бот запущен! Нажми Ctrl+C для остановки.")
    logger.info("Найди бота в Telegram и напиши /start")
    
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
