from setuptools import setup

setup(
    name='aplicacion-saludo',
    version='1.0.0',
    packages=['app'],
    include_packages=['app'],
    install_requires=['Flask'],
    entry_points={'console_scripts': ['app = app.app:run']}
)
