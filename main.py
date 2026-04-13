class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def bark(self):
        print("Whoof whoof")

class Owner:
    def __init__(self, name, address, contact_number):
        self.name = name
        self.address = address
        self.phone_number = contact_number

owner1 = Owner("Kelvin", "1234", "0758263468")
dog1 = Dog("Kenneth", "Garman", owner1)
print(dog1.owner.name)

owner2 = Owner("omollo", "2344", "07992084u")
dog2 = Dog("Kiash", "brush", owner2)
print(dog2.owner.name)