inputstring = input("Enter a word")
vowels = {"a":0,"e":0,"i":0,"o":0,"u":0}
for i in inputstring:
    print(i)
    if i in vowels:
        vowels[i] += 1
print(vowels)