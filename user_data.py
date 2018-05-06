class User:
    """
    class that generates new instances of users
    """
    def __init__(self, username, password):
        
        self.username = username
        self.password = password
    
    user_list = []


    def save_user(self):
        """
        save_user method saves user object into user_list
        """
        User.user_list.append(self)


    @classmethod
    def user_exists(cls, userName):
        """
        Method that checks if a user exists in the user list.
        Args:
        username: username to search if the user exists
        Returns :
        Boolean: True or false depending if the user exists 
        """
        for user in cls.user_list:
            if user.username == userName:
                return True
            else:
                return False



    @classmethod
    def find_user(cls, userName, passwrd):
        """
        find_user method that checks if a username already exists
        """
        for user in cls.user_list:
            if user.username == userName:
                return True
            else:
                return False  


    @classmethod
    def confirm_user(cls, userName, passwrd):
        """
        confirm_user method that checks if a password matches a username
        """
        for User in cls.user_list:
            if cls.find_user(userName, passwrd):
                password_match = User.password
                if password_match == passwrd:
                    return True
                else:
                    return False
            else:
             return False



    @classmethod
    def change_userpass(cls, userName, new_pass):
        """
        change_userpass method changes a user's password
        """
        for user in cls.user_list:
            if cls.find_user(userName, new_pass):
                user.password = new_pass
                return user
            else:
                return False


    @classmethod
    def user_delete_account(self):
        """
        user_delete_account method that deletes a particular acount
        """
        User.user_list.remove(self)
                           





    