"""
Команда для заповнення бази демо-даними.
Запуск: python manage.py seed_menu
"""
from django.core.management.base import BaseCommand
from menu.models import Category, Dish


class Command(BaseCommand):
    help = 'Заповнює базу даних демонстраційним меню ресторану'

    def handle(self, *args, **options):
        categories_data = [
            {
                'name': 'Перші страви',
                'order': 1,
                'dishes': [
                    ('Мінестроне', 'Овочевий суп з пастою та пармезаном', 120),
                    ('Крем-суп з гарбуза', 'З трюфельною олією та грінками', 110),
                ]
            },
            {
                'name': 'Основні страви',
                'order': 2,
                'dishes': [
                    ('Паста Карбонара', 'Бекон, яйце, пармезан, чорний перець', 185),
                    ('Різотто з грибами', 'Білі гриби, пармезан, трюфельна олія', 210),
                    ('Піца Маргарита', 'Томатний соус, моцарела, базилік', 220),
                    ('Лазанья Болоньєзе', 'Класична лазанья з м\'ясним соусом', 195),
                ]
            },
            {
                'name': 'Десерти',
                'order': 3,
                'dishes': [
                    ('Тірамісу', 'Класичний італійський десерт', 145),
                    ('Панна-кота', 'З ягідним соусом', 130),
                ]
            },
            {
                'name': 'Напої',
                'order': 4,
                'dishes': [
                    ('Espresso', 'Класична еспресо', 55),
                    ('Домашній лимонад', 'Свіжий лимонад з м\'ятою', 85),
                ]
            },
        ]

        for cat_data in categories_data:
            category, created = Category.objects.get_or_create(
                name=cat_data['name'],
                defaults={'order': cat_data['order']}
            )
            for name, description, price in cat_data['dishes']:
                Dish.objects.get_or_create(
                    category=category,
                    name=name,
                    defaults={'description': description, 'price': price}
                )

        self.stdout.write(self.style.SUCCESS('Меню успішно заповнено демо-даними!'))
