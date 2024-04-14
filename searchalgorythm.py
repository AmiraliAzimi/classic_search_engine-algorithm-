first_dict = 'In the golden embrace of the sun, love blossoms , dance '
second_dict = 'Hair, Hands, Health: A Triad of Vitality In the tapestry '
third_dict = 'Travel, Summer, Vacation: A Seasonal Odyssey As the sun '

first_key = ['love' , 'sun' , 'dance']
second_key = ['hair' , 'hands' , 'health']
third_key = ['travel' , 'summer' , 'vacation']

count_list = []
for i in first_dict :
    if first_key[0] in first_dict.lower():
        
        count1 = 0
        count1 += 1

    if first_key[1] in first_dict.lower():
        count2 = 0

        count2 += 1
        
    if first_key[2] in first_dict.lower():
        count3 = 0

        count3 += 1
        


for i in second_dict :
    if second_key[0] in second_dict.lower():
        count4 = 0

        count4 += 1
        
    if second_key[1] in second_dict.lower():
        count5 = 0

        count5 += 1
        
    if second_key[2] in second_dict.lower():
        
        count6 = 0

        count6 += 1
        

for i in third_dict :
    if third_key[0] in third_dict.lower():
        count7 = 0 
        count7 += 1
        
    if third_key[1] in third_dict.lower():
         count8 = 0
         count8 += 1
         
    if third_key[2] in third_dict.lower():
         count9 = 0
         count9 += 1
          
count_list.append(count1) 
count_list.append(count2) 
count_list.append(count3) 
count_list.append(count4) 
count_list.append(count5) 
count_list.append(count6) 
count_list.append(count7) 
count_list.append(count8) 
count_list.append(count9) 


row = 3  # Number of rows
Matx = [[] for _ in range(row)]  # Initialize empty Matrix
col = 0
for i in count_list:
    Matx[col].append(i)
    col += 1
    if col == row:
        col = 0

print(Matx)