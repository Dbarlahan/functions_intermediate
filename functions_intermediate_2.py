# Update Values in Dictionaries and Lists

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
# Change the last_name of the first student from 'Jordan' to 'Bryant'
# In the sports_directory, change 'Messi' to 'Andres'
# Change the value 20 in z to 30

x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


def value():
    x[1][0] = 15
    return x
print(value())


def last_name():
    students[0]['last_name'] = 'Bryant'
    return students[0]
print(last_name())


def soccer():
    sports_directory['soccer'][0] = 'Andres'
    return sports_directory['soccer']
print(soccer())


def value():
    z[0]['y'] = 30
    return z
print (value())

# Iterate Through a List of Dictionaries

# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:

students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    for curr_dict in some_list:
        display_str = ""
        for curr_key in curr_dict.keys():
            display_str += f"{curr_key} - {curr_dict[curr_key]}, "
    # remove comma and extra space from display_str
        display_str = display_str[:len(display_str) - 2]
        print(display_str)
iterateDictionary(students)

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

# Get Values From a List of Dictionaries

# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary.

# For example, iterateDictionary2('first_name', students) should output:

# Michael
# John
# Mark
# KB

# And iterateDictionary2('last_name', students) should output:

# Jordan
# Rosales
# Guillen
# Tonel

def iterateDictionary2(key_name, some_list):
    for curr_dict in some_list:
        print (curr_dict[key_name])

iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

# Iterate Through a Dictionary with List Values

# Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. For example:

# output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank

# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(some_dict):
    for key in some_dict.keys():
        print(f'{len(some_dict[key])} {key.upper()}')
        for item in some_dict[key]:
            print(item)
        print('\n')
printInfo(dojo)