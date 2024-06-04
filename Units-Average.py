def Unit_Count(number,units):
    units_Set={}
    units.sort(reverse=True)
    cnt=0
    for i in units:
        if number>=i:
            cnt+=number//i
            units_Set[i]=number//i
            number-=i*(number//i)
    return cnt
units=list(map(int,input().split()))
unit_count=[]
for i in range(1,100):
    unit_count.append(Unit_Count(i,units))
print("AVG of Units:",sum(unit_count)/100)