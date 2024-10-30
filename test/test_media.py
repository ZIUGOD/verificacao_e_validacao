import unittest
from media import calcular_media


class TestMedia(unittest.TestCase):

    def test_media_basica(self):
        # Teste básico com três notas distintas
        self.assertEqual(calcular_media(7, 8, 9), 8.0)

    def test_media_zero(self):
        # Teste com todas as notas zero
        self.assertEqual(calcular_media(0, 0, 0), 0.0)

    def test_media_valor_maximo(self):
        # Teste com notas máximas (considerando nota máxima == 10)
        self.assertEqual(calcular_media(10, 10, 10), 10.0)

    def test_media_valores_decimais(self):
        # Teste com valores decimais
        self.assertAlmostEqual(calcular_media(7.5, 8.5, 9.5), 8.5)

    def test_media_valores_negativos(self):
        # Teste com valores negativos
        self.assertAlmostEqual(calcular_media(-5, -10, -15), -10.0)

    def test_media_valores_mistos(self):
        # Teste com valores positivos e negativos
        self.assertAlmostEqual(calcular_media(-5, 10, 5), 3.33, places=2)

    def test_media_entrada_invalida(self):
        # Teste com valores não numéricos para verificar a validação de tipo
        with self.assertRaises(ValueError):
            calcular_media("a", 5, 10)

    def test_media_entrada_none(self):
        # Teste com None como uma das notas
        with self.assertRaises(ValueError):
            calcular_media(None, 5, 10)

    def test_media_com_uma_nota(self):
        # Teste com apenas uma nota válida para verificação do número de argumentos
        with self.assertRaises(TypeError):
            calcular_media(10)

    def test_media_valor_extremamente_alto(self):
        # Teste com valores muito altos
        self.assertAlmostEqual(calcular_media(1e6, 1e6, 1e6), 1e6)

    def test_media_com_minimo_e_maximo(self):
        # Teste com valores mínimo e máximo para verificação de borda
        self.assertAlmostEqual(calcular_media(-1e6, 0, 1e6), 0)


if __name__ == "__main__":
    unittest.main()
