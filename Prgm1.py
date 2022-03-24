import unittest

def addition(x, y):
    return x + y

def add3num(x, y, z):
    return x + y +z

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

class calculator(unittest.TestCase):
    def test_case1(self):
        number1 = 4
        number2 = 5
        result = addition(number1, number2)
        self.assertEqual(number1+number2, result)

    def test_case2(self):
        number1 = 4
        number2 = 5
        number3 = 6
        result = add3num(number1, number2, number3)
        self.assertEqual(number1+number2+number3, result)

    def test_case3(self):
        number1 = 5
        number2 = 4
        result = subtraction(number1, number2)
        self.assertEqual(number1 - number2, result)

    def test_case4(self):
        number1 = 4
        number2 = 5
        result = multiplication(number1, number2)
        self.assertEqual(number1 * number2, result)

    def test_case5(self):
        number1 = 8
        number2 = 4
        result = division(number1, number2)
        self.assertEqual(number1 / number2, result)


if __name__ == "__main__":
    unittest.main()

