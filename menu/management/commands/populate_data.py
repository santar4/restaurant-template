from django.core.management.base import BaseCommand
from menu.models import Category, Dish


class Command(BaseCommand):
    def handle(self, *args, **options):

        first, _ = Category.objects.get_or_create(
            name="Перші страви",
            defaults={"order": 1},
        )

        second, _ = Category.objects.get_or_create(
            name="Основні страви",
            defaults={"order": 2},
        )

        third, _ = Category.objects.get_or_create(
            name="Десерти",
            defaults={"order": 3},
        )

        Dish.objects.get_or_create(
            name="Мінестроне",
            defaults={
                "category": first,
                "description": "Овощевий суп з пастою та пармезаном",
                "price": 120,
                "image": "dishes/minestrone.jpg",
                "is_available": True,
                "order": 1,
            },
        )

        self.stdout.write(self.style.SUCCESS("Дані успішно перевірені"))