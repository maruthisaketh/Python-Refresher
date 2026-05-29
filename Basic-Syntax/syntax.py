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

# Abstraction
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius
rectangle = Rectangle(4, 5)
print(rectangle.area())  # Output: 20
print(rectangle.perimeter())  # Output: 18
circle = Circle(3)
print(circle.area())  # Output: 28.26
print(circle.perimeter())  # Output: 18.84

# Modules and Packages

# Importing the module
import math_utils
print(math_utils.add(5, 3))  # Output: 8
print(math_utils.subtract(5, 3))  # Output: 2

# Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Regular Expressions
import re
pattern = r'\d+'  # Matches one or more digits
text = "The price is 100 dollars"
matches = re.findall(pattern, text)
print(matches)  # Output: ['100']


# Lambda Functions
square = lambda x: x ** 2
print(square(5))  # Output: 25

# Map, Filter, Reduce
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(square, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4]

from functools import reduce
product = reduce(lambda x, y: x * y, numbers)
print(product)  # Output: 120

# Decorators
def decorator1(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper
@decorator1
def say_hello():
    print("Hello!")
say_hello()

# Generators
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
for number in count_up_to(5):
    print(number)  # Output: 1 2 3 4 5
    
# Iterators
my_list = [1, 2, 3]
my_iterator = iter(my_list)
print(next(my_iterator))  # Output: 1
print(next(my_iterator))  # Output: 2
print(next(my_iterator))  # Output: 3
