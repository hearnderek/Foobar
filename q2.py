# Python2

def solution(l):
    return ''.join(sorted([str(x) for x in l if x == 1 or x%3==0], reverse=True))


print solution([1,2,3,5,6])