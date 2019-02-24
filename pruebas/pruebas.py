import unittest
import funciones as f

class pruebas(unittest.TestCase):

    def test_calcular_precio_producto(self):

        self.assertEqual(f.calcular_precio_producto(1000), 1500.0)
        self.assertEqual(f.calcular_precio_producto(2000), 3000.0)
        self.assertEqual(f.calcular_precio_producto(0), 0)
        pass

    def test_calcular_precio_servicio(self):

        self.assertEqual(f.calcular_precio_servicio(4), 400000.0)
        self.assertEqual(f.calcular_precio_servicio(5), 500000.0)
        self.assertEqual(f.calcular_precio_servicio(0), 0)
        pass

    def test_calcular_precio_servicio_extras(self):

        self.assertEqual(f.calcular_precio_servicio_extras(1), 525000.0)

        self.assertEqual(f.calcular_precio_servicio_extras(2), 650000.0)

        pass

    def test_calcular_costo_envio(self):

        self.assertEqual(f.calcular_costo_envio(1), 115.0)
        self.assertEqual(f.calcular_costo_envio(0), 0.0)

        pass

    def test_calcular_precio_producto_fuera(self):
        self.assertEqual(f.calcular_costo_envio_fuera(1000,1), 1615.0)
        pass

    def test_calcular_iva_producto(self):
        pass

    def test_calcular_recaudo_locales(self):
        pass

    def test_calcular_recaudo_horas_extra(self):
        pass

    def test_calcular_recaudo_mixto_local(self):
        pass

if __name__ == 'main':
    unittest.main()
