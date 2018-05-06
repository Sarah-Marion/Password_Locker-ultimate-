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


    def test_check_user_exists(self):
        """
        test_check_user_exists to test if a user exists or not
        """
        self.new_user.save_user()
        test_user = User("username", "password1")
        test_user.save_user()
        user_exists = User.user_exists("username")
        self.assertTrue(user_exists)


    def test_username_match_password(self):
        """
        test_username_match_password to test if a password matches a username
        """
        self.test_user = User("username", "password1")   
        self.test_user.save_user()
        confirm_user_exist = User.confirm_user("username", "password1")
        self.assertTrue(confirm_user_exist)


    def test_user_change_password(self):
        """
        test_user_change_password to test if a user can alter their password
        """
        test_alter = User("username", "password1")
        test_alter.save_user()
        change_passwrd = test_alter.change_userpass("username", "password03")
        self.assertEqual(change_passwrd.password, "password03")

    
    
    def test_user_delete_account(self):
        """
        test_user_delete_account to test if a user can delete their account
        """
        self.test_user = User("username", "password1")   
        self.test_user.save_user()
        self.test_user.user_delete_account()
        self.assertEqual(len(User.user_list), 0)


if __name__ == "__main__":
    unittest.main()