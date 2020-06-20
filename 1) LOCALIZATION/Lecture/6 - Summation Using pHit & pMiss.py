# Modify the code so you get the sum of all of the previously calculated probabilities.
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

sum = 0
for i in range(len(p2)):
    sum += p2[i]

print(sum)
