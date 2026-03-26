print('\nBUCKET LIST\n')
bucket1 = ['Witness something truly majestic',
        'Help a complete stranger' ,
        'Laugh uuntil I cry','Drive a Shelby Mustang']

bucket1.append('Kiss the most beautiful girl in the world')
bucket1.append('Get a tattoo')
bucket1.append('Skydiving')
del bucket1[5]

bucket2 = ['Visit Stonehence',
        'Drive a motorcycle on the Great Wall of China',
        'Go on a Safari','Visit the Taj Mahal',
        'Sit on the Great Egyptian Pyramids',
        'Find the Joy in your life']

print('Bucket 1: ', bucket1)
print('Bucket 2: ', bucket2)
bucket = bucket1 + bucket2
bucket.insert(5, 'Get a tattoo')

print('\nThe bucket list is:')
print('Complete bucket list: ', bucket)

print('\nNicer foematting....\n')


for item in bucket:
    print(item)

