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
    def find_user(cls, userName, passwrd):
        """
        find_user method that checks if a username already exists
        """
        for user in cls.user_list:
            if user.username == userName:
                return True
            else:
                return False       


    