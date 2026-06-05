s = input("Enter string: ") 

count = sum(1 for ch in s if ch.lower() in "aeiou") 

print("Vowels:", count) 

