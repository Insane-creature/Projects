# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Overrites everything
with open("my_file.txt", mode="w") as file:
    file.write("New text.")

# Append the file
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")

# Creating new file
with open("new_file.txt", mode="w") as file:
    file.write("Creating through python, is fun.")