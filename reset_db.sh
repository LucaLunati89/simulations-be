#!/bin/bash

echo "⚠️ Reset completo del progetto Django..."

# 1. Rimuovo DB e migrazioni
echo "🗑️  Rimozione vecchio db.sqlite3 e migrazioni..."
rm -f db.sqlite3
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete

# 2. Svuoto cache Python
echo "🧹 Pulizia cache Python..."
find . -type d -name "__pycache__" -exec rm -rf {} +

# 3. Reinstallo Django (ultima versione 4.x)
echo "📦 Reinstallazione Django..."
pip uninstall -y django
pip install "django>=4.2,<5"

# 4. Ricreo DB e migrazioni
echo "🛠️  Creazione nuove migrazioni e database..."
python manage.py makemigrations
python manage.py migrate

# 5. Ricreo superuser senza password (admin)
echo "👤 Creazione superuser admin..."
echo "from django.contrib.auth import get_user_model; \
User = get_user_model(); \
User.objects.filter(username='admin').delete(); \
User.objects.create_superuser('admin', 'admin@example.com', 'admin1234')" \
| python manage.py shell

# 6. Rigenero requirements.txt
echo "📑 Rigenerazione requirements.txt..."
pip freeze > requirements.txt

echo "✅ Reset completato! Puoi accedere con user: admin (senza password)."
