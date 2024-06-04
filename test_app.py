import unittest
from app import app

class PruebasAplicacionSaludo(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_pagina_inicio(self):
        respuesta = self.app.get('/')
        self.assertEqual(respuesta.status_code, 200)
        self.assertIn("¡Bienvenido a la Aplicación 'Saludo' de Salvador Flores!", respuesta.data.decode('utf-8'))

    def test_pagina_saludo_get(self):
        response = self.app.get('/saludo')
        self.assertEqual(response.status_code, 200)
        self.assertIn('<title>saludo</title>', response.data.decode('utf-8'))

    def test_pagina_saludo_post(self):
        usuario = 'Usuario'
        fecha_nacimiento = '2000-01-01'
        respuesta = self.app.post('/saludo', data=dict(usuario=usuario, fecha_nacimiento=fecha_nacimiento))
        self.assertEqual(respuesta.status_code, 200)
        self.assertIn(f'¡Hola, {usuario}! Le damos la bienvenida a nuestro servicio exclusivo.<br>Su fecha de nacimiento es {fecha_nacimiento}.', respuesta.data.decode('utf-8'))

if __name__ == '__main__':
    unittest.main()
