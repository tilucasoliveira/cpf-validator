import unittest
from src.ValidateCpfFunction.cpf_validator import validate_cpf, save_cpf, get_cpf

class TestValidateCpf(unittest.TestCase):
    def test_valid_cpf(self):
        self.assertTrue(validate_cpf('123.456.789-09'))

    def test_invalid_cpf(self):
        self.assertFalse(validate_cpf('123.456.789-00'))

    def test_save_and_get_cpf(self):
        save_cpf('123.456.789-09')
        result = get_cpf('123.456.789-09')
        self.assertIsNotNone(result)

if __name__ == '__main__':
    unittest.main()
