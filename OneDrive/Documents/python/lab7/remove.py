# Original tuple
my_tuple = ("apple", "banana", "cherry")
item_to_remove = "banana"

# Create a new tuple without the item to remove
new_tuple = my_tuple[0:1] + my_tuple[2:]  # Slicing to exclude the item

# Print both tuples
print("Original tuple:", my_tuple)
print("New tuple:", new_tuple)
