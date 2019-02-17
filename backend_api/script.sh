#!/bin/sh

# wait-for-postgres.sh

set -e

host="$1"

until PGPASSWORD=$POSTGRES_PASSWORD psql -h address_book_database -U "$POSTGRES_USER" address_db -c '\q'; do
  >&2 echo "Postgres is unavailable - sleeping"
  sleep 1
done

>&2 echo "Postgres is up - executing command"

sleep 5

python manage.py db init
python manage.py db migrate
python manage.py db upgrade
python run.py
