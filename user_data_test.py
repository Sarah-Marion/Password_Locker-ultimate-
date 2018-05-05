import unittest
from user_data import User


class user_test(unittest.TestCase):
    """
    Test class that defines test cases for the user_data class behaviours
    Args:
        unittest.Testcase: TestCase class that helps in creating test cases
    """

def setUp(self):
    """
    set up method to run each test case
    """
    self.new_user = User("username","password")


def test_init(self):
    """
    test init test case to test if the object is initialized properly
    """
    
    self.assertEqual(self.new_user.username, "username")
    self.assertEqual(self.new_user.password, "password")


if __name__ == "__main__":
    unittest.main()