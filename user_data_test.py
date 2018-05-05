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


    def test_create_new_account(self):
        """
        test_create_new_account test case to test if the new user object is
        saved into the user list
        """

        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)


    def tearDown(self):
        """
        teardown method that does clean up after each test case has run
        """
        User.user_list = []


    def test_check_user_exist(self):
        """
        test_check_user_exist to test if a user exists or not
        """
        self.test_user = User("username", "password1")
        self.test_user.save_user()
        found_user = User.find("username")
        self.assertTrue(found_user)




if __name__ == "__main__":
    unittest.main()