#Create a class "possible palindrome" and a class method "checking_palindrome" that determine whether it is possible to build a palindrome from the character in string.
class possible_palindrome():
    def __init__(self,str1):
        self.str1 =  str1
    def checking_palindrome(self):
        rev = self.str1[::-1]
        if rev == self.str1:
            print("Can make the following palindrome:",rev) 
        else:
            print("Can't be a palindrome! ") 
obj1 = possible_palindrome("aabaa") 
obj2 = possible_palindrome("ppppop")
obj3 = possible_palindrome("pop")

obj1.checking_palindrome() 
obj2.checking_palindrome() 
obj3.checking_palindrome() 



