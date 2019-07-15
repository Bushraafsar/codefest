#Task 1:you are given the year,and you have to write a function to check if the year is leap or not.
year = int(input("Enter the year!"))
def is_leap(year):
    if year % 4 == 0 :
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    else:
        leap = False 
    return leap
print(is_leap(year))
        
