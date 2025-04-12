original = "SAI"

def is_Palindrome(original_Str):
    rev_Str = original_Str[::-1]
    print(rev_Str)
    if original_Str == rev_Str:
        print("Palindrome")
    else:
        print(" It is not")

        print(is_Palindrome(original_Str))