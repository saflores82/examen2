¡Leeme! - Aplicación de Saludo con Flask en Python
Este proyecto presenta una sencilla aplicación web Flask que permite a los usuarios saludarse e ingresar su fecha de nacimiento. La aplicación se ejecuta en una instancia EC2 de Amazon Linux y se documenta para facilitar su distribución e instalación.

Requisitos:

Instancia EC2 con máquina Amazon Linux t2.micro
Seguridad Group con puertos 80 y 5000 habilitados
Python 3, pip3, git y Flask instalados
Pasos de instalación:

Configurar la instancia EC2:

Cree una instancia EC2 con Amazon Linux t2.micro.
Edite el Security Group para permitir el tráfico en los puertos 80 y 5000.
Instalar herramientas básicas:

Conéctese a la instancia EC2 mediante SSH.
Ejecute los siguientes comandos para instalar Python 3, pip3, git y Flask:
Bash
sudo yum update -y
sudo yum install -y python3 git
python3 --version
sudo yum install -y python3-pip
pip3 --version
sudo pip3 install --upgrade pip
Usa el código con precaución.
content_copy
Clonar el repositorio:

En GitHub, vaya al repositorio https://github.com/ComlanGiovanni/42-Exam-Rank-02 y copie la URL SSH.
En la consola EC2, clone el repositorio usando el comando:
Bash
git clone https://github.com/saflores82/examen2.git
Usa el código con precaución.
content_copy
Instalar dependencias:

Navegue a la carpeta examen2.
Instale Flask usando pip3:
Bash
sudo pip3 install Flask
Usa el código con precaución.
content_copy
Ejecutar la aplicación:

Inicie la aplicación con el comando:
Bash
sudo python3 app.py
Usa el código con precaución.
content_copy
La aplicación se ejecutará en el puerto 80. Puede acceder a ella desde un navegador web en la dirección http://<su-direccion-ip>:80.
Ejecutar pruebas unitarias:

Verifique el funcionamiento de la aplicación con las pruebas unitarias:
Bash
sudo python3 unittest test_app.py
Usa el código con precaución.
content_copy
Distribución y Documentación:

Crear archivo requirements.txt:

Ejecute el comando pip freeze > requirements.txt para generar una lista de dependencias de la aplicación.
Crear archivo setup.py:

Cree un archivo setup.py para configurar la instalación del paquete. Un ejemplo básico se muestra a continuación:
Python
from setuptools import setup

setup(
    name='aplicacion-saludo',
    version='1.0.0',
    packages=['app'],
    include_packages=['app'],
    install_requires=['Flask'],
    entry_points={'console_scripts': ['app = app.app:run']}
)
Usa el código con precaución.
content_copy
Recursos adicionales:

Documentación de Flask: https://palletsprojects.com/
Tutorial de setuptools: https://docs.readthedocs.io/en/stable/tutorial/index.html
Documentación de pipenv: https://readthedocs.org/projects/pipenv/
Documentación de Docker: https://docs.docker.com/
Documentación de Sphinx: https://docs.readthedocs.io/
PlantUML: https://plantuml.com/
Nota:

Este README proporciona una guía básica para la instalación y ejecución de la aplicación. Se recomienda adaptar los pasos a su entorno específico y considerar aspectos adicionales como la gestión de usuarios, bases de datos y seguridad para una implementación completa en producción.
