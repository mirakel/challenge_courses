# Aplicacion de cursos
Aplicación de cursos con carrito de compras en django

## Ejecutar

Para ejecutar el proyecto debe de tener instalado VirtualWrapper, Python3 y pip3, y sigas las instrucciones:
Nota: si esta trabajando con Virtualenv, puede ejecutar por ejemplo: virtualenv -p python3 env_django1.11.7


```
$ git clone git@github.com:mirakel/challenge_courses.git
```

```
$ python3 -m venv venv
```

```
$ cd carrito_compra/
```

```
$ pip install -r requirements.txt
```

```
$ python manage.py makemigrations
```


```
$ python manage.py migrate
```

```
$ python manage.py createsuperuser
```

```
$ python manage.py runserver
```
