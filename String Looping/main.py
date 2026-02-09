print("### String Looping ###") 
 
string_1 = "hello"  
print("# Starting Example 1...")
for letter in string_1: 
    print(letter) 
print("# Executed Example 1!\n") 

print("# Starting Example 2...")
for letter in string_1:
    print(letter * 2)
print("# Executed Example 2!\n") 

print("# Starting Example 3...")
for num in range(len(string_1)):
    print(string_1[num])
print("# Executed Example 3!\n") 

print("# Starting Example 4...")
for num in range(len(string_1)):
    print(string_1[num] * (num + 1))
print("# Executed Example 4!\n") 

print("# Starting Example 5...")
for num in range(len(string_1)):
    print(string_1[num].replace(string_1[num], "#") * (num + 1))
print("# Executed Example 5!\n") 

print("# Program Ended! ")