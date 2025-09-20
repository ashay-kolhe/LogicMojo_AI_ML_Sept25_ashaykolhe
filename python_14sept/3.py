# Write a program to Reversing a String without using reverse().

str1 = "Ashay"
rev = ""
for i in range(len(str1)):
    rev += str1[len(str1) - i - 1]

print(f"rev is {rev}")
