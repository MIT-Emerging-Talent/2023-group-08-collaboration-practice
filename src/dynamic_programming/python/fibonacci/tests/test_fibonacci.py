import unittest


from src.fibonacci import fib_basic, fib_recursion,fib_list


class TestFibBasic(unittest.TestCase):
    def test_with_0(self):
        num = 0
        result = 0
        self.assertEqual(fib_basic(num), result)

    def test_with_1(self):
        num = 1
        result = 1
        self.assertEqual(fib_basic(num), result)

    def test_with_2(self):
        num = 2
        result = 1
        self.assertEqual(fib_basic(num), result)

    def test_with_10(self):
        num = 10
        result = 55
        self.assertEqual(fib_basic(num), result)

    def test_with_20(self):
        num = 20
        result = 6765
        self.assertEqual(fib_basic(num), result)


class TestFibMemo(unittest.TestCase):
    def test_with_0(self):
        num = 0
        result = 0
        self.assertEqual(fib_recursion(num), result)

    def test_with_1(self):
        num = 1
        result = 1
        self.assertEqual(fib_recursion(num), result)

    def test_with_2(self):
        num = 2
        result = 1
        self.assertEqual(fib_recursion(num), result)

    def test_with_10(self):
        num = 10
        result = 55
        self.assertEqual(fib_recursion(num), result)

    def test_with_20(self):
        num = 20
        result = 6765
        self.assertEqual(fib_recursion(num), result)


class TestFibTab(unittest.TestCase):
    def test_with_0(self):
        num = 0
        result = [0,1]
        self.assertEqual(fib_list(num), result)

    def test_with_1(self):
        num = 1
        result = [0,1]
        self.assertEqual(fib_list(num), result)

    def test_with_2(self):
        num = 4
        result = [0, 1, 1, 2]
        self.assertEqual(fib_list(num), result)

    def test_with_10(self):
        num = 10
        result = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        self.assertEqual(fib_list(num), result)


if __name__ == "__main__":
    unittest.main()
