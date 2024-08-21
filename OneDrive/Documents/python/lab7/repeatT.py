def find_repeated_items(my_tuple):
  """Finds the repeated items in a given tuple.

  Args:
      my_tuple: The input tuple.

  Returns:
      A list containing the repeated items (without duplicates).
  """

  repeated_items = []
  seen_items = set()  # Use a set for efficient membership checking

  for item in my_tuple:
    if item in seen_items:
      repeated_items.append(item)
    else:
      seen_items.add(item)

  return repeated_items

# Example usage
my_tuple = (2, 4, 5, 6, 2, 3, 4, 4, 7, 8, 4, 3, 2)
repeated_items = find_repeated_items(my_tuple)

if repeated_items:
  print("Repeated items:", repeated_items)
else:
  print("No repeated items found in the tuple.")
