#!/usr/bin/py
def lonelyinteger(a):
    j=1
    while len(a)>2:
            if a[0]==a[j]:
                a.pop(j)
                a.pop(0)
                j=1
            else:
                j=j+1
                if j==len(a):
                    break
    return a[0]


if __name__ == '__main__':
    a = input()
    b = map(int, raw_input().strip().split(" "))
    print lonelyinteger(b)
