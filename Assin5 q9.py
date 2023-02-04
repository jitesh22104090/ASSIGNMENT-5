listin=input('enter space seperated words:').split()
setin=set(listin)
for i in setin:
    count=0
    for j in listin:
        if j==i:
            count+=1
    print('number of',i,'=',count)