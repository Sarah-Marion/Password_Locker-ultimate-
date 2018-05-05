import unittest
import pyperclip
from credential import Credential

class credential_test(unittest.TestCase):
    """
    Test class that defines test cases for the credential class behaviours
    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        """
        set up method to run each test case
        """
        self.new_profile = Credential ("github", "Sarah", "devsarahmarion@gmail.com", "password")


    def test_init(self):
        """
        test init to test if the object is initialized properly
        """    
        self.assertTrue(self.new_profile.profile_name, "github")
        self.assertTrue(self.new_profile.profile_username, "Sarah")
        self.assertTrue(self.new_profile.profile_email,"devsarahmarion@gmail.com")
        self.assertTrue(self.new_profile.profile_password)


    def test_create_new_profile(self):
        """
        test_create_new_profile to test if a new object can be saved
        """
        self.new_profile.save_profile()
        self.assertEqual(len(Credential.profile_list), 1)


    def tearDown(self):
        """
        teardown method that does clean up after each test case has run
        """
        Credential.profile_list = []


    def test_create_multiple_profiles(self):
        """
        test_create_multiple_profiles to test if multiple objects can be saved
        """
        self.new_profile.save_profile()
        test_profile = Credential("facebook", "Marion", "devsarahmarion@gmail.com")
        test_profile.save_profile()
        self.assertEqual(len(Credential.profile_list), 2)




if __name__ == "__main__":
    unittest.main()
