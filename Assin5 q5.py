n = int(input("Enter number of rows: "))
a = 65
for i in range (n+1):
    for j in range (i):
        print (chr(a), end = "")
        a = a + 1
        if a>=91:
            a = a-26
    print("")