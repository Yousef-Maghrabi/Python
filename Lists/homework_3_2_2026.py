# Task 1: 
# Print Integers between 0 and 100 that are divisable by 5

int_from_0_to_100 = list(range(0, 101))
list_1 = []

print("List of Integers divisable by 5: ")
for i in int_from_0_to_100: 
    if i % 5 == 0: 
        list_1.append(i) 


print(list_1)
print("\n\n")

# Task 2: 
# Print Integers between 0 and 100 that are divisable by 6

print("List of Integers divisable by 6: ")
list_2 = []

for i in int_from_0_to_100: 
    if i % 6 == 0: 
        list_2.append(i) 


print(list_2)
print("\n\n")

# Task 3: 
# Print Integers between 0 and 100 that are divisable by 7

print("List of Integers divisable by 7: ")
list_3 = []

for i in int_from_0_to_100: 
    if i % 7 == 0: 
        list_3.append(i) 


print(list_3)
print("\n\n")

# Task 4: 
# Print Integers between 0 and 100 descendingly  

print("List of Integers between 0 and 100 descendingly") 

print(int_from_0_to_100[::-1])