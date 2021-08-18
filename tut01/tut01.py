

def meraki_helper(n): 
    """This will detect meraki number""" 
    digits = [] 
    if n==0: return True
    if n//10==0: return True 
    cnt=0;    
    while n: 
        cnt+=1
        remaining_number=n//10        
        digits.append(n%10) 
        n=remaining_number 
        
    cur_pos=0 
    next_pos=1 
    while next_pos<cnt: 
        if abs(digits[next_pos]-digits[cur_pos])==1:  
          cur_pos=next_pos
          next_pos+=1; 
        else:
          return False

    return True         
 
 
input = [12, 14, 56, 78, 98, 54, 678, 134, 789, 0, 7, 5, 123, 45, 76345, 987654321] 
meraki=non_meraki=0 
 
for number in range(len(input)): 
    if meraki_helper(input[number])==True: 
        meraki=meraki+1 
        print("Yes - {0} is a Meraki number".format(input[number])) 
    else: 
        non_meraki=non_meraki+1 
        print("No - {0} is not a Meraki number".format(input[number]))     
 
print("the input list contains {0} meraki and {1} non meraki numbers".format(meraki,non_meraki))
