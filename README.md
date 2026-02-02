# 🛒 Django Shop - Интернет-магазин на Django

![Django](https://img.shields.io/badge/Django-4.2+-092E20?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5.1-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)

Современный интернет-магазин на Django с темной темой и адаптивным дизайном.

## ✨ Особенности

- 🎨 **Темная тема** - современный дизайн с фиолетовыми акцентами
- 📱 **Полностью адаптивный** - оптимизирован для всех устройств
- 🛒 **Корзина покупок** - с подсчетом товаров и общей суммы
- 👤 **Система аутентификации** - регистрация, вход, выход
- 📂 **Категории товаров** - удобная навигация по продуктам
- 🔍 **Детальные страницы товаров** - с сохранением оригинальных изображений
- ⚡ **Оптимизированная производительность** - быстрая загрузка страниц
- 🎭 **Плавные анимации** - улучшенный пользовательский опыт

## 🚀 Быстрый старт

### Предварительные требования

- Python 3.8 или выше
- Django 4.2 или выше
- pip (менеджер пакетов Python)

### Установка

1. **Клонируйте репозиторий**
```bash
git clone https://github.com/your-username/django-shop.git
cd django-shop

    Создайте виртуальное окружение

bash

python -m venv venv
source venv/bin/activate  # Для Linux/Mac
# или
venv\Scripts\activate     # Для Windows

    Установите зависимости

bash

pip install -r requirements.txt

    Настройте базу данных

bash

python manage.py migrate

    Создайте суперпользователя

bash

python manage.py createsuperuser

    Запустите сервер разработки

bash

python manage.py runserver

    Откройте в браузере

text

http://127.0.0.1:8000/

📁 Структура проекта
text

django-shop/
├── manage.py
├── requirements.txt
├── README.md
├── shop/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── products/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── products/
│           ├── product_list.html
│           └── product_detail.html
├── cart/
│   ├── __init__.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── context_processors.py
│   └── templates/
│       └── cart/
│           └── cart_detail.html
├── accounts/
│   ├── __init__.py
│   ├── apps.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
│       └── registration/
│           ├── login.html
│           └── register.html
└── templates/
    └── base.html

🎨 Дизайн и CSS
Цветовая палитра

    Основной фиолетовый: #8a2be2

    Вторичный фиолетовый: #9d4edd

    Акцентный красный: #ff6b6b

    Фон карточек: #1e1e1e

    Основной фон: #0a0a0a

Особенности дизайна

    Градиенты для навигации и кнопок

    Многослойные тени для глубины

    Современные скругления углов (12px)

    Плавные анимации при наведении

    Черный фон для изображений

🛠 Технологии
Backend

    Django - основной веб-фреймворк

    Django ORM - работа с базой данных

    Сессии Django - управление корзиной

Frontend

    Bootstrap 5.1 - CSS-фреймворк

    Bootstrap Icons - векторные иконки

    Кастомный CSS - темная тема и анимации

    JavaScript - интерактивность

📦 Модели данных
Product (продукт)
python

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название")
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    image = models.ImageField(upload_to='products/%Y/%m/%d/', verbose_name="Изображение")
    available = models.BooleanField(default=True, verbose_name="Доступен")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

Category (категория)
python

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    slug = models.SlugField(max_length=100, unique=True)
    
    def get_absolute_url(self):
        return reverse('products_by_category', args=[self.slug])

Cart (корзина)
python

class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)

🔧 Настройка
requirements.txt
text

Django>=4.2
Pillow>=10.0.0

Конфигурация settings.py
python

# Настройки приложений
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'products',
    'cart',
    'accounts',
]

# Настройки медиа файлов
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Контекстные процессоры
TEMPLATES = [
    {
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
                'products.context_processors.categories',
            ],
        },
    },
]
