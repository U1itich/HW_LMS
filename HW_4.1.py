#1
s={}
summ=0
for i in range(int(input())):
  a=input()
  if not a in s:
    s[a]=1
  else:
    s[a]+=1
    for k,p in s.items():
      if p>1:
        summ+=p
print(summ)
