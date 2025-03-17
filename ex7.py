#Print students' name.
#Auther: Yang Yue

# This program creates a list of names and prints each with the last name Evans
# Then asks the user to add another name and prints the updated list

# Initial list of names
studentNames = ["Lisa", "Liam", "Leo", "Larry", "Linda"]

# Print each name with last name Evans
print("Original list:")
for name in studentNames:
    print(f"{name} Evans")

# Ask user to add another name
new_name = input("\nPlease enter another name to add to the list: ")

# Add the new name to the list
studentNames.append(new_name)

# Print the updated list
print("\nUpdated list:")
for name in studentNames:
    print(f"{name} Evans")
