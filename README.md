# 2026.1-PABD

## 1. Criar e ativar o ambiente virtual
python3 -m venv env

#Linux / macOS
source env/bin/activate
#Windows
env\Scripts\activate

## 2. Instalar as dependências do projeto
* pip install django # Framework web principal
* pip install djangorestframework # Biblioteca para construção de APIs REST
* pip install psycopg2-binary # Driver de conexão com o PostgreSQL
* pip install markdown # Suporte a markdown na interface do DRF
* pip install django-filter # Filtros avançados nas consultas da API

## 3. Salvar as dependências em requirements.txt
pip freeze > requirements.txt

## 4. Criar o projeto principal chamado 'amazon'
django-admin startproject amazon

# Entrar na pasta do projeto
cd amazon

# Criar o aplicativo de backend
python manage.py startapp backend
