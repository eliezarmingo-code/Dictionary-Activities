
 #Activity 1: Fill in the Blanks
student = {
   "name": "Ana",
   "age": 20,
   "course": "IT"
}

print(student["name"])

#Activity 2: Add and Update
student = {"name": "Ana", "age": 20}
student["grade"] = 95
student.update({"age" : 21})
print(student)



# Activity 3: Loop Through Dictionary
car = {"brand": "Toyota", "model": "Corolla", "year": 2020}
car = {"brand": "Toyota", "model": "Corolla", "year": 2020}
print(car) 


# Activity 4 (Challenge): Mini Phonebook
mini_phonebook = {
    "Tomas" : "09526131978",
    "Lara" : "09520457335",
    "Angel" : "09559353373"
}
name = input("Enter a name:")
if name in mini_phonebook:
     print(f"{name} ‘s number is {mini_phonebook[name]}")
else:
    print("Name not found in mini_phonebook")