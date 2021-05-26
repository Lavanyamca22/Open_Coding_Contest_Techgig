def prime_game(L,R):
    prime_list = []
    prime = [True for i in range(R+1)]
    p = 2
    while(p*p<=R):
        if(prime[p] == True):
            for i in range(p*p,R+1,p):
                prime[i] = False
        p+=1
    for p in range(2,R+1):
        if prime[p] and p>=L:
            prime_list.append(p)
    if(len(prime_list) == 1):
        return 0
    elif(len(prime_list) == 0):
        return -1
    else:
        return prime_list[-1]-prime_list[0]

N = int(input())
for i in range(0,N):   
    L,R = list(map(int,input().split()))
    result = prime_game(L,R)
    print(result)
