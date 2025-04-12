user_input = input("enter the input String\n")

# Palindrome
#Reverse the String and match with the old String it Should be same.
# 1 by using a traditional method
# 2 Build in functions

def reverse_String (input_String):
    reverse_Str =" "
    for C in input_String:
        reverse_Str = C +reverse_Str
        return reverse_Str # DCBA
    original_Str = "SAI"
    rev_Str = reverse_String(original_Str)
    print(rev_Str)
    if original_Str == rev_Str:
        print("Palindrome")
    else:
        print("It is not")
