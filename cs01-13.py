y = ['*']
for i in range(6):
    for j in range(0,i+1):
        a = y*j
        print(a)
        if (j == 6):
            print(a ,end='')