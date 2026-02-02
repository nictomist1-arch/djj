from .models import Category

def categories(request):
    """Добавляет все категории в контекст всех шаблонов"""
    return {
        'categories': Category.objects.all()
    }