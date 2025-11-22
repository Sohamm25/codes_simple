# lcm and gcd
a = int(input())
b = int(input())
#for lcm-
aa = []
bb = []
if a > b:
    for i in range(1, a + 1):
        aa.append(a * i)
        bb.append(b * i)
else:
    for i in range(1, b + 1):
        aa.append(a * i)
        bb.append(b * i)
abc = []
for i in aa:
    if i in bb:
        abc.append(i)
if abc:
    final2 = min(abc)
    print("LCM:", final2)
else:
    print("The list is empty, no minimum value.")
print(aa, bb, abc)
# for gcd - 
ab = []
ba = []
if a > b:
    for i in range(1, a + 1):
        if a % i == 0:
            ab.append(i)
        if b % i == 0:
            ba.append(i)
else:
    for i in range(1, b + 1):
        if a % i == 0:
            ab.append(i)
        if b % i == 0:
            ba.append(i)
abcd = []
for i in ab:
    if i in ba:
        abcd.append(i)
if abcd:
    final2 = max(abcd)
    print("GCD:", final2)
else:
    print("The list is empty, no minimum value.")
print(ab, ba, abcd)