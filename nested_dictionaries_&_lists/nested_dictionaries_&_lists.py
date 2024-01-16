#Starting code
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

#Update values in dictionaries and lists

x = [ [5, 2, 3], [15, 8, 9] ]

students = [
     {'first_name': 'Michael', 'last_name': 'Bryant'},
     {'first_name': 'John', 'last_name': 'Rosales'}
]

sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Andres', 'Ronaldo', 'Rooney']
}

z = [ {'x': 10, 'y': 30} ]

#Iterate through a list of Dictionaries

def iterateDictionary(some_list):
    for dictionary in some_list:
        key_value_pairs = [f"{key} - {value}" for key, value in dictionary.items()]
        print(', '.join(key_value_pairs))

students = [
     {'first_name': 'Michael', 'last_name': 'Bryant'},
     {'first_name': 'John', 'last_name': 'Rosales'}
]
iterateDictionary(students)

#Get values from a list of dictionaries

def iterateDictionary2(key_name, some_list):
    for dictionary in some_list:
        if key_name in dictionary:
            print(dictionary[key_name])
        else:
            print(f"The key '{key_name}' does not exist in the dictionary.")

students = [
     {'first_name': 'Michael', 'last_name': 'Bryant'},
     {'first_name': 'John', 'last_name': 'Rosales'}
]
iterateDictionary2('first_name', students)
iterateDictionary2('last_name', students)

#Iterate through a dictionary with list values

def printInfo(some_dict):
    for key, value_list in some_dict.items():
        print(f"{len(value_list)} {key.upper()}")
        for value in value_list:
            print(value)
        print()

dojo_info = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

printInfo(dojo_info)
