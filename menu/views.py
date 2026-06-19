from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Category, Dish
from .forms import BookingForm


def home(request):
    """Головна сторінка з hero-банером"""
    featured_dishes = Dish.objects.filter(is_available=True)[:3]
    return render(request, 'menu/home.html', {
        'featured_dishes': featured_dishes
    })


def menu_list(request):
    """Сторінка меню, згруповане по категоріях"""
    categories = Category.objects.prefetch_related('dishes').all()
    return render(request, 'menu/menu_list.html', {
        'categories': categories
    })


def about(request):
    """Сторінка про ресторан"""
    return render(request, 'menu/about.html')


def contacts(request):
    """Контакти + форма бронювання столика"""
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                'Дякуємо! Вашу заявку на бронювання прийнято. Ми зв\'яжемося з вами найближчим часом.'
            )
            return redirect('contacts')
    else:
        form = BookingForm()

    return render(request, 'menu/contacts.html', {'form': form})
