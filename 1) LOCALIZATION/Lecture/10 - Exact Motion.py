# What's the posterior probability after cyclical motion, with only one grid cell movement to the right
#
# p = [1/9, 1/3, 1/3, 1/9, 1/9]
# n = 1
#
# ----------------------------------------------------------------------

p = [1/9, 1/3, 1/3, 1/9, 1/9]
n = 1
pNew = []

for i in range(len(p)):
    motion = ((i - n) % len(p))
    pNew.append(p[motion])

print(pNew)





