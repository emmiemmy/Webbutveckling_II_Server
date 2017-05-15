#=========
#Uppgift 1

#Function prints every number up until given number in parameter, starting from 1
def printNumbers(num):
	for i in range(1, num +1):
		print(i)

#Testing function above
print("Testing Uppgift 1")

printNumbers(5)



#=========
#Uppgift 2
#Function tries if given number in parameter is diviseable with 3, 5 or neither
def fooBar(num):
	res = ""
	for i in range(1, num+1):
		res = i
		if i % 3 == 0:
			res="Foo"
		if i % 5 == 0:
			res ="Bar"
		if i % 3 == 0 and i % 5 == 0:
			res = "FooBar"
		print(res)

#Testing function above
print("Testing Uppgift 2")

fooBar(15)


#=========
#Uppgift 3

#Function returns the average of numbers in given list
def calculate_average(num):
	return sum(num) / len(num)

#Testing function above
print("Testing Uppgift 3")

numbers = [2,4,6,8]

average = calculate_average(numbers)

print(average)



#=========
#Uppgift 4
#Function returns a list of names that fulfills the minimum amount of characters given in parameter.
def filter_names_by_length(list, minLength):
	res = []
	for elem in list:
		if len(elem) > minLength:
			res.append(elem)
	return res

#Testing the function above
print("Testing Uppgift 4")

names = ["Emma", "Johanna", "Elizabet", "Joe", "Watson"]
# All names that have more then 4 characters
names_above_4 = filter_names_by_length(names, 4)
print(names_above_4) # => ["Johanna", "Elizabet", "Watson"]

# All names that have more then 6 characters
names_above_6 = filter_names_by_length(names, 6)
print(names_above_6) # => ["Elizabet", "Johanna"]


#=========
#Uppgift 5

# Dictionary
myself = {
	"firstname" : "Emma",
	"lastname" : "Shakespeare",
	"age" : 17,
	"top_3_movies" : ["Heat", "Gone Girl", "Catch me if you can"]
}

#Testing function above
print("Testing Uppgift 5")
# Firstname - String
print(myself["firstname"])

# Lastname - String
print(myself["lastname"])

# Age - Integer
print(myself["age"])

# Movies - List
print(myself["top_3_movies"])

#=========
#Uppgift 6

#Function prints dictionary values in formatted string
def printPerson(p):
	movies = ", ".join(p["top_3_movies"])
	print(p["firstname"] + " " + p["lastname"] + \
		" (" + str(p["age"]) + "), " + "Top Movies: " + movies )

#Testing function above
print("Testing Uppgift 6")

printPerson(myself)


#=========
#Uppgift 7
#Function takes in values and creates a dictionary with given parameters
def createPerson(first, last, age, movie_list):
	newPerson = {
	"firstname" : first,
	"lastname" : last,
	"age" : age,
	"top_3_movies" : movie_list
	}
	return newPerson

""" Test the function above 
Create a new dictionary from the arguments"""
print("Testing Uppgift 7")

sherlock = createPerson("Sherlock", "Holmes", 35, ["Seven", "Gone Girl", "The Prestige"])

printPerson(sherlock)














