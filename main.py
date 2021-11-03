import random

def max(nmax,a,i):
    if i>len(a)-1:
        return nmax
    else:
        if a[i] > nmax:
            nmax = a[i]
        return max(nmax, a, i + 1)


def min(nmin,a,i):
    if i>len(a)-1:
        return nmin
    else:
        if a[i] < nmin:
            nmin = a[i]
        return min(nmin, a, i + 1)


def main():
    a=[]
    n=int(input('n='))
    for i in range(n):
        a.append(random.randint(-20,20))
    print(a)
    print(max(a[0],a,0))
    print(min(a[0],a,0))


if __name__=='__main__':
    main()