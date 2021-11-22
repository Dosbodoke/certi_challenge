import unittest
from utils import number_to_text_format

class TestNumberConversion(unittest.TestCase):
    def test(self):
        self.assertEqual(number_to_text_format('5489'), 'cinco mil e quatrocentos e oitenta e nove')
        self.assertEqual(number_to_text_format('-00'), 'zero')
        self.assertEqual(number_to_text_format('-500'), 'menos quinhentos')
        self.assertEqual(number_to_text_format('8751'), 'oito mil e setecentos e cinquenta e um')
        self.assertEqual(number_to_text_format('-95418'), 'menos noventa e cinco mil e quatrocentos e dezoito')
        self.assertEqual(number_to_text_format('1000'), 'mil')
        self.assertEqual(number_to_text_format('21005'), 'vinte e um mil e cinco')
        self.assertEqual(number_to_text_format('99999'), 'noventa e nove mil e novecentos e noventa e nove')
        self.assertEqual(number_to_text_format('-108'), 'menos cento e oito')
        self.assertEqual(number_to_text_format('-100'), 'menos cem')

if __name__ == "__main__":
    unittest.main()