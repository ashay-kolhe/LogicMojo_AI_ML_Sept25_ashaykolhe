# Write a program to count no. of vowels and print all the vowels.

vowels = ["a", "e", "i", "o", "u"]
str1 = "Ashay Kolhe"
vowels_in_str1 = []
for i in range(len(str1)):
    if str1[i].lower() in vowels:
        vowels_in_str1.append(str1[i])

print(f"vowels are {vowels_in_str1}")
