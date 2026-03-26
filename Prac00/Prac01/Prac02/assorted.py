import random
biscuits = []
biscuits. extend(['Monte Carlo']*7)
biscuits.extend(['Shortbread Cream']*7)
biscuits.extend(['Delta Cream']*6)
biscuits.extend(['Orange Slice']*6)
biscuits.extend(['Kingston']*5)
print('\nASSORTED CREAMS\n')
print('There are ', len(biscuits), ' biscuits in the pack.')
print('\n', biscuits, '\n')
more = input('\nWould you like a biscuits (Y/N)...')
while more != 'N':
    choice = random. randint(0,len(biscuit)-1)
    print('Your biscuit is : ', biscuits[choice])
    del biscuits[choice]
    more = input('\nWould you like a biscuit (Y/N)...')
print('\nThere are ', len(biscuits), ' biscuits left.')
print('\n', biscuits, '\n')

