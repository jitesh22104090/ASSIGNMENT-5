a = int(input('enter range: '))
b = int(input('enter number for which divisibility is to be checked : '))

for i in range(0,a):
    if i%b==0:
        print(i)