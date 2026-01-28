# String methods 
print("###### String Methods ######")
# 1. length
print(len("Hello World")) # 11 
# 2. search using in  
print("H" in "Hello World") # true 
print("h" in "Hello World") # false 

# using search string method in a conditional 
gender = "male"
if ("male" in gender) : 
    print("Character is a male") 
else : 
    print("Character is a female") 

# excluding search string 
password = "myPaSs129@$"
print(" " not in password)

username = "Yousef Maghrabi" 
if ("+" not in username) : 
    print("Good Username") 
else : 
    print("Bad Username") 

# slicing a string 
# Note you can slice from a specific point till end without including the last index
 
string = "foo bar"  
print(string[:3]) # foo 
print(string[4:]) # bar
print(string[-3: -1]) # ba 

"""
exercise: 
1* store 'www.google.com '
2* print 'www'
3* print 'google'
4* print '.com' 
"""  

exercise_string = "www.google.com" 
subdomain = exercise_string[:3] # www
domain = exercise_string[4:10] ## google 
ext = exercise_string[10:] # .com 

print(subdomain+"."+domain+ext) # www.google.com