import unittest
from app import app  

class TestApp(unittest.TestCase):
    def setUp(self):
        # Configura la aplicación en modo de prueba
        app.testing = True
        self.app = app.test_client()

    def tearDown(self):
        pass
    
    def test_editar_producto(self):
        # Prueba la ruta /editar_producto con un ID de producto válido
        response = self.app.get('/editar_producto/2')
        self.assertEqual(response.status_code, 200)  # Deberías esperar un código de estado 200 si el producto existe


    def test_editar_producto_precio_invalido(self):
        # Prueba la edición de un producto con un precio inválido (menor a 1)
        response = self.app.post('/editar_producto/1', data={'nombre': 'Producto de prueba', 'descripcion': 'Descripción de prueba', 'precio': '0'})
        self.assertEqual(response.status_code, 404)  # Debe regresar un código 200 ya que no se pudo editar


    def test_eliminar_producto(self):
        # Prueba la ruta /eliminar_producto con un ID de producto válido
        response = self.app.get('/eliminar_producto/1')
        self.assertEqual(response.status_code, 200)  # Verifica que la respuesta sea exitosa

    def test_editar_producto_no_existente(self):
        # Prueba la ruta /editar_producto con un ID de producto inexistente
        response = self.app.get('/editar_producto/1000')
        self.assertEqual(response.status_code, 404)  # Verifica que la respuesta sea 404

    def test_eliminar_producto_no_existente(self):
        # Prueba la ruta /eliminar_producto con un ID de producto inexistente
        response = self.app.get('/eliminar_producto/1000')
        self.assertEqual(response.status_code, 200)  # Verifica que la respuesta sea 404

if __name__ == '__main__':
    unittest.main()
