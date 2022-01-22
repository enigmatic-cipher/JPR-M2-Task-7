"""
Given a string str as input, check whether str can be of the type str = str1+str1.
Input: "Java" Output: No
Input: "123123" Output: Yes
"""

st = "JAVA"
ln = len(st)
st1 = ""
st2 = ""
for i in range(0,ln):
  ch = st[i]
  if(i>=int(ln/2)):
    st1 = st1 + ch
  elif(i<int(ln/2)):
    st2 = st2 + ch
if(st2==st1):
  print("Yes")
else:
  print("No")
  