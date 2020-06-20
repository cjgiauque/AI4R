# Start with non-normalized. Write a piece of code that outputs 'p' after multiplying in pHit and pMiss."
#
# p = [0.2, 0.2, 0.2, 0.2, 0.2]
# pHit = 0.6
# pMiss = 0.2
#
# ----------------------------------------------------------------------

p = [0.2, 0.2, 0.2, 0.2, 0.2]
pHit = 0.6
pMiss = 0.2

precision = [pMiss,pHit,pHit,pMiss,pMiss]
p2 = []

for i in range(len(p)):
    p2.append(p[i] * precision[i])

print(p2)