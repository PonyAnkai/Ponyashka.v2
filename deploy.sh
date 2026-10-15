#!/bin/bash
set -e

echo "[1] Pull last-version"
cd /var/www/ponyashka.bot
git fetch origin
git reset --hard origin/master

echo "[2] Setup requirements"
pip install -r requirements.txt

# Сделать собственные миграции
# echo "[3] Setup migrations"
# python3 app/manage.py migrate --noinput

# echo "[4] Setup collectstatic"
# python3 app/manage.py collectstatic --clear --noinput
# mkdir -p app/media

echo "[3] Restart bot ponyashka.bot"
sudo systemctl restart ponyashka.bot