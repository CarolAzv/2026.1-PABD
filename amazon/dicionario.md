# Migrações
#Gerar os arquivos de migração com base nos Models definidos
python manage.py makemigrations

#Aplicar as migrações ao banco de dados PostgreSQL
python manage.py migrate

#Criar um superusuário para acessar o painel de administração
python manage.py createsuperuser

#Iniciar o servidor de desenvolvimento
python manage.py runserver

# Postgres
#Verificar status
sudo service postgresql status

#inicie postgres
sudo service postgresql start

conectar
sudo -u postgres psql -c '\l'