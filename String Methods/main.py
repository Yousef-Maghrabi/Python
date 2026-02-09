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

# run file to understand
print("#############################")
print("### String Methods Part 1 ###")
print("#############################\n\n")
print("### 1. Capitalize String ###\n")
string1 = "python"
print("Capitalized: " + string1.capitalize()) 
print("Original: " + string1 + "\n") # Note didn't change 
print("### 2. Title String ###") 
print("=> means make uppercase of first letter in each word\n") 
string2 = "Hello there I love Python" 
print("Titled: " + string2.title()) 
print("Original: " + string2 + "\n")
print("### 3. Uppercase String ###") 
string3 = "John Doe" 
print("Titled: " + string3.upper()) 
print("Original: " + string3 + "\n")
print("### 3. Uppercase String ###") 
string4 = "JoHn doE" 
print("Titled: " + string4.lower()) 
print("Original: " + string4 + "\n")

print("########################")
print("### String Methods 2 ###")
print("########################\n\n")
# ****************************
print("1. Strip Text") 

# __________________________
string_5 = "   Cat   "; 
 
print(f"Oringinal: |{string_5}|") 

print(f"Trimmed: |{string_5.strip()}|")  

# __________________________
string_6 = "#######dogs#########" 

print(f"Original: {string_6}") 

print(f"Trimmed: {string_6.strip("#")}") 

# __________________________
string_7 = "!@#$%^documents&*()_+-=" 

print(f"Original: {string_7}") 

print(f"Trimmed: {string_7.strip("!@#$%^&*()_+-=)")}\n") 

# ***********************
print("2. Replace Text")  

string_8 = "Today is Monday" 

print(f"Original: {string_8}"); 

print(f"Replaced with Tuesday: {string_8.replace("Monday", "Tuesday")}\n")

# *****************
print("3. Split Text")  

string_9 = "I Love Python"  

print(f"{string_9} consists of {len(string_9.split())} words")

# *********************** 

print("4. Join Iterables") 

list_1 = ["Java", "Python", "Go", "Ruby"]
tuple_1 = ("Java", "Python", "Go", "Ruby") 
dictionary_1 = {"Name": "John", "Age": 30, "Job": "Surgeon"} 

print(f"List: {" - ".join(list_1)}")  
print(f"Tuple: {" - ".join(tuple_1)}") 
print(f"Dictionary: {" - ".join(dictionary_1)}\n")

print("5. Count Repetition of a String in a String") 

string_10 = "last summer i bought a pair of shoes, i have been wearing these shoes since i got these shoes because i love these shoes. I am in love with these shoes"
 
print(f"{string_10}. the word shoes was repeated {string_10.count("shoes")} times") 

string_11 = "I love Python" 

print(f"Python Exists in the text at index: {string_11.find("Python")}")