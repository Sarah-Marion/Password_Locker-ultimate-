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


    def test_profile_exist(self):
        """
        test_profile_exist to check if there is another matching or similar profile
        """
        test_profile1 = Credential("twitter", "Marion", "devsarahmarion@gmail.com")    
        test_profile1.save_profile()
        profile = test_profile1.check_profile_exist("twitter", "Marion", "devsarahmarion@gmail.com")
        self.assertTrue(profile)


    def test_search_profile(self):
        """
        test_search_profile to test if a user can be able to search for a profile_email
        """
        test_profile1 = Credential("twitter", "Marion", "devsarahmarion@gmail.com")
        test_profile1.save_profile()    
        search_result = test_profile1.search_profile("twitter")
        self.assertEqual(test_profile1, search_result)
  


    def test_delete_profile(self):
        """
        test_delete_profile to test if a user can delete a specific profile
        """
        test_profile1 = Credential("twitter", "Marion", "devsarahmarion@gmail.com")
        test_profile1.save_profile()
        test_profile1.delete_profile()
        self.assertEqual(len(Credential.profile_list), 0)



    # def test_display_all_profiles(self):
    #     """
    #     test_display_all_profiles to test if a user can view all their profiles
    #     """
    #     self.assertEqual(Credential.display_profiles(), Credential.profile_list)

    def test_copy_credentials(self):
        """
        test copy_credentials to test if a user can be able to copy an item to the clipboard
        """
        test_profile1 = Credential("twitter","Marion","devsarahmarion@gmail.com","testPassword")
        test_profile1.save_profile()
        Credential.copy_credentials("twitter")
        self.assertEqual(test_profile1.profile_password,pyperclip.paste())


    def test_generate_random_password(self):
        """
        test_generate_random_password to test if a user can generate a random password with a set length
        """
        test_profile1 = Credential("Marion","devsarahmarion@mail.com")
        generated_password = test_profile1.generate_random_password
        test_profile1.profile_password = generated_password
        test_profile1.save_profile()
        self.assertTrue(test_profile1.profile_password)
    
    

if __name__ == "__main__":
    unittest.main()
