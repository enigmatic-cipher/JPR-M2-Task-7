"""
Given a string str as input, check whether str can be of the type str = str1+str1.
Input: "Java" Output: No
Input: "123123" Output: Yes
"""

st = "12312323"
ln = len(st)
ln1 = int(ln/2)
ln2 = int(ln-ln1)
st1 = ""
st2 = ""
for i in range(0,ln1):
  ch = st[i]
  st1 = st1 + ch
print(st1)