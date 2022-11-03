import re
s=str(input())
d=re.findall(r'[\d]',s)
f=re.findall(r'[^\W,\d]',s)
if len(d)==11 and len(f)==0:
    if len(re.findall(r'[+][7]',s))==1:
        s=s.replace('+7','8')
    if re.findall(r'[(][\d]{3}[)]',s):
        g=s.index('(')
        h=s[g:g+5]
        k=s[g+1:g+4]
        s=s.replace(h,k)
    if re.findall(r'[-]',s)!=['']:
        s=s.replace('-','')
    if re.findall(r'[\s]',s)!=['']:
        s=s.replace(' ','')
    print(s[0]+'-'+s[1:4]+'-'+s[4:7]+'-'+s[7:9]+'-'+s[9:11])
else:
    print('Ошибка')
