class A:
    def _init_(self, name):
        self.name = name
    
    def greet(self):
        print("Hello,", self.name)

# Creating objects of class A with constructor
obj1 = A("Alice")
obj2 = A("Bob")

# Accessing object attributes and methods
print(obj1.name)  # Output: Alice
obj1.greet()      # Output: Hello, Alice

print(obj2.name)  # Output: Bob
obj2.greet()      # Output: Hello, Bob