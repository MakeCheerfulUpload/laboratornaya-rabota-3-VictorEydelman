import re
n=re.split(r' ',str(input()))
for i in range(len(n)):
    d=re.split(r'[А,И,О,У,Ы,Э,Е,Ё,Ю,Я]',n[i].upper())
    g=re.split(r'[А,И,О,У,Ы,Э,Е,Ё,Ю,Я]{2}',n[i].upper())
    if sum(map(len,d))<=3 and len(g)>1:
        print(n[i])
