# Python Tuples
# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
# A tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.
# Tuple items are ordered, unchangeable, and allow duplicate values. 


# ONE: What's not a tuple (Because round brackets don't make it a tuple)
tpl_1 = (1) 
tpl_2 = ("Hello") 
tpl_3 = ([1, 2, 3]) 

print(type(tpl_1)) # <class 'int'>
print(type(tpl_2)) # <class 'str'>
print(type(tpl_3)) # <class 'list'>


# TWO: What's a tuple (Because comma makes it a tuple) 
tpl_4 = (1,) 
tpl_5 = ("Hello",) 
tpl_6 = ([1, 2, 3],) 

print(type(tpl_4)) # <class 'tuple'>
print(type(tpl_5)) # <class 'tuple'>
print(type(tpl_6)) # <class 'tuple'>
 

# THREE: Create a tuple with no brackets 
tpl_7 = 1, 2, 3, 4, 5 # NOT RECOMMENDED (Because it's not clear if it's a tuple or not)
print(type(tpl_7)) # <class 'tuple'> 


# FOUR: Accessing a tuple using indexing 

tpl_8 = ("red", "green", "blue")
# Way one
print(tpl_8[0])
print(tpl_8[1])
print(tpl_8[2])
# Way two
print(tpl_8[-1])
print(tpl_8[-2])
print(tpl_8[-3]) 


# FIVE: Accessing a tupe using slicing 
tpl_color = ("red", "green", "blue", "yellow", "green", "orange")
primary_colors = tpl_color[0:3]
secondary_colors = tpl_color[3:]
print(primary_colors)
print(secondary_colors) 

# SIX: Adding two tuples together 

tpl_9 = (1, 2, 3) 
tpl_10 = (4, 5, 6) 
tpl_11 = tpl_9 + tpl_10 
print(tpl_11)


# SEVEN: Unpacking a tuple 

tpl_12 = ("car", "bike", "plane", "ship") 
(a, b, *c) = tpl_12 
print(a) 
print(b) 
print(c) 


# EIGHT: Check existance in a tuple 

tpl_color = ("red", "green", "blue", "yellow", "green", "orange") 
if "orange" in tpl_color: 
    print("orange is in the tuple") 
else: 
    print("orange is not in the tuple") 


# NINE: Loop through a tuple 

tpl_13 = ("red", "green", "blue", "yellow", "green", "orange") 
for color in tpl_13: 
    print(color)      

# -------- or ----------- 

for color in range(len(tpl_13)) : 
    print(tpl_13[color]) 

    