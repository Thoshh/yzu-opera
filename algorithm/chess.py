#!usr/bin/python
#输出象棋中将帅不同线的所有情况，只用一个变量
i = 81
j=0
while i > 0:
    #print i,
    if i/9%3 == i%9%3:
        i=i-1
        continue
    print "a=",i/9+1,"b=",i%9+1
    i=i-1
