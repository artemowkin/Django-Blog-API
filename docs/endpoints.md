# Endpoint'ы проекта

Весь REST API лежит на `/api/v1/`

Аутентификация:

* `/api/v1/auth/login/` - для входа в аккаунт нужно отправить POST запрос с JSON body `{'username': 'some_username', 'email': 'some_mail@mail.com', 'password': 'qwerty123'}`. После успешного входа сервер вернет API token, который надо сохранить
* `/api/v1/auth/logout/` - для выхода из аккаунта нужно отправить пустой POST запрос
* `/api/v1/auth/registration/` - для регистрации нужно отправить POST запрос с JSON body `{'username': 'some_username', 'email': 'some_mail@mail.com', 'password1': 'qwerty123', 'password2': 'qwerty123'}`, после чего сервер вернет API token

GET-запросы:

* `/api/v1/posts/` - возвращает список постов
* `/api/v1/posts/<id>/` - возвращает конкретный объект поста с указанным ID
* `/api/v1/posts/tag/<slug>/` - возвращает список постов, у которых есть тег с указанным slug'ом
* `/api/v1/users/` - возвращает список пользователей
* `/api/v1/users/<id>/` - возвращает конкретный объект пользователя с указанным ID 
* `/api/v1/users/<id>/posts/` - возвращает список постов автора с указанным ID

POST-запросы

* `/api/v1/posts/` - для добавления поста нужно отправить POST запрос с JSON body `{'title': 'some_title', 'body': 'some_text', 'tags': ['first_tag', 'second_tag']}`

DELETE-запросы

* `/api/v1/posts/<id>/` - для удаления поста с указанным ID нужно отправить пустой DELETE запрос

PUT-запросы

* `/api/v1/posts/<id>/` - для обновления поста нужно отправить POST запрос с JSON body `{'title': 'new_or_old_title', 'body': 'new_or_old_body', 'tags': ['new', 'or', 'old', 'tags']}`

# Авторизация

Для доступа к страницам, на которых нужна авторизация (сейчас это страницы, принимающие POST-запросы), в запрос нужно добавить header `Authorization: Token <token>`. Token надо было сохранить, ага
