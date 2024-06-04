def sol(n,units):
    res={}
    units.sort(reverse=True)
    cnt=0
    for i in units:
        if n>=i:
            cnt+=n//i
            res[i]=n//i
            n-=i*(n//i)
    return cnt
units=list(map(int,input().split()))
res=[]
for i in range(1,100):
    res.append(sol(i,units))
print("AVG of Units:",sum(res)/100)