import pyperclip
import string
import random

class Credential:
    """
    class that generates new instances of user credentials
    """
    def __init__(self, profile_name, profile_username = None, profile_email = None, profile_password = None):
        self.profile_name = profile_name
        self.profile_username = profile_username
        self.profile_email = profile_email
        self.profile_password = profile_password
    
    profile_list = []


    def save_profile(self):
        """
        save_profile method saves user object into profile_list
        """
        Credential.profile_list.append(self)



    @classmethod
    def check_profile_exist(cls, profile_name, profile_username = None, profile_email = None):
        """
        check_profile_exist method checks if there is another matching or similar profile
        Args:
            profile to search if it exists
        Returns:
            Boolean: True or false depending if the profile exists
        """
        
        for profile in cls.profile_list:
            if (profile.profile_name == profile_name) or (profile.profile_username == profile_username) or (profile.profile_email == profile_email):
                return True
            else:
                return False 



    @classmethod
    def search_profile(cls, param):
        """
        search_profile method that searches for profile/s based on profile name, username or profile_email
        Args:
            profile to search if it exists
        """

        for profile in cls.profile_list:
            while (profile.profile_name == param) or (profile.profile_username == param) or (profile.profile_email == param):
                return profile


