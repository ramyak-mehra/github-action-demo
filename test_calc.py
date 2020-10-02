import unittest
import calc
class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(19 , 2) , 21)
        self.assertEqual(calc.add(-1 , 1) , 0)
        self.assertEqual(calc.add(-2 , -2) , -4)


    def test_subtract(self):
        self.assertEqual(calc.subtract(19 , 2) , 17)
        self.assertEqual(calc.subtract(-1 , 1) , -2)
        self.assertEqual(calc.subtract(-2 , -2) , 0)

    def test_multiply(self):
        self.assertEqual(calc.multiply(5 , 2) , 10)
        self.assertEqual(calc.multiply(-1 , 0) , 0)
        self.assertEqual(calc.multiply(-2 , -2) , 4)

    def test_divide(self):
        self.assertEqual(calc.divide(20 , 2) , 10)
        self.assertEqual(calc.divide(-1 , 1) , -1)
        self.assertEqual(calc.divide(-2 , -2) , 1)
        self.assertRaises(ValueError , calc.divide , 10 , 0)
   

if __name__ == '__main__':
    unittest.main()