# Method 1: Using string formatting (f-strings)
my_tuple = ("apple", "banana", "cherry")
colon_separated = f"{' : '.join(my_tuple)}"  # Join elements with ': '
print(colon_separated)  # Output: apple : banana : cherry

# Method 2: Using the join() method with a custom separator
separator = ": "
colon_separated = separator.join(my_tuple)
print(colon_separated)  # Output: apple: banana: cherry

my_tuple = ("apple", "banana", ":", "cherry")
print(my_tuple)  # Output: ('apple', 'banana', ':', 'cherry')

my_list = ["apple", "banana"]
my_list.append(":")  # Add the colon element dynamically
my_list.append("cherry")
print(my_list)  # Output: ['apple', 'banana', ':', 'cherry']

# You can modify elements in a list:
my_list[0] = "orange"
print(my_list)  # Output: ['orange', 'banana', ':', 'cherry']
