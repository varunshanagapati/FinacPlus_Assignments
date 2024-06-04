def cipher(t,s):
    ref= ""
    for i in t:
        if i.islower() :
            ref += chr((ord(i) + s-97)%26 + 97)
        else:
            ref += chr((ord(i) + s-65)%26 + 65)
    res= ""
    cnt = 1
    for i in range(len(ref)-1):
        if ref[i]==ref[i+1] :
            cnt+=1
        else:
            if cnt>1 :
                res+=ref[i]+str(cnt)
            else:
                res+=ref[i]
            cnt=1
    if cnt>1 :
        res+=ref[i]+str(cnt)
    else:
        res+=ref[i]
    return res
a= input()
s = int(input())
print(cipher(a,s))