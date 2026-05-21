#write a pg to check how many vowels are present in an instagram string.
name=input("Enter a string:")
count = 0
for ch in name:
    if ch in "aeiouAEIOU":
        count = count+1
print("Total vowel are",count)