# 2026.1-PABD

## Baixar:
pip install django
pip install djangorestframework
pip install psycopg2-binary 
pip install markdown
pip install -U drf-yasg

## Criando Projeto com Django
django-admin startproject [nome]
cd [nome]
python manage.py startapp [nome]


DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'copa2026_db', # Nome do banco de dados
    'USER': 'mega_coach', # Usuário do PostgreSQL
    PASSWORD': 'coach123', # Senha do usuário
    'HOST': 'localhost', # Endereço do servidor
    'PORT': '5432', # Porta padrão do PostgreSQL
     }
}