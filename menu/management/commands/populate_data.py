from django.core.management.base import BaseCommand
from menu.models import Category, Dish, Booking
from datetime import datetime

class Command(BaseCommand):
    def handle(self, *args, **options):
        if not Category.objects.exists():
            first = Category.objects.create(name='Перші страви', order=1)
            main = Category.objects.create(name='Основні страви', order=2)
            dessert = Category.objects.create(name='Десерти', order=3)
            beverages = Category.objects.create(name='Напої', order=4)

            first.dishes.create(
                name='Мінестроне',
                description='Овочевий суп з пастою та пармезаном',
                price=120,
                image='media/dishes/minestrone.jpg',
                is_available=True,
                order=1
            )
            first.dishes.create(
                name='Крем-суп з гарбуза',
                description='З трюфельною олією та грінками',
                price=110,
                image='dishes/Крем-суп_з_гарбуза.jpg',
                is_available=True,
                order=2
            )

            main.dishes.create(
                name='Паста Карбонара',
                description='Бекон, яйце, пармезан, чорний перець',
                price=185,
                image='dishes/Паста_Карбонара.png',
                is_available=True,
                order=1
            )
            main.dishes.create(
                name='Різотто з грибами',
                description='Білі гриби, пармезан, трюфельна олія',
                price=210,
                image='dishes/Різотто_з_грибами.jpg',
                is_available=True,
                order=2
            )
            main.dishes.create(
                name='Піца Маргарита',
                description='Томатний соус, моцарела, базилік',
                price=220,
                image='dishes/Піца_Маргарита.webp',
                is_available=True,
                order=3
            )
            main.dishes.create(
                name='Лазанья Болоньєзе',
                description="Класична лазанья з м'ясним соусом",
                price=195,
                image='dishes/Лазанья_Болоньєзе.webp',
                is_available=True,
                order=4
            )

            dessert.dishes.create(
                name='Тірамісу',
                description='Класичний італійський десерт',
                price=145,
                image='media/dishes/Тірамісу.jpg',
                is_available=True,
                order=1
            )
            dessert.dishes.create(
                name='Панна-кота',
                description='З ягідним соусом',
                price=130,
                image='media/dishes/Панна-кота.jpg',
                is_available=True,
                order=2
            )

            beverages.dishes.create(
                name='Espresso',
                description='Класична еспресо',
                price=55,
                image='media/dishes/Espresso.webp',
                is_available=True,
                order=1
            )
            beverages.dishes.create(
                name='Домашній лимонад',
                description="Свіжий лимонад з м'ятою",
                price=85,
                image='dishes/Домашній_лимонад.jpg',
                is_available=True,
                order=2
            )

            Booking.objects.create(
                name='Max',
                phone='+38(098)454-2064',
                guests=2,
                date='2026-06-18',
                time='17:00:00',
                comment='',
                is_confirmed=False
            )

            self.stdout.write('Всі дані додані!')
        else:
            self.stdout.write('Дані вже існують')