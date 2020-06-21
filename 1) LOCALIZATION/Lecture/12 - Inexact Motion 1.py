# What's the distribution after the motion given the following:
#
# p = [0,1,0,0,0]
# U = 2
#
# TargetU = 0.8
# Under1 = 0.1
# Over1 = 0.1
#
# ----------------------------------------------------------------------

p = [0,1,0,0,0]
U = 2

pHit = 0.8
pOver = 0.1
pUnder = 0.1

q = []

for i in range(len(p)):

    if p[((i - U) % len(p))] == 1:
        q.append(pHit)
    elif p[(((i - U)+1) % len(p))] == 1:
        q.append(pUnder)
    elif p[(((i - U)-1) % len(p))] == 1:
        q.append(pOver)
    else:
        q.append(0)

print(q)