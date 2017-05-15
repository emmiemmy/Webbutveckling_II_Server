#=========
#Uppgift 1

print(5 * 2 < 12)
print(55 != 22)
print(16 / 4 == 4)
print(8 + 2 <=  128)
print(32 * 8  > 255)

#=========
#Uppgift 2
# The name
name = "Sherlock Holmes"
# Number of characters
num_of_chars = len(name)
# Print the number of characters
print(num_of_chars)


#=========
#Uppgift 3
part_1 = "The area of a Triangle with a width of "
part_2 = 12
part_3 = " and a height of "
part_4 = 8
part_5 = " is: "
# Calculate the area with the variables part_2
# and part_4 (the area is: height * width / 2)
part_6 = part_4 * part_2 / 2

#Concatenate string and ints
all_parts = part_1 + str(part_2)
all_parts += part_3 + str(part_4) + part_5 + str(part_6)
print(all_parts)


#=========
#Uppgift 4

#Part 1
#Create strings
day = "Tisdag"
dinner = "Hamburgare"
threat = "I'll be back"

#Get a slice of the string
print(day[:3]) # => 'Tis'
print(dinner[3:]) # => 'burgare'
print(threat[-7:]) # => 'be back'

#Part 2
#create strings
platform = "It's Learning"
title = "Python: The Good Parts"

#get a slice of the string and convert to upper/lower case
print(platform[5:].upper()) # => 'LEARNING'
print(title[-10:].lower()) # => 'good parts'


#=========
#Uppgift 5
def calculate_triangle_area(width, height):
    return width * height /2

# Store the height and width in variables
# then calculate the area and finally print it
width = int(input("Please enter width: ")) # Using python 3.5 conversion is needed
height = int(input("Please enter height: "))
area = calculate_triangle_area(width, height)
print(area)



#=========
#Uppgift 6
#Function returns largest number of two given ones
def max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
#Function returns smallest number of two given ones
def min(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2

# Max
print(max(12, 17)) # => 17
print(max(15, 15)) # => 15
print(max(20, 3)) # => 20

# Min
print(min(12, 17)) # => 12
print(min(15, 15)) # => 15
print(min(20, 3)) # => 3




#=========
#Uppgift 7

#Function returns true if number given is even, otherwise it returns false
def isEven(number):
    if number % 2 == 0:
        return True
    else:
        return False

#Testing function above:
print(isEven(10)) # => True
print(isEven(17)) # => False

print("Goodbye!")
