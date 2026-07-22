from django.core.management.base import BaseCommand
from menu.models import Category, Dish


class Command(BaseCommand):
    def handle(self, *args, **options):
        if not Category.objects.exists():
            Category.objects.create(name='Перші страви', order=1)
            Category.objects.create(name='Основні страви', order=2)
            Category.objects.create(name='Десерти', order=3)

            Category.objects.get(name='Перші страви').dishes.create(
                name='Мінестроне',
                description='Овощевий суп з пастою та пармезаном',
                price=120.00,
                image='media/dishes/minestrone.jpg',
                is_available=True,
                order=1
            )

            self.stdout.write('Дані додані!')
        else:
            self.stdout.write('Дані вже існують')