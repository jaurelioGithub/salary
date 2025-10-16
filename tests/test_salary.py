# test_salary.py
import unittest
from src.salary import salary

class TestSalary(unittest.TestCase):

    def test_salario(self):
        self.assertEqual(salary(30, 2000), 50000)
        self.assertEqual(salary(50, 2000), 110000)

if __name__ == '__main__':
    unittest.main()