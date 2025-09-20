# Write a program to check palindrome.

def palindrome_rev(str1, str2):
    if len(str1) != len(str2):
        return False
    rev = str2[::-1]
    if str1 == rev:
        return True
    return False


if palindrome_rev("abc", "cba"):
    print("Is palindrome")
else:
    print("Not a palindrome")


def palindrome_loop(str1, str2):
    if len(str1) != len(str2):
        return False
    str2len = len(str2)
    for i in range(str2len):
        if str1[i] != str2[str2len-i-1]:
            return False
    return True


if palindrome_loop("ashay", "yahsa"):
    print("Is palindrome")
else:
    print("Not a palindrome")

if palindrome_loop("aaa", "bbb"):
    print("Is palindrome")
else:
    print("Not a palindrome")