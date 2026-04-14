
from datetime import datetime
class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password



    def get_email(self):
        print(f"Email accessed at {datetime.now()}")
        return(self._email)    
    def set_email(self, new_email):
        self._email = new_email

    # def clean_email(self):
    #         return self._email.lower().strip()
    # def say_hi_to_user(self, user):
    #     print(
    #         f"Sending message to {user.username}: Hi {user.username}, it's {self.username}"
    #     )
    
user1 = User("dantheman", "  KENNethmwangi848@gmail.com", "123")
print(user1.get_email())


# user1._email = "1234546767"
user1.set_email("kennehj")
print(user1.get_email())
# print(user1.__email)
# print(user1.clean_email())
# user2 = User("kiash", "kiash1232@gmail.com", "123")

# user1.say_hi_to_user(user2)
# print(user1._email)
# user1.email = "danny@gmail.com"
# print(user1.email)

# Accesssing and Modifing data:
# 1. the traditional way: making the data pprivate and use getters and setters:


# the "Consenting Adults" Philosofy
