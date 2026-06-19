from django.db import models


class Category(models.Model):
    """Категорія меню: Перші страви, Основні страви, Десерти, Напої"""
    name = models.CharField('Назва категорії', max_length=100)
    order = models.PositiveIntegerField('Порядок показу', default=0)

    class Meta:
        verbose_name = 'Категорія меню'
        verbose_name_plural = 'Категорії меню'
        ordering = ['order']

    def __str__(self):
        return self.name


class Dish(models.Model):
    """Страва в меню"""
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE,
        related_name='dishes', verbose_name='Категорія'
    )
    name = models.CharField('Назва страви', max_length=200)
    description = models.TextField('Опис', blank=True)
    price = models.DecimalField('Ціна (грн)', max_digits=8, decimal_places=2)
    image = models.ImageField(
        'Фото страви', upload_to='dishes/',
        blank=True, null=True
    )
    is_available = models.BooleanField('Доступно для замовлення', default=True)
    order = models.PositiveIntegerField('Порядок показу', default=0)

    class Meta:
        verbose_name = 'Страва'
        verbose_name_plural = 'Страви'
        ordering = ['category__order', 'order']

    def __str__(self):
        return self.name


class Booking(models.Model):
    """Заявка на бронювання столика"""
    name = models.CharField('Ім\'я', max_length=100)
    phone = models.CharField('Телефон', max_length=20)
    guests = models.PositiveIntegerField('Кількість гостей', default=2)
    date = models.DateField('Дата')
    time = models.TimeField('Час')
    comment = models.TextField('Коментар', blank=True)
    created_at = models.DateTimeField('Створено', auto_now_add=True)
    is_confirmed = models.BooleanField('Підтверджено', default=False)

    class Meta:
        verbose_name = 'Бронювання'
        verbose_name_plural = 'Бронювання'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.name} — {self.date} {self.time}'
