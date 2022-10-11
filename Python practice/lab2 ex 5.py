letters = []
numbers = []
user = input("enter a phrase")

for i in user:
    if i.isalpha() == True:
        letters.append(i)
    elif i.isdigit() == True:
        numbers.append(i)

print (letters)
print (numbers)
print (len(letters))
print(len(numbers))
