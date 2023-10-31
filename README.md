# Read Me 

Entrega Final de Luis Hidalgo, hecha en Django-Python 

## Walkthrough

Un CRM donde se tiene la informacion de clientes, ordenes y productos, donde hay diferentes relaciones
y hay dos operaciones principales C (create) y R (Read), la operacion de lectura se puede evidenciar en 
cada una de las tablas y adicionalmente en la informacion de cada cliente se tiene una barra de busqueda
para filtrar por diferentes parametros. 

Se puede evidenciar las operacion de creaacion, actualizacion y borrado en los botones de las ordenes, tambien estan hechas por medio de la plantilla que nos facilita Django para hacer estas operaciones por medio de la plataforma de administracion, aqui tambien se puede actualizar la imagen de perfil de cada usuario y esta se mostrara en la cuenta de el mismo cuando inicie sesion. 

Adicionalmente se tienen dos pantallas una para el inicio de sesion y la otra para registro de clientes si no se tiene una cuenta, existen diferentes validaciones para la contraseña y una vez se complete este registro se tiene un mensaje de exito.

La restriccion de paginas esta hecha mediante los roles que se le asigne a cada usuario.

## Usage 

Programa usando Django 

bash
pip install django

y los filtros se estan haciendo mediante django-filter

bash
pip install django-filter

es necesario la instalacion de pillow para el manejo de imagenes

bash
pip install Pillow
