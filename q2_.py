def solution(l):
    # presorting allows later index() calls to always return smallest values
    xs = sorted(l)
    mod = sum(xs)%3
    if mod == 0:
        return asNum(xs)

    # parallel array with xs for looking up index of number(s) to remove
    nmul = [x%3 for x in xs]

    # remove smallest number that makes whole multiple of 3
    if mod in nmul:
        del xs[nmul.index(mod)]
        if any(xs):
            return asNum(xs)

    # remove 2 smallest numbers that together make whole a multiple of 3
    omod = 3-mod
    if omod in nmul:
        i = nmul.index(omod)
        del nmul[i]
        del xs[i]
        if omod in nmul:
            i = nmul.index(omod)
            del nmul[i]
            del xs[i]
            if any(xs):
                asNum(xs)

    # impossible to make multiple of 3
    return 0

def asNum(xs):
    # assert on input being sorted in ascending order
    return int(''.join([str(x) for x in reversed(xs)]))

print solution([3, 1, 4, 1, 5, 9])
print solution([3, 1, 4, 1])
print solution([1, 4, 1])
print solution([4, 1])
print solution([4])