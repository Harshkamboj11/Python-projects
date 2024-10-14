print("       vowels calculator     ")
print()
print()

print("enter any name: ")
a = str(input("")).lower()
vowels = 0
vowel = ''
for i in a:
    if i == 'a':
        vowels += 1
    elif i == 'e':
        vowels += 1
    elif i == 'i':
        vowels += 1
    elif i == 'o':
        vowels += 1
    elif i == 'u':
        vowels += 1

print(f"number of vowels in {a} is/are {vowels}")