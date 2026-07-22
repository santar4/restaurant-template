from django.core.management.base import BaseCommand
from menu.models import Category, Dish


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = {
            "Перші страви": Category.objects.get_or_create(
                name="Перші страви",
                defaults={"order": 1},
            )[0],
            "Основні страви": Category.objects.get_or_create(
                name="Основні страви",
                defaults={"order": 2},
            )[0],
            "Десерти": Category.objects.get_or_create(
                name="Десерти",
                defaults={"order": 3},
            )[0],
            "Напої": Category.objects.get_or_create(
                name="Напої",
                defaults={"order": 4},
            )[0],
        }

        dishes = [
            {
                "category": "Перші страви",
                "name": "Мінестроне",
                "description": "Овочевий суп з пастою та пармезаном",
                "price": 120,
                "image": "dishes/minestrone.jpg",
                "order": 1,
            },
            {
                "category": "Перші страви",
                "name": "Крем-суп з гарбуза",
                "description": "З трюфельною олією та грінками",
                "price": 110,
                "image": "dishes/Крем-суп_з_гарбуза.jpg",
                "order": 2,
            },
            {
                "category": "Основні страви",
                "name": "Паста Карбонара",
                "description": "Бекон, яйце, пармезан, чорний перець",
                "price": 185,
                "image": "dishes/Паста_Карбонара.png",
                "order": 1,
            },
            {
                "category": "Основні страви",
                "name": "Різотто з грибами",
                "description": "Білі гриби, пармезан, трюфельна олія",
                "price": 210,
                "image": "dishes/Різотто_з_грибами.jpg",
                "order": 2,
            },
            {
                "category": "Основні страви",
                "name": "Піца Маргарита",
                "description": "Томатний соус, моцарела, базилік",
                "price": 220,
                "image": "dishes/Піца_Маргарита.webp",
                "order": 3,
            },
            {
                "category": "Основні страви",
                "name": "Лазанья Болоньєзе",
                "description": "Класична лазанья з м'ясним соусом",
                "price": 195,
                "image": "dishes/Лазанья_Болоньєзе.webp",
                "order": 4,
            },
            {
                "category": "Десерти",
                "name": "Тірамісу",
                "description": "Класичний італійський десерт",
                "price": 145,
                "image": "dishes/Тірамісу.jpg",
                "order": 1,
            },
            {
                "category": "Десерти",
                "name": "Панна-кота",
                "description": "З ягідним соусом",
                "price": 130,
                "image": "dishes/Панна-кота.jpg",
                "order": 2,
            },
            {
                "category": "Напої",
                "name": "Espresso",
                "description": "Класичне еспресо",
                "price": 55,
                "image": "dishes/Espresso.webp",
                "order": 1,
            },
            {
                "category": "Напої",
                "name": "Домашній лимонад",
                "description": "Свіжий лимонад з м'ятою",
                "price": 85,
                "image": "dishes/Домашній_лимонад.jpg",
                "order": 2,
            },
        ]

        for dish in dishes:
            Dish.objects.get_or_create(
                name=dish["name"],
                defaults={
                    "category": categories[dish["category"]],
                    "description": dish["description"],
                    "price": dish["price"],
                    "image": dish["image"],
                    "is_available": True,
                    "order": dish["order"],
                },
            )

        self.stdout.write(self.style.SUCCESS("Дані успішно перевірені та додані!"))