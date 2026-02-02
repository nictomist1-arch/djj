# add_product_images.py
import os
import django
from django.core.files import File

# Настройка Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from products.models import Product


def assign_images_to_products():
    """Присваивает изображения товарам по ключевым словам"""

    # Словарь соответствия ключевых слов и файлов
    image_mapping = {
        'macbook': 'images.jpg',
        'asus': 'images.jpg',
        'lenovo': 'images.jpg',
        'ноутбук': 'images.jpg',
        'iphone': 'phone.jpg',
        'samsung': 'phone.jpg',
        'pixel': 'phone.jpg',
        'смартфон': 'phone.jpg',
        'sony': 'headphones.jpg',
        'airpods': 'headphones.jpg',
        'наушники': 'headphones.jpg',
    }

    # Папка с изображениями
    images_dir = 'media/products'

    products = Product.objects.all()
    updated_count = 0

    for product in products:
        product_name_lower = product.name.lower()

        # Ищем подходящее изображение
        for keyword, filename in image_mapping.items():
            if keyword in product_name_lower:
                image_path = os.path.join(images_dir, filename)

                if os.path.exists(image_path):
                    # Удаляем старое изображение, если есть
                    if product.image:
                        product.image.delete(save=False)

                    # Загружаем новое
                    with open(image_path, 'rb') as f:
                        product.image.save(filename, File(f), save=True)

                    print(f"✅ {product.name} → {filename}")
                    updated_count += 1
                    break
        else:
            print(f"⚠️  Не найдено изображение для: {product.name}")

    print(f"\n📊 Итого: {updated_count} из {len(products)} товаров обновлено")


if __name__ == '__main__':
    assign_images_to_products()