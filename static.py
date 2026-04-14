class User:
    user_count = 0 #static attribute

    def __init__(self, username, email):
     self.username = username
     self.email = email
     User.user_count += 1

     def display_user(self):
        print(f"Username: {self.username}, Email: {self.email}")
user1 = User("kenneth", "kennethmwangi848@gmail.com")       
user2 = User("mwangi", "kiash@gmail.com")
print(User.user_count)
print(user1.user_count)
print(user2.user_count)

# When to use static attributes:

#     Counters
#     Constants
#     Shared config
#     Default values