# class User:
#     user_count = 0 #static attribute

#     def __init__(self, username, email):
#      self.username = username
#      self.email = email
#      User.user_count += 1

#      def display_user(self):
#         print(f"Username: {self.username}, Email: {self.email}")
# user1 = User("kenneth", "kennethmwangi848@gmail.com")       
# user2 = User("mwangi", "kiash@gmail.com")
# print(User.user_count)
# print(user1.user_count)
# print(user2.user_count)

# When to use static attributes:

#     Counters
#     Constants
#     Shared config
#     Default values


# @classmethod vs @staticmethod
class BankAccount:
   MIN_BALANCE = 100 #static attribute

   def __init__(self, owner, balance = 0):
      if balance < BankAccount.MIN_BALANCE:
         raise ValueError("Balance below minimum")
      self.owner = owner
      self._balance = balance

   def deposit(self, amount):
      if amount > 0:
         self._balance += amount
         print(f"Deposited {amount}. New balance: {self._balance}") 
      else:    
         print("Invalid deposit amount.")

   def withdraw(self, amount):
     if amount <= 0:
        print("Invalid amount")
     elif self._balance - amount < BankAccount.MIN_BALANCE:
        print("Cannot go below minimum balance")
     else:
        self._balance -= amount
        print(f"Withdrew {amount}. New balance: {self._balance}")          

   @staticmethod     
   def is_valid_interest_rate(rate):
      return 0 <= rate <= 5
   @property
   def balance(self):
    return self._balance
   
account = BankAccount("Alice", 500)
account.deposit(50)
print(BankAccount.is_valid_interest_rate(3))  # True
print(BankAccount.is_valid_interest_rate(6))  # False   