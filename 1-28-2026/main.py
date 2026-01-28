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