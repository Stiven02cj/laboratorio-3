import unittest
from src.procesador import Analizador

class TestAnalizador(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.analizador = Analizador("data/sri_ventas_2024.csv")

    def test_ventas_totales_como_diccionario(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        self.assertIsInstance(resumen, dict)
    
    def test_ventas_totales_todaslas_provincias(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        total_provincias = len(resumen)
        # El archivo contiene registros "ND" en provincias
        self.assertEqual(total_provincias, 24)

    def test_ventas_totales_todaslas_mayores_0(self):
        resumen = self.analizador.ventas_totales_por_provincia()
        self.assertTrue(all(float(v)> 0 for v in resumen.values()))

    def test_ventas_por_provincia_inexistente(self):
        with self.assertRaises(KeyError):
            self.analizador.ventas_por_provincia("Narnia")
    