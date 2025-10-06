# Ask for the user's name
name = input("What's your name? ") #Asks for name input

# Ask how many shoe sizes to convert
how_many = int(input("How many US shoe sizes would you like to convert? ")) #Determines how many shoe sizes that the user will input and convert

# Use a for loop to convert each size
print("Great! Let's convert your sizes, " + name + ".") #Utilizes the name variable

for i in range(how_many): #Converts the US shoe size to UK shoe size using the value entered by the user
    us_size = float(input("Enter US shoe size #" + str(i + 1) + ": "))
    eu_size = us_size + 33
    print("US size", us_size, "is about EU size", eu_size) #Prints the converted size


print("All done! Thanks for using the converter,", name) #Signifies the end of the program
