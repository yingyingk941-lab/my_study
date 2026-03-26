instring = input('Enter a string...')
print('Resever string is : ', end='')
index = len(instring)-1
while index > -1:
    print(instring[index], end='')
    index = index - 1
print()

print('Reversed string is : ', end='')
for index in range(len(instring)-1, -1, -1):
    print(instring[index], end='')
print()

print('Reversed string is :', instring[::-1])

print('Reversed string is :', instring[len(instring)-1:-1:-1])

