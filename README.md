
# ToolTracker

Webová aplikácia pre evidenciu náradia (Django).

## Inštalácia (lokálne)

1. Vytvor virtuálne prostredie a aktivuj ho:
   ```bash
   python -m venv venv
   source venv/bin/activate   # alebo .\venv\Scripts\activate na Windows
   ```

2. Nainštaluj balíčky:
   ```bash
   pip install -r requirements.txt
   ```

3. Spusti migrácie:
   ```bash
   python manage.py migrate
   ```

4. Spusti server:
   ```bash
   python manage.py runserver
   ```

5. Vytvor admin účet:
   ```bash
   python manage.py createsuperuser
   ```

## Deploy na Render
- Vytvor nový Web Service na [https://render.com](https://render.com)
- Nahraj projekt cez GitHub
- Pridaj PostgreSQL databázu
- Nastav env premenné: `DATABASE_URL`, `SECRET_KEY`, `DEBUG`
- Build command: `pip install -r requirements.txt && python manage.py migrate`
- Start command: `gunicorn tooltracker.wsgi`

