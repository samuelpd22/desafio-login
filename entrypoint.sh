#!/bin/sh

echo "Aguardando o banco de dados em $DB_HOST:$DB_PORT..."

# Aguarda o banco de dados estar pronto
while ! nc -z $DB_HOST $DB_PORT; do
  sleep 1
done

echo "Banco de dados pronto. Executando migrações para 'mypage'..."
python manage.py makemigrations mypage
python manage.py migrate mypage

echo "Iniciando o servidor Django..."
exec python manage.py runserver 0.0.0.0:8000
