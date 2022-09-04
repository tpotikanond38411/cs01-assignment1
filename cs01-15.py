Num = int(input('Enter your loop: '))
num_total = []
for i in range(Num):
    data = int(input('Enter your data: '))
    num_total += [data]


num_total.sort()
print('Min: ',num_total[0])

Num_total = num_total[::-1]
print('Max:',Num_total[0])

print("Finish")

