class animal:
    def speak(self):
        print("all animals are better than humans")

class dog(animal):
    def bark(self):
        print("woof means dog is better than humans")

a=dog()
dog.speak(a)
dog.bark(a)


class parent:
    def land(self):
        print("Has a coconut farmland")

class child(parent):
    def coconut(self):
        print("Child inherits coconut farmland from parent")

c = child()
c.land()
c.coconut()

print("---------------------------")

class cat:
    def sound(self):
        print("cats meow")

class dog_animal:
    def sound(self):
        print("dogs bark")

abc=[cat(), dog_animal()]
for i in abc:
    i.sound()

    #self and () are mandatory otherwise remove both for it to work



class company:
    def comp(self):
        print("This is Gleamator company located in rajajinagar")
        print("This company has 6 employees")

    
class employee:
    def comp(self):
        print("This is Mr. Ramesh, he is an old man in this company")
        print("This person earns about 50 lakhs per year")

c=[company(), employee()]
for i in c:
    i.comp()


#encapsulation

# simple example of encapsulation using bank account
class bank:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive")


    def get_balance(self):
        return self.__balance

account = bank(1000)
print("Initial Balance:", account.get_balance())
account.deposit(500)
print(f"Current Balance: {account.get_balance()}")
