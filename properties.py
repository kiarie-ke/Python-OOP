class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email  # calls the setter
        self.password = password

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Invalid email address")
        self._email = value.lower().strip()


user1 = User("dantheman", "  kenNNNethmwangi848@gmail.com", "123")
print(user1.email)  # kennethmwangi848@gmail.com

user1.email = "this is not an email"  # raises ValueError