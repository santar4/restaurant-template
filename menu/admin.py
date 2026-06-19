from django.contrib import admin
from .models import Category, Dish, Booking

from django.contrib import admin
from .models import Dish, Category, Booking


class DishInline(admin.TabularInline):
    """Показує страви прямо всередині категорії — зручно для клієнта"""
    model = Dish
    extra = 1
    fields = ['name', 'price', 'image', 'is_available', 'order']
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj and obj.image:
            return f'<img src="{obj.image.url}" width="80" style="object-fit: cover;" />'
        return '📷 Немає фото'

    image_preview.allow_tags = True
    image_preview.short_description = 'Фото'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'order', 'dish_count']
    search_fields = ['name']
    inlines = [DishInline]

    def dish_count(self, obj):
        return obj.dishes.count()

    dish_count.short_description = 'Кількість страв'


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'is_available', 'image_preview']
    list_filter = ['category', 'is_available']
    search_fields = ['name', 'description']
    list_editable = ['price', 'is_available']
    list_per_page = 20

    # Додаємо попередній перегляд фото у списку
    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" width="80" height="80" style="object-fit: cover;" />'
        return '📷 Немає фото'

    image_preview.allow_tags = True
    image_preview.short_description = 'Фото'

    # Групуємо поля для зручності
    fieldsets = (
        ('Основна інформація', {
            'fields': ('category', 'name', 'description', 'price')
        }),
        ('Медіа', {
            'fields': ('image',),
            'classes': ('wide',)
        }),
        ('Налаштування', {
            'fields': ('is_available', 'order'),
            'classes': ('collapse',)
        })
    )


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'date', 'time', 'guests', 'is_confirmed', 'created_at']
    list_filter = ['is_confirmed', 'date']
    list_editable = ['is_confirmed']
    search_fields = ['name', 'phone', 'email']
    ordering = ['-created_at']
    date_hierarchy = 'date'

    # Додаткові дії для масового підтвердження
    actions = ['confirm_bookings']

    def confirm_bookings(self, request, queryset):
        updated = queryset.update(is_confirmed=True)
        self.message_user(request, f'Підтверджено {updated} бронювань.')

    confirm_bookings.short_description = 'Підтвердити вибрані бронювання'