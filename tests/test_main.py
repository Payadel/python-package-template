import unittest

from package_name.main import say_hello


class TestMain(unittest.TestCase):
    """ Test main.py """

    def say_hello_give_name_get_str(self):
        """ Test say hello function """
        name = "Hamid"

        result = say_hello(name)
        expected = f"Hello {name}!"

        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
