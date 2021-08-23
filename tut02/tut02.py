def get_memory_score(input_nums):
    score_gained = 0
    current_storage = []
    for inputs in input_nums : 
        exist_count = current_storage.count(inputs)
        if exist_count > 0 :
            score_gained=score_gained+1
        else :
            if len(current_storage)==5:
                current_storage.pop(0)
                current_storage.append(inputs)
            else:
                current_storage.append(inputs)
    print('Score: {0}'.format(score_gained))
    
input_nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
invalid_items=[]
for items in input_nums:
        if type(items)!=int : 
            invalid_items.append(items)
if len(invalid_items) >0 :
        print("Please enter a valid input list. Invalid inputs detected",invalid_items)
else:
        get_memory_score(input_nums)