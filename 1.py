from typing import List

def solution(S: str) -> str:
    '''
    1. use hashtable to count the number of all digits
    2. begin to combine
    '''
    digit_table = {}
    num = int(S)
    while num:
        digit_table[num%10] += 1
        num = num/10
    print(digit_table)



if __name__ == "__main__":
    S1 = '39878'
    S2 = '00900'
    S3 = '0000'
    S4 = '54321'

    solution(S1)
    # assert S1 == '898'
    # assert S2 == '9'
    # assert S3 == '0' 
    # assert S4 == '5'