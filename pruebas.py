import unittest
import funciones as f

class pruebas(unittest.TestCase):

    def test_calcular_precio_producto(self):
        self.assertEqual(f.calcular_precio_producto(1000), 1500)
        self.assertEqual(f.calcular_precio_producto(1500), 2250)
        self.assertEqual(f.calcular_precio_producto(0), 'El costo del producto debe ser mayor a cero.')
        self.assertEqual(f.calcular_precio_producto(-200), 'El costo del producto debe ser mayor a cero.')
        pass

    def test_calcular_precio_servicio(self):
        self.assertEqual(f.calcular_precio_servicio(5), 500000)
        self.assertEqual(f.calcular_precio_servicio(3), 300000)
        self.assertEqual(f.calcular_precio_servicio(0), 'Las horas deben ser mayor a cero.')
        self.assertEqual(f.calcular_precio_servicio(-2), 'Las horas deben ser mayor a cero.')
        pass

    def test_calcular_precio_servicio_extras(self):
        self.assertEqual(f.calcular_precio_servicio_extras(2), 250000)
        self.assertEqual(f.calcular_precio_servicio_extras(0), 'El servicio no genera horas extras.')
        self.assertEqual(f.calcular_precio_servicio_extras(-1), 'Las horas deben ser mayor a cero.')
        pass

    def test_calcular_costo_envio(self):
        self.assertEqual(f.calcular_costo_envio(2), 230)
        self.assertEqual(f.calcular_costo_envio(0), 0)
        self.assertEqual(f.calcular_costo_envio(-2), 'El numero de kilometros debe ser mayor a cero.')
        pass

    def test_calcular_precio_producto_extra(self):
        self.assertEqual(f.calcular_precio_producto_extra(600, 20), 3200)
        self.assertEqual(f.calcular_precio_producto_extra(2000, 50), 8750)
        self.assertEqual(f.calcular_precio_producto_extra(1100, 0), 1650)
        self.assertEqual(f.calcular_precio_producto_extra(1100, 0), 1650)
        self.assertEqual(f.calcular_precio_producto_extra(0, 10), 'El costo del producto debe ser mayor a cero.')
        pass

    def test_calcular_iva_producto(self):
        self.assertEqual(f.calcular_iva_producto(1000, 0.19), 285)
        self.assertEqual(f.calcular_iva_producto(1000, 0), 0)
        self.assertEqual(f.calcular_iva_producto(0, 0), 'El costo del producto debe ser mayor a cero.')
        pass

    def test_calcular_iva_servicio(self):
        self.assertEqual(f.calcular_iva_servicio(4, 0.19), 76000)
        self.assertEqual(f.calcular_iva_servicio(4, 0), 0)
        self.assertEqual(f.calcular_iva_servicio(0, 0.19), 'El numero de horas debe ser mayor a cero.')
        pass

    def test_calcular_iva_envio(self):
        self.assertEqual(f.calcular_iva_envio(2, 0.19), 43.7)
        self.assertEqual(f.calcular_iva_envio(8, 0.19), 174.8)
        self.assertEqual(f.calcular_iva_envio(0, 0.19), 0)
        self.assertEqual(f.calcular_iva_envio(4, 0), 0)
        self.assertEqual(f.calcular_iva_envio(-3, 0.19), 'El numero de kilometros no debe ser menor a cero.')
        pass

    """
    def test_calcular_iva_servicio_fuera(self):
        self.assertEqual(f.calcular_iva_servicio_fuera(1, 0.19), 23750.0)
        self.assertEqual(f.calcular_iva_servicio_fuera(0, 0.19), 0.0)
        pass

    def test_calcular_recaudo_locales(self):
        self.assertEqual(f.calcular_recaudo_locales(1000, 1500, 2000), 4500.0)
        pass

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
