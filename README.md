# Trattoria Bella — демо-сайт ресторану на Django

Демонстраційний сайт ресторану для портфоліо. Django + Bootstrap 5.

## Що є на сайті

- Головна сторінка з hero-банером
- Сторінка меню (категорії + страви, керується через адмінку)
- Сторінка "Про нас"
- Контакти + форма бронювання столика
- Django Admin для редагування меню без коду

---

## 🚀 Запуск локально

### 1. Встанови залежності

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

### 2. Створи файл .env

Скопіюй `.env.example` в `.env` і заповни (для локальної розробки можна залишити як є).

### 3. Виконай міграції

```bash
python manage.py migrate
```

### 4. Заповни демо-даними (страви, категорії)

```bash
python manage.py seed_menu
```

### 5. Створи адміна

```bash
python manage.py createsuperuser
```

### 6. Запусти сервер

```bash
python manage.py runserver
```

Відкрий у браузері:
- Сайт: http://127.0.0.1:8000/
- Адмінка: http://127.0.0.1:8000/admin/

---

## 🌐 Деплой на Railway

### 1. Залий проєкт на GitHub

```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/твій-нік/restaurant-demo.git
git push -u origin main
```

### 2. На Railway

1. Зареєструйся на [railway.app](https://railway.app)
2. **New Project → Deploy from GitHub repo** → обери свій репозиторій
3. **+ New → Database → PostgreSQL** (Railway автоматично підставить `DATABASE_URL`)
4. У вкладці **Variables** додай:
   ```
   SECRET_KEY=довгий-випадковий-рядок-тут
   DEBUG=False
   ```
5. Railway автоматично визначить Procfile і задеплоїть проєкт

### 3. Після деплою виконай міграції та seed

У вкладці сервісу → **Settings → Deploy → відкрий термінал** (або через Railway CLI):

```bash
railway run python manage.py migrate
railway run python manage.py seed_menu
railway run python manage.py createsuperuser
```

### 4. Готово

Railway видасть домен типу `your-app.up.railway.app` — це і є твоє демо для портфоліо.

---

## 📁 Як редагувати меню (для клієнта)

Все відбувається через адмінку `/admin/`:
1. Заходиш під своїм логіном
2. **Категорії меню** — додаєш/редагуєш розділи (Перші страви, Десерти і т.д.)
3. Всередині категорії додаєш страви прямо в таблиці — назва, ціна, фото
4. Зміни одразу з'являються на сайті, без участі розробника

---

## 🛠️ Технології

- Python 3.12 + Django 5.0
- Bootstrap 5.3
- SQLite (локально) / PostgreSQL (Railway)
- Gunicorn + Whitenoise (продакшен)
