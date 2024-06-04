def Cipher_Text(text,shift):
    temp= ""
    for i in text:
        if i.islower() :
            temp+=chr((ord(i)+shift-97)%26+97)
        else:
            temp+=chr((ord(i)+shift-65)%26+65)
    cipher_text=""
    cnt = 1
    for i in range(len(temp)-1):
        if temp[i]==temp[i+1] :
            cnt+=1
        else:
            if cnt>1 :
                cipher_text+=temp[i]+str(cnt)
            else:
                cipher_text+=temp[i]
            cnt=1
    if cnt>1 :
        cipher_text+=temp[i]+str(cnt)
    else:
        cipher_text+=temp[i]
    return cipher_text
input_text=input()
shift=int(input())
print(Cipher_Text(input_text,shift))