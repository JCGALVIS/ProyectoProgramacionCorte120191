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
        self.assertEqual(f.calcular_precio_servicio_extras(1, 4), 525000.0)
        self.assertEqual(f.calcular_precio_servicio_extras(2, 1), 350000.0)

        pass

    def test_calcular_costo_envio(self):
        self.assertEqual(f.calcular_costo_envio(1), 115.0)
        self.assertEqual(f.calcular_costo_envio(0), 0.0)

        pass

    def test_calcular_precio_producto_fuera(self):
        self.assertEqual(f.calcular_precio_producto_fuera(1000, 1), 1615.0)
        self.assertEqual(f.calcular_precio_producto_fuera(2000, 1), 3115.0)
        pass

    def test_calcular_iva_producto(self):
        self.assertEqual(f.calcular_iva_producto(1000, 0.19), 190.0)
        self.assertEqual(f.calcular_iva_producto(2000, 0.19), 380.0)
        pass

    def test_calcular_iva_servicio(self):
        self.assertEqual(f.calcular_iva_servicio(4, 0.19), 76000.0)
        self.assertEqual(f.calcular_iva_servicio(2, 0.16), 32000.0)
        pass

    def test_calcular_iva_envio(self):
        self.assertEqual(f.calcular_iva_envio(1, 0.19), 21.85)
        self.assertEqual(f.calcular_iva_envio(0, 0.19), 0.0)
        pass

    def test_calcular_iva_servicio_fuera(self):
        self.assertEqual(f.calcular_iva_servicio_fuera(1, 0.19), 23750.0)
        self.assertEqual(f.calcular_iva_servicio_fuera(0, 0.19), 0.0)
        pass

    def test_calcular_recaudo_locales(self):
        self.assertEqual(f.calcular_recaudo_locales(1000, 1500, 2000), 4500.0)
        self.assertEqual(f.calcular_recaudo_locales(0, 1500, 0), 1500.0)
        pass

    """
    def test_calcular_recaudo_horas_extra(self):
       self.assertEqual(f.calcular_recaudo_horas_extra(), )
       self.assertEqual(f.calcular_recaudo_horas_extra(), )
       pass

    def test_calcular_recaudo_mixto_local(self):
       self.assertEqual(f.calcular_recaudo_mixto_local(), )
       self.assertEqual(f.calcular_recaudo_mixto_local(), )
       pass
  """


if __name__ == 'main':
    unittest.main()
