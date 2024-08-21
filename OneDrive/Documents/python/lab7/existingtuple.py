my_tuple = ("apple", "banana", "cherry")
element_to_check = "banana"

if element_to_check in my_tuple:
  print("Yes,", element_to_check, "is in the tuple.")
else:
  print("No,", element_to_check, "is not in the tuple.")



my_tuple = ("apple", "banana", "cherry")
element_to_check = "orange"
found = False

for item in my_tuple:
  if item == element_to_check:
    found = True
    break  # Exit the loop once the element is found

if found:
  print("Yes,", element_to_check, "is in the tuple.")
else:
  print("No,", element_to_check, "is not in the tuple.")
