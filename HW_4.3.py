#3
def k(str1, str2):
  return sorted(str1) == sorted(str2)
  
import re
a = re.sub(r'[^a-zа-яё]', '', input().lower())
b = re.sub(r'[^a-zа-яё]', '', input().lower())
print(k(a, b))
