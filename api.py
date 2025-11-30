from flask import Flask, send_file, jsonify, render_template, send_from_directory
import os
import random
from pathlib import Path

app = Flask(__name__)

# Путь к папке с картинками
IMAGES_DIR = Path("images")

# --- ГЛАВНАЯ СТРАНИЦА (HTML Галерея) ---
@app.route("/")
def index():
    """
    Главная страница - HTML галерея
    """
    return render_template("index.html")

# --- API ENDPOINTS ---

@app.route("/api/info")
def api_info():
    """
    Информация об API
    """
    return jsonify({
        "message": "Teto Gallery API",
        "endpoints": {
            "/": "HTML галерея",
            "/api/info": "Информация об API",
            "/api/random": "Случайное изображение",
            "/api/images": "Список всех изображений"
        }
    })

@app.route("/api/random")
def get_random_image():
    """
    Возвращает случайную картинку
    """
    images = list(IMAGES_DIR.glob("*"))
    images = [img for img in images if img.suffix.lower() in ['.jpg', '.jpeg', '.png']]
    
    if not images:
        return jsonify({"error": "Нет картинок"}), 404
    
    random_image = random.choice(images)
    return send_file(random_image, mimetype='image/jpeg')

@app.route("/api/images")
def list_images():
    """
    Список всех изображений (JSON)
    """
    images = list(IMAGES_DIR.glob("*"))
    images = [img for img in images if img.suffix.lower() in ['.jpg', '.jpeg', '.png']]
    
    return jsonify({
        "total": len(images),
        "images": [img.name for img in sorted(images)]
    })

@app.route("/images/<filename>")
def serve_image(filename):
    """
    Отдаёт конкретную картинку по имени
    Используется для галереи
    """
    return send_from_directory(IMAGES_DIR, filename)

# Запуск сервера
if __name__ == "__main__":
    # Создаём папки если их нет
    Path("templates").mkdir(exist_ok=True)
    Path("static").mkdir(exist_ok=True)
    
    print("🚀 Teto Gallery запущена!")
    print("📱 Главная страница: http://localhost:8000")
    print("🔌 API: http://localhost:8000/api/info")
    app.run(host="0.0.0.0", port=8000, debug=True)
