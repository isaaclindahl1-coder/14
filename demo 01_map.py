"""
The map() function is used to apply a given function to every item in a collection
(collections: list, tuple, set, dictionary)
"""


celsius_temps = [0,10,20,30,40]

#convert these all to a list of fahrenheit
#formula (c * 9/5) + 32
# fahrenheit = celsius_temps * 9/5 +32
# print(fahrenheit)
# fahrenheit_temps = [(x*9/5) +32 for x in celsius_temps]

def c_to_f(temp):
    return (temp * 9/5) + 32

fahrenheit_temps = map(c_to_f, celsius_temps)
print(fahrenheit_temps) #map object
#convert map object to a list.
print(list(fahrenheit_temps))

#do the same thing but with a lambda
fahrenheit_temps2 = map(lambda temp: (temp *9/5) + 32, celsius_temps)
print(fahrenheit_temps2) # map object
#covert list
fahrenheit_temps2 = list(fahrenheit_temps2)

# why would we use map?
# - save time, no need for long for loops
# - cleaner code
# - works great with lambda
# - efficient.

names = [
    {"fname": "frank", "lname": "williams", "age": 52},
    {"fname": "david", "lname": "smith", "age": 15},
    {"fname": "jase", "lname": "larkin", "age": 16},
    {"fname": "k", "lname": "luh", "age": 103},
    {"fname": "duane", "lname": "olesnanik", "age": 31}
]

#without list comprehension: Map these names to be lastnameFirstinitial, zero padded age (52, 052, if age were 7, 007
#eg. williamsf052
print(f"{'55'.rjust(3, "0")}") # This is how you Zero pad you use .rjust()
codes = list(map(lambda dict: f"{dict["lname"]}{dict["fname"][0]}{str(dict["age"]).rjust(3,"0")}",names))
 
 
 