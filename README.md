# Django Blog API

Some text

## Install

### Pip and Pipenv

Install `pip` and `pipenv`

Ubuntu/Debian:

```
$ sudo apt install python3-pip
$ sudo -H pip3 install pipenv
```

Arch/Manjaro:

```
$ sudo pacman -S python-pip
$ sudo -H pip3 install pipenv
```

### Install dependencies

Go to the project directory, create virtualenv, and sync it with project

```
$ pipenv sync
```

### Run server

To get started you need to go to the virtualenv

```
$ pipenv shell
```

At the first start you need to create DB

```
$ python manage.py migrate
```

And run server

```
$ python manage.py runserver
```
