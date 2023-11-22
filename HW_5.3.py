#3
def maxs(a,b,c=-9**9):
    maxi=-9**9
    if a>maxi:
        maxi=a
    if b>maxi:
        maxi=b
    if c>maxi:
        maxi=c
    return maxi
print(maxs(4,8,1))
