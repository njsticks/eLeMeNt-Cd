def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

def sqrt(x, y = 0.5):
    return x ** y

class User_id():
    def __init__(self, name, surname, age, business, email):
        self.name = name
        self.surname = surname
        self.age = age
        self.business = business
        self.email = email

print("\n")

user = User_id("John", "Michael", 67, "RemoteIndustries", "rindustries@ret.ls")

print(" Name:    ", user.name,"\n", "Surname:", user.surname,"\n", "Age:      ", user.age, "\n", "Business:", user.business, "\n", "Email:    ",user.email, "\n")

edit = int(input("To Edit Your Profile Press '1', Else Press '0': "))

print("\n")

if edit == 1:
    user.name = input("Name:  ")
    user.surname = input("Surname: ")
    user.age = input("Age:  ")
    user.business = input("Business: ")
    user.email = input("Email: ")

    print("\n")
    print("Thank You for Signing up", user.name, user.surname, "Here's Your Business ID", "\n")
    print(" Name:     ", user.name,"\n", "Surname: ", user.surname, "    ","\n", "Age:       ", user.age, "\n", "Business: ", user.business, "\n", "Email:     ",user.email, "\n")

else:
    print("Thank You for Logging in", user.name, user.surname, "Here's Your Business ID", "\n")
    
    print(" Name:    ", user.name,"\n", "Surname:", user.surname,"\n", "Age:      ", user.age, "\n", "Business:", user.business, "\n", "Email:    ",user.email, "\n")
