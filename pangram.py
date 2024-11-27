inputstring = input("Enter a number")
letters = {"0":0,"1":0,"2":0,"3":0,"4":0,"5":0,"6":0,"7":0,"8":0,"9":0}
for i in inputstring:
    print(i)
    if i in letters:
            letters[i] += 1
print(letters)
pangram = True
for count in letters.values():
      if count == 0:
            pangram = False
if pangram == True:
      print("You've made a pangram! :) ") 
else:
    print("You have not made a pangram :( ")