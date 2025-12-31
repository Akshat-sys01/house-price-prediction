#!/usr/bin/env bash

pip install -r requirements.txt

cd house_price_web

python manage.py collectstatic --noinput
python manage.py migrate