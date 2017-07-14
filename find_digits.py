#!/bin/python3


t = int(input().strip())
num_list = []
for a0 in range(t):
    n = int(input().strip())
    num_list.append(n)


for num in num_list:
    count = 0
    for i in str(num):

        if int(i)!=0 and (num%int(i)==0):
            count+=1
    print (count)