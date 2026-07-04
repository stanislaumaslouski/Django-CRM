import sys
import os
from pathlib import Path

# Добавляем путь к проекту
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))

# Устанавливаем настройки Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

# Импортируем WSGI приложение
from backend.wsgi import application

# Vercel ожидает функцию handler
handler = application
