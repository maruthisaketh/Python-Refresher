#Variables, Loops, Conditions, Functions, Lists, Dictionaries, Sets, Tuples, 
#Strings, File Handling, Classes and Objects, Inheritance, Polymorphism, 
#Encapsulation, Abstraction, Modules and Packages, Exception Handling, Regular Expressions, 
#Lambda Functions, Map, Filter, Reduce, Decorators, Generators, Iterators


# Variables
x = 5
y = "Hello, World!"

# Loops
for i in range(5):
    print(i)

while x > 0:
    print(x)
    x -= 1

# Conditions
if x > 0:
    print("x is positive") 
elif x < 0:
    print("x is negative")
else:
    print("x is zero")

# Functions
def greet(name):
    return f"Hello, {name}!"
print(greet("Alice"))

# Lists
my_list = [1, 2, 3, 4, 5]
print(my_list[0])  # Output: 1
# Dictionaries
my_dict = {"name": "Alice", "age": 30}
print(my_dict["name"])  # Output: Alice

# Sets
my_set = {1, 2, 3, 4, 5}
print(3 in my_set)  # Output: True

# Tuples
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])  # Output: 1

# Strings
my_string = "Hello, World!"
print(my_string.upper())  # Output: HELLO, WORLD!

# File Handling
with open("example.txt", "w") as file:
    file.write("This is an example file.")

# Classes and Objects
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Creating an object of the Person class
person1 = Person("Alice", 30)
print(person1.greet())  # Output: Hello, my name is Alice and I am 30 years old.

# Inheritance
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        return f"{self.name} is studying."
    
# Creating an object of the Student class
student1 = Student("Bob", 20, "S12345")
print(student1.greet())  # Output: Hello, my name is Bob and I am 20 years old.
print(student1.study())  # Output: Bob is studying.

# Polymorphism
class Animal:
    def speak(self):
        return "Animal speaks"
class Dog(Animal):
    def speak(self):
        return "Woof!"
class Cat(Animal):
    def speak(self):
        return "Meow!"
animals = [Dog(), Cat()]
for animal in animals:    print(animal.speak())  # Output: Woof! Meow!

# Encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance  
account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())  # Output: 1500
account.withdraw(200)
print(account.get_balance())  # Output: 1300
