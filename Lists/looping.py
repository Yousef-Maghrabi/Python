# 1: Printing through languages  
print(" ### Printing through languages") 
langs = ["HTML", "CSS", "JavaScript", "Python", "Java"] 
for lang in langs: 
    print (lang)   
print("\n\n") 

# 2: Access all items indexed
print(" ### Access all items indexed") 
langs = ["HTML", "CSS", "JavaScript", "Python", "Java"] 
for item in langs: 
    print(langs.index(item))
print("\n\n") 

# 3: Access all items and also indexed  
print(" ### Access all items and also indexed")
langs = ["HTML", "CSS", "JavaScript", "Python", "Java"]  
for item in langs: 
    print(langs.index(item), ":", item) 
print("\n\n")  

# 4: Applications 
print(" ### Application 1 ") 
print("Description: Write a python program to sum all the number of a list of even numbers belong to [0, 100]") 
nums = list(range(0, 101, 2))
nums_sum = 0
for num in nums: 
    nums_sum += num 
print(nums_sum) 
print("\n\n")

print(" ### Application 2 ") 
print("Description: Write a python program to sum all the number of a list of odd numbers belong to [0, 100]") 
nums = list(range(1, 101, 2))
nums_sum = 0
for num in nums: 
    nums_sum += num 
print(nums_sum) 
print("\n\n")

print(" ### Application 3 ") 
print("Description: Write a python program to get product of all the number of a list of numbers belong to [0, 10]") 
nums = list(range(1, 11))
nums_product = 1
for num in nums: 
    nums_product *= num 
print(nums_product) 
print("\n\n")

print(" ### Application 4 ") 
print("Description: Write a python program to get max of a list") 
nums = [1, 2233, 343, 434, 33, 3, 5, 6654, 234, 5, 7, 234, 566, 574 , 6666, 64656, 990] 
nums_max = nums[0]
for num in nums: 
    if num > nums_max: 
        nums_max = num
print(nums_max) 
print("\n\n")

print(" ### Application 5 ") 
print("Description: Write a python program to get min of a list") 
nums = [1, 2233, 343, 434, 33, 3, 0, 5, 6654, 234, 5, 7, 234, 566, 574 , 6666, 64656, 990] 
nums_min = nums[0]
for num in nums: 
    if num < nums_min:  
        nums_min = num
print(nums_min) 
print("\n\n")

print(" ### Application 6 ") 
print("Description: Write a python program to get average of a list") 
nums = [1, 2233, 343, 434, 33, 3, 0, 5, 6654, 234, 5, 7, 234, 566, 574 , 6666, 64656, 990] 
nums_sum = 0  
for i in nums: 
    nums_sum += num 
nums_average = nums_sum / len(nums)
print(nums_average) 
print("\n\n")