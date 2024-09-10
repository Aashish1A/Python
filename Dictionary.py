"""dict={
    "name" : "Aashish",
    "cgpa" : 9.0,
    "marks" : [98,97,95],
}
print(type(dict)) # checking type
print(dict)
print(dict["name"]) # Accesing name and marks in dictionary
print(dict["marks"])
dict["marks"] = "python is a good programming language for beginners." #Replace value in dictionary
dict["surname"] = "kumar" # we can add something in  dictionary.
print(dict)"""

# Nested dictionary

"""student = {
    "name" : "Aashish",
    "subjects" : {
        "phy" : 98,
        "chem" : 95,
        "math" : 68,
    }
}
print(student)
print(student["subjects"])"""

# Dictionary methods

"""mydict={
    "name" : "Aashish",
    "cgpa" : 9.0,
    "marks" : [98,97,95],
}
print(len(mydict))
print(len(list(mydict.keys())))
print(mydict.keys())

print(mydict.values())
print(list(mydict.values()))

print(list(mydict.items()))
print(mydict.items())

print(mydict["name"])
print(mydict.get("cgpa"))

new_dict = {"city" : "patna"}
mydict.update(new_dict)
print(mydict)
mydict.update({"city" : "Patna"})
print(mydict)

a=45
b=35
sum = a+b
print(sum)"""

# Write a program in python to stores the word.

"""stories = {
    "table" : ["a piece of furniture" , "list of facts & figures"],
    "cat" : "a small animal"
}

print(type(stories))
print(stories)"""

# You are given a list of subjects for students. Assume one classroon is required for 1 sujects. How many classrooms are needed by all students.
# "python","java","c++","python","javascripr","java","python","java","c++","c"

"""subjects = {
    "python", "java", "c++","python","javascript",
    "java","python","java","c++","c"
}

print(len(subjects))"""

# Wap to enter marks of 3 subjects from the user and store them in a dictionary. 
# Start with an empty dictionary & add one by one. Use subject name as key & marks as variable.

marks = {}

x = int(input("Enter physics : "))
marks.update({"physics" : x})

x = int(input("Enter chem : "))
marks.update({"chem" : x})

x = int(input("Enter math : "))
marks.update({"math" : x})

print(marks)




