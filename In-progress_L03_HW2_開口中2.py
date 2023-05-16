# Range: 1 - 99 (inclusive)
# system generate an answer -> random number
# user input 1 number, check if the number within range
# check input match answer or not
# if yes then it's finished
# if not, Range update with input number, e.g. input 45, from 1-99 to 1-45
# set a limit: how many times in maximum can a user guess

import random
r_num = random.randint(1, 99)

a = 15
while True:
    p_num = int(input('Pick a number: '))
    range = {'st':1,'en':99}
    if r_num == p_num:
        print("BOOM!!")
        print(f'Rand: {r_num}, Input: {p_num}')
        print(range)
        print(r_num)
    elif r_num > p_num:
        range['st']= p_num
        print(f'{range["st"]} to {p_num}')
        print(range)
        print(r_num)
    elif r_num < p_num:
        range['en'] = p_num
        print(f'{p_num} to {range["en"]}')
        print(f'Rand: {r_num}, Input: {p_num}')
        print(range)
        print(r_num)

    
print(f'Rand: {r_num}, Input: {p_num}')