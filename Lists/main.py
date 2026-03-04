# --- Python mylists --- # 
# they are used to store multiple items like tuples, sets and dictionaries 

# --- 1. Looping through a mylist --- # 
print(" --- Looping Through A mylist --- ")
mylist = ["a", "b", "c"] 
for i in mylist : 
    print(i) 
print("\n\n")

# --- 2. Indexing in mylists --- # 
print(" --- Indexing in mylists --- ")
mylist = ["a", "b", "c"] 
print(mylist[0])
print(mylist[1])
print(mylist[2])
print(mylist[-1])
print(mylist[-2])
print(mylist[-3])
print("\n\n")

# --- 2. Range in mylists --- # 
print(" --- Range in mylists --- ")
print(mylist[0:2]) 
print(mylist[:]) 
print(mylist[1:]) 
print(mylist[::-1])
print("\n\n")

# --- 2. Adding and Removing in mylists --- # 
mylist = ["Banana", "Cherry"] 
mylist[1:] = ["Apples", "Oranges", "Kiwis"] 
print(mylist) 
print("\n\n")

# --- 3. Getting Length of a mylist  
mylist = [100, 200, 300, 400, 500] 
print(len(mylist)) 
print("\n\n")

# --- 4. mylist Unpacking 
mylist = ["Apples", "Oranges", "Bananas", "Pears"] 

# --- 4.1 Statically 
apple = mylist[0] 
orange = mylist[1] 
banana = mylist[2] 
pear = mylist[3]
print(f""" 
--- 1st: Static Way
    1st Item: {apple} 
    2nd Item: {orange} 
    3rd Item: {banana} 
    4th Item: {pear} 
    """)
print("\n\n") 

# --- 4.2 Spreading Methond 
apple, orange, banana, pear = mylist
print(f""" 
--- 2nd: Automatic Way
    1st Item: {apple} 
    2nd Item: {orange} 
    3rd Item: {banana} 
    4th Item: {pear} 
    """)
print("\n\n") 
 
# --- 5. mylist Concatenations 

girls = ["Marry", "Susan", "Jennifer"] 
boys = ["Scott", "Robert", "Michael"] 
teachers = ["John", "Rita", "Adam"] 
names = girls + boys + teachers

print(names)
print("\n\n") 

# --- 5. mylist Multiplication 

mylist = ["TEST"] * 10

print(mylist)
print("\n\n") 

# --- 5. list Function 

chars = list("Hello World.")

print(chars)
print("\n\n")  

# --- 6. range Function 

nums = list(range(50, 101)) # list from 50 to 100

print(nums)
print("\n\n")  

# --- 6.1 Even Numbers

nums = list(range(50, 101, 2)) # list from 50 to 100

print(nums)
print("\n\n")  

# --- 6.2 Odd Numbers

nums = list(range(51, 101, 2)) # list from 50 to 100

print(nums)
print("\n\n")   

# --- #################  

# --- Methods
# --- 1. Add Items: append(), insert(), extend() 


# --- Append: Adds an item at the end of a list 
print("# -------------- #")
print("# -------------- #")
print("# -------------- #")
print("# -------------- #")

my_animals = ["goat", "sheep", "cow"] 
pet_animals_new = ["dog", "cat"] 
print(my_animals) 
print(pet_animals_new) 
farm_animal_new = "horse" 
my_animals.append(farm_animal_new) 
my_animals += pet_animals_new 
print(my_animals)  
print("\n\n") 
 
# --- Insert: Adds an item at a specified index 

favourite_subjects = ["Mathematics", "Language", "English"] 
second_favourite = "Science" 
favourite_subjects.insert(1, second_favourite)
print(favourite_subjects) 
print("\n\n") 

# --- Extend: Adds Items in a list or any Iterable 

food = ["Duck", "Rice", "Beef Soup", "Pigeon"]
food.extend({"Fries": "Fried", "Shawerma": "Grilled"})  
print(food)
print("\n\n") 
 
print("# -------------- #")
print("# -------------- #")
print("# -------------- #")
print("# -------------- #")
# 2. Remove Items: pop(), del, remove(), clear() 

# --- pop(): Removes an item at a specified position 

nums = [1, 2, 3, 4, 5] 
nums.pop() # no params => removes the last index 
print(nums)  
nums.pop(2) 
print(nums) # with params = removed the added index 


# 1. Add Items: append(), insert(), extend()