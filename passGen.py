import string
import random

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    # Including all lowercase alphabets into a string
    s2 = string.ascii_uppercase
    # Including all uppercase alphabets into a string
    s3 = string.digits
    # Including all digits into a string
    s4 = string.punctuation
    # Including all characters into a string
    plen = int(input("Enter password length\n")) #Todo1: Handle Gibberish
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
   
    random.shuffle(s)
    # A function that would shuffle the elements of list s
    print("Your password is: ")
    
    print("".join(s[0:plen]))