t = int(input())
l = list()
if t >= 1 and t <= 20:
    for i in range(t):
        n_kList = input().split()
        n,k = map(int,n_kList)
        if n >= 0 and n <= (10**5):
            elList = input().split()
        if len(elList) == n:
            l = list(map(int,elList))
        if k >= 0 and k <= (10**6):
            l = (l[-k:] + l[:-k]) 
        print(' '.join(map(str, l))) 
