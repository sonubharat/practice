def get_elements(my_tuple):
  """Retrieves the 4th element and 4th element from last of a tuple.

  Args:
      my_tuple: The input tuple.

  Returns:
      A tuple containing the 4th element and the 4th element from last,
      or None if the tuple length is less than 4.
  """

  if len(my_tuple) < 4:
    return None

  # Access the 4th element using positive indexing (starts from 0)
  fourth_element = my_tuple[3]

  # Access the 4th element from last using negative indexing (starts from -1)
  fourth_from_last = my_tuple[-4]

  return fourth_element, fourth_from_last

# Example usage
my_tuple = ("apple", "banana", "cherry", "orange", "mango")
elements = get_elements(my_tuple)

if elements:
  fourth_element, fourth_from_last = elements
  print("4th element:", fourth_element)
  print("4th element from last:", fourth_from_last)
else:
  print("Tuple length is less than 4.")
