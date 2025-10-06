# Ask for the user's name
name = input("What's your name? ")

# Ask how many shoe sizes to convert
how_many = int(input("How many US shoe sizes would you like to convert? "))

# Use a for loop to convert each size
print("Great! Let's convert your sizes, " + name + ".")

for i in range(how_many):
    us_size = float(input("Enter US shoe size #" + str(i + 1) + ": "))
    eu_size = us_size + 33
    print("US size", us_size, "is about EU size", eu_size)

print("All done! Thanks for using the converter,", name)