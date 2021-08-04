# EmphaSoft_test
Реализация SCUD API приложения Users тестового проекта EmphaSoft.


# Использованные языки и фреймворки:
- [Python](https://www.python.org/) 3.8.8
- [Django](https://www.djangoproject.com/) 2.2.19
- [Django Rest Framework](https://www.django-rest-framework.org/) 3.12.4


# Приступая к работе

- Клонируйте репозиторий:
```
git clone https://github.com/DmitriyReztsov/EmphaSoft_test.git
```

- Установите зависимости:
```
pip install -r requirements.txt
```

- Выполните миграции:
```
python manage.py makemigrations
python manage.py migrate
```

- Создайте суперпользователя:
```
python manage.py createsuperuser
Username (leave blank to use 'user'): # Придумайте логин (например, admin)
Email address: # укажите почту
Password: # придумайте пароль
Password (again): # повторите пароль
Superuser created successfully.
```

- Запустите сервер:
```
python manage.py runserver
```


# Endpoints

Запустите сервер. Доступные эндпойнты будут доступны по адресу http://127.0.0.1:8000/swagger/

Список доступных эндпойнтов:
| Endpoint | Доступные методы | Описание |
| -------- | ---------------- | -------- |
| /api-token-auth/ | POST | получение токена для дальнейших запросов |
| /api/v1/users/ | GET | получение списка всех пользователей |
| /api/v1/users/ | POST | создание нового пользователя |
| /api/v1/users/{id}/ | GET | получение детальной информации о пользователе {id} |
| /api/v1/users/{id}/ | PUT, PATCH | внесение изменения (полного или частичного соответственно) в информацию о пользователе {id} |
| /api/v1/users/{id}/ | DELETE | пользователю {id} устанавливается значение is_active=False |

## Тестирование эндпойнтов

Возможно тестирование из браузера по адресу: http://127.0.0.1:8000/swagger/
Для этого необходимо получить токен на пользователя, от имени которого будут отправляться запросы:
1. выполните POST запрос на эндпойнт `/api-token-auth/`, указав в теле запроса `username` и `password`
2. в ответ вы получите токен, который необходимо передавать в заголовке следующих запросов
3. нажмите кнопку Authorize и внесите полученный токен: "Token <полученный токен>"
4. выполняйте запросы, заполняя требуемую информацию в теле запроса или в части url.


# Линтер

- flake8

Для проверки линтером соответствия кода стандартам PEP8 выполнить:
```
flake8 scud_user/
flake8 users/
```


# Автор

Dmitriy Reztsov
