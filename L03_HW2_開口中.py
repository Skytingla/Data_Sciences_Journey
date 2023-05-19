# Range: 1 - 99 (inclusive)
# system generate an answer -> random number
# user input 1 number, check if the number within range
# check input match answer or not
# if yes then it's finished
# if not, Range update with input number, e.g. input 45, from 1-99 to 1-45
# set a limit: how many times in maximum can a user guess

import random
r_num = random.randint(1, 99)
#print(r_num)
r = {'From':1,'to':99}

while True:
    
    p_num = int(input('Pick a number: '))

    if r_num == p_num:
        print('BOOM')
    else:
        if r_num  in range(r['From'],p_num):
           r['to'] = p_num
           print(r)
        else:
            r_num  in range(p_num,r['to'])
            r['From'] = p_num
            print(r)     
              
