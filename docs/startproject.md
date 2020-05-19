# Запуск проекта

Для того, чтобы запустить проект, надо сначала установить `pip` и `pipenv`. Если они уже установлены, можно переходить к установке зависимостей

## Установка pip и pipenv

Для Ubuntu/Debian

```
$ sudo apt install python3-pip
$ sudo -H pip3 install pipenv
```

Для Manjaro/Arch

```
$ sudo pacman -S python-pip
$ sudo -H pip install pipenv
```

Для Fedora/RHEL

```
$ sudo dnf install python3-pip
$ sudo -H pip3 install pipenv
```

## Установка зависимостей

Из папки проекта, где лежат файлы `Pipfile` и `Pipfile.lock`, нужно выполнить следующую команду

```
$ pipenv sync
```

## Запуск сервера для разработки

После установки зависимостей нужно перейти в virtualenv

```
$ pipenv shell
```

Приглашение для ввода в консоли должно поменяться на что-то такое:

```
(test-api-blog) $
```

> Чтобы выйти из virtualenv, нужно написать exit

При первом запуске нужно создать базу данных (при последующих этого не требуется)

```
(test-api-blog) $ python manage.py migrate
```

Можно запускать сервер

```
(test-api-blog) $ python manage.py runserver
```
