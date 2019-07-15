# task 5
# Create Function that takes two strings as argumenting and return either True or False depending on whether the total no of characters of both string is equal.
def no_of_character(string1,string2):
    length_of_str1 = len(string1)
    length_of_str2 = len(string2)
    if length_of_str1 == length_of_str2:
        return True
    else:
        return False
string1 = input("Enter first string here:")
string2 = input("Enter second string here:") 
print(no_of_character(string1,string2))           