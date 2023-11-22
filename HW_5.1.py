#1
def a(a):
    a1=""
    last=str(a)
    while a!=0:
        a1+=str(a%10)
        a//=10
    if last==a1:
        return True
    else:
        return False
print(a(input()))
