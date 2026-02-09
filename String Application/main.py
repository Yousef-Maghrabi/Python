long_string = "William Shakespeare was an English playwright, poet and actor. He is widely regarded as the greatest writer in the English language and the world's greatest dramatist. He is often called England's national poet. His extant works, including collaborations" 
arr = []

for char in long_string: 
    if char.isalpha(): 
        arr.append(char.lower()) 

counter_list = [] 

for index in arr: 
    if index not in counter_list: 
        counter_list.append(index) 
        counter_list.append(arr.count(index))

for item in counter_list: 
    if item: 
        letter_index = counter_list.index(item)
        if(letter_index % 2 == 0): 
            print(f"{item} : {counter_list[letter_index + 1]}")
