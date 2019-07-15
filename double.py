# Task 10
# python function that remove dublicates values from the list:
import collections
lst = ["Ahmed","Sana","Mujtuba","Ahmed","Iqrar","Bushra","Iqrar","Aliyan"]
def remove_dublicate(lst):
    lst = collections.Counter(lst)
    for i,j in lst.items():
        if j == 2:
            j = j - 1    
        else:
            j = j
    lst = list(lst)   
    print(lst) 
remove_dublicate(lst)            

