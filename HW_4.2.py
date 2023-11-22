#2
text=input()
b = ""
a = True
for i in range(len(text)):
  if text[i].isalpha():
    if a:
      b += text[i].upper()
      a = False
    else:
      if text[i]==text[i].upper():
        b += text[i]
      else:
        b += text[i].lower()
  else:
    b += text[i]
    if text[i] in [".", "!", "?"]:
      a = True
print(b)
