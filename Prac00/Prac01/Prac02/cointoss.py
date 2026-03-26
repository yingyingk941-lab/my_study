import random
coin = ['heads','tails']
heads = 0
tails = 0
trials = 1000
print('\nCOIN TOSS\n')
for index in range (trials):
    if random. choice(coin) == 'heads':
        heads = heads + 1
    else:
        tails = tails + 1
print('\nThere were ', heads, ' heads & ', tails, ' tails.\n')







import time


LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'
numlines = 3

eyes = ["\n< @ > < @ >\n",
       "\n<@  > <@  >\n",
       "\n<  @> <  @>\n"]

for i in range(10):
    if i % 2 == 0:
        print(eyes[0])
    elif i % 4 == 1:
        print(eyes[1])
    else:
        print(eyes[2])
    time.sleep(0.5)
    for j in range(numlines):
        print(LINE_UP, end=LINE_CLEAR)


numlines = 4

eyes = ["\n< @ > < @ > \n    db\n  \_____/",
        "\n<@  > <@  >\n    db\n  \____/",
        "\n<  @> <  @>\n    db\n  \____/"]





Swimming left
  /
 /\/
 \/\
  \



Swimming right
 \
\/\
/\/        
 /
        

