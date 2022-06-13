"""
1. Update Values in Dictionaries and Lists:
    1. Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
    2. Change the last_name of the first student from 'Jordan' to 'Bryant'
    3. In the sports_directory, change 'Messi' to 'Andres'
    4. Change the value 20 in z to 30
"""

# Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].
x = [ [5,2,3], [10,8,9] ] 

x[1][0] = 15
print(x)



# Change the last_name of the first student from 'Jordan' to 'Bryant'
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]

students[0]["last_name"] = "Bryant"
print(students)



# In the sports_directory, change 'Messi' to 'Andres'
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

sports_directory["soccer"][0] = "Andres"
print(sports_directory)



# Change the value 20 in z to 30
z = [ {'x': 10, 'y': 20} ]

z[0]["y"] = 30
print(z)




"""
2. Iterate Through a List of Dictionaries
Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value.

For example, given the following list:

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

iterateDictionary(students) 

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel

"""

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


# output - each key-value pair ends up on 2 separate lines
def iterateDictionary(some_list):
    for i in range(len(some_list)):
        for key in some_list[i].keys():
            print(key, some_list[i][key])

# bonus
def iterateDictionary(some_list):
    for i in range(len(some_list)):
        name1 = []
        for key in some_list[i].keys():
            name1.append(key)
            name1.append(some_list[i][key])
        # print(name1) checking output
        print(f"{name1[0]} - {name1[1]}, {name1[2]} - {name1[3]}")

iterateDictionary(students) 



"""
3. Get Values From a List of Dictionaries
Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary. 

For this giving list:

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]


iterateDictionary2('first_name', students) should output:
Michael
John
Mark
KB

And iterateDictionary2('last_name', students) should output:
Jordan
Rosales
Guillen
Tonel

"""

def iterateDictionary2(key_name, some_list):
    for ls in some_list:
        print(ls[key_name])


students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

iterateDictionary2('first_name', students)

iterateDictionary2('last_name', students)



"""
4. Iterate Through a Dictionary with List Values
Create a function printInfo(some_dict) that given a dictionary whose values are all lists, prints the name of each key along with the size of its list, and then prints the associated values within each key's list. 

For example:

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)

# output:
7 LOCATIONS
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
8 INSTRUCTORS
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon
"""


def printInfo(some_dict):
    for key, val in some_dict.items():
        val_length = len(some_dict[key])
        key_name = key.upper()

        print(val_length, key_name)     # print name of each key along with the size of its list

        for i in range(val_length):
            print(some_dict[key][i])    # prints the associated values within each key's list


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo)
