# --- Python Lists --- # 
# they are used to store multiple items like tuples, sets and dictionaries 

# --- 1. Looping through a list --- # 
print(" --- Looping Through A List --- ")
list = ["a", "b", "c"] 
for i in list : 
    print(i) 
print("\n\n")

# --- 2. Indexing in lists --- # 
print(" --- Indexing in lists --- ")
list = ["a", "b", "c"] 
print(list[0])
print(list[1])
print(list[2])
print(list[-1])
print(list[-2])
print(list[-3])
print("\n\n")

# --- 2. Range in lists --- # 
print(" --- Range in lists --- ")
print(list[0:2]) 
print(list[:]) 
print(list[1:]) 
print(list[::-1])
print("\n\n")

# --- 2. Adding and Removing in lists --- # 
list = ["Banana", "Cherry"] 
list[1:] = ["Apples", "Oranges", "Kiwis"] 
print(list)