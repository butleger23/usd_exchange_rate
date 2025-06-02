# USD exchange rate
Тестовое задание для получение актуального курса USD/RUB

##  Технологии
* Django 5.2
* Python 3.12
* django-ratelimit
* requests


## Настройка и запуск
Склонировать проект:
```
git clone https://github.com/butleger23/usd_exchange_rate.git
cd usd_exchange_rate
```
Выполнить
```
python manage.py runserver
```

Можно проверить работу проекта по адресу `http://localhost:8000/get_current_usd/`

Либо использовать curl команду из bash консоли: `curl http://127.0.0.1:8000/get-current-usd/`