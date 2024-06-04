Aplicación de Saludo con Flask en Python

El proyecto presenta una sencilla aplicación en lenguaje python con framework web Flask que permite a los usuarios saludarse e ingresar su fecha de nacimiento. La aplicación se ejecuta en una instancia EC2 de Amazon Linux y se documenta para facilitar su distribución e instalación.

Requisitos:

Instancia EC2 en AWS con máquina Amazon Linux t2.micro o superior
Grupos de seguridad con puertos 80 y 5000 habilitados
Python 3, pip3, git y Flask instalados

Pasos para la instalación:

-Configurar la instancia EC2:

-Cree una instancia EC2 con Amazon Linux t2.micro.
Edite el Security Group para permitir el tráfico en los puertos 80 y 5000.
Instalar herramientas básicas:

-Conéctese a la instancia EC2.

-Ejecute los siguientes comandos para instalar Python 3, pip3, git y Flask:

sudo yum update -y
sudo yum install -y python3 git
python3 --version
sudo yum install -y python3-pip
pip3 --version
sudo pip3 install --upgrade pip

-Clonar el repositorio:

En GitHub, vaya al repositorio https://github.com/saflores82/examen2.git y copie la URL HTTPS.
En la consola EC2, clone el repositorio usando el comando:

git clone https://github.com/saflores82/examen2.git

Instalar dependencias:

Navegue a la carpeta examen2:
cd examen2

Instale Flask usando pip3:
sudo pip3 install Flask

Ejecutar la aplicación con el comando:
sudo python3 app.py

La aplicación se ejecutará en el puerto 80. Puede acceder a ella desde un navegador web con la dirección http://<ip-de-su-ec2>.

Ejecutar pruebas unitarias:

Verifique el funcionamiento de la aplicación con las pruebas unitarias:
sudo python3 unittest test_app.py

Distribución y Documentación:

Creo un archivo que generar una lista con todas las dependencias de la aplicación llamado requirements.txt ejecutando el siguiente comando:
pip freeze > requirements.txt  

Cree un archivo setup.py para configurar la instalación del paquete, muestro el ejemplo a continuación:

from setuptools import setup

setup(
    name='aplicacion-saludo',
    version='1.0.0',
    packages=['app'],
    include_packages=['app'],
    install_requires=['Flask'],
    entry_points={'console_scripts': ['app = app.app:run']}
)

-El archivo se ejecuta con el siguiente comando: 
python3 setup.py sdist

P.D.
Este README proporciona una guía básica para la instalación y ejecución de esta aplicación. Le recomiendo adaptar los pasos a su entorno específico de trabajo y considerar algunos aspectos adicionales como la gestión de usuarios, bases de datos y la seguridad para la correcta implementación en producción.
