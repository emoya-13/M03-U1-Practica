import unittest
from security import validar_password

class TestSecurity(unittest.TestCase):
    def test_password_curt(self):
        # Aquest ha de retornar False perquè té menys de 8 caràcters
        self.assertFalse(validar_password("12345"))

    def test_password_llarg(self):
        # Aquest ha de retornar True
        self.assertTrue(validar_password("configuracio123"))
