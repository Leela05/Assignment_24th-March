import unittest

def check_even_or_not(x):
    if x % 2 == 0:
        return True
    else:
        return False

def check_prime_or_not(x):
    for n in range(2, int(x ** 0.5) + 1):
        if x % n == 0:
            return False
    return True

def check_divisible_by_7(x):
    if x % 7 == 0:
        return True
    else:
        return False

class check_evenOrOdd(unittest.TestCase):

    def test_case1(self):
        result = check_even_or_not(3)
        self.assertFalse(result)

    def test_case2(self):
        result = check_even_or_not(4)
        self.assertTrue(result)

class check_primeOrNot(unittest.TestCase):

    def test_case3(self):
        result = check_prime_or_not(4)
        self.assertFalse(result)

    def test_case4(self):
        result = check_prime_or_not(2)
        self.assertTrue(result)

class check_number(unittest.TestCase):

    def test_case4(self):
        result = check_divisible_by_7(4)
        self.assertFalse(result)
    def test_case5(self):
        result = check_divisible_by_7(14)
        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()