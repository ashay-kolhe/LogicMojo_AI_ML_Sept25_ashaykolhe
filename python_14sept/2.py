# Write program count the blank spaces.

str1 = "a b c d e f "
count = 0
for l in str1:
    if l == " ":
        count += 1
print(f"count is {count}")

print(f"count is {str1.count(' ')}")