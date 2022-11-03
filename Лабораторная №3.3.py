import re
a=str(input())
n=re.split(r'[\w,\.,\_]*[@][^\W,_]*[\.][^\W,_]*',a)
print(re.findall(r'[\w]*[\.][\w]*',a)[-1] if n==len(n)*[''] else 'Fail!')
