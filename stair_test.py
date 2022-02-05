from stair import *

def test():
    print('t3:',solution(3))
    print('t5:',solution(5))
    #print('t6:',solution(6))
    #print('t7:',solution(7))
    #print('t8:',solution(8))
    #print('t10:',solution(10))
    #print('t11:',solution(11))
    #print('t20:',solution(20))

def test2():
    for i in range(3,101):
        print('t',i,':',solution(i))



def math():
    n = 5
    i = 1
    print(n-i)
    print(int((n-i)/2+0.6)-i-1)

test2()