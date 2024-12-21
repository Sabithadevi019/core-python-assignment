def palindrome(string):
    check = list(string)
    reversed_check = check[::-1]
    if check == reversed_check:
        print("String is a palindrome")
    else:
        print("String is not a palindrome")

string = input("Enter string: ")
palindrome(string)
