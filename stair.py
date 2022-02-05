def solution(n):
    a,b = split(n), split2(n)
    if a != b:
        print(a,b)
    return b

def split(n,p=0):
    self_count = 0
    count = 0
    i = p+1
    while n-i > i:
        count += 1
        self_count += 1
        ret = split(n-i,i)
        count += ret
        i += 1

    return count

def split2(n,p=0):
    k=p+1
    e = int(n/2+0.6)
    return e-k + sum([split(n-i,i) for i in range(p+1,e) if n>=3*i+2])