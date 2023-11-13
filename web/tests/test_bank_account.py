import unittest
import sys
import os
# Add the src directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from upload.bank_account import deposit, withdraw
class TestBankAccount(unittest.TestCase):
    def test_deposit(self):
        account = (123456, 1000.0)
        account = deposit(account, 200.0)
        self.assertEqual(account, (123456, 1200.0))
    def test_withdraw(self):
        account = (123456, 1000.0)
        account = withdraw(account, 150.0)
        self.assertEqual(account, (123456, 850.0))
if __name__ == "__main__":
    unittest.main()