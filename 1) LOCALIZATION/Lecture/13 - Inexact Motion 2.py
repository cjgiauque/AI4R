# What's the distribution after the motion given the following:
#
# p = [0, 0.5, 0, 0.5, 0]
# U = 2
#
# TargetU = 0.8
# Under1 = 0.1
# Over1 = 0.1
#
# ----------------------------------------------------------------------

p = [0, 0.5, 0, 0.5, 0]
U = 2

pHit = 0.8
pOver = 0.1
pUnder = 0.1

q = []

for i in range(len(p)):

    if p[((i - U) % len(p))] != 0:
        q.append(pHit * p[((i - U) % len(p))])
    elif ((p[(((i - U)+1) % len(p))] != 0) and (p[(((i - U)-1) % len(p))] != 0)):
        q.append((pUnder * p[(((i - U)+1) % len(p))])+(pOver * p[(((i - U)-1) % len(p))]))
    elif p[(((i - U)+1) % len(p))] != 0:
        q.append(pUnder * p[(((i - U)+1) % len(p))])
    elif p[(((i - U)-1) % len(p))] != 0:
        q.append(pOver * p[(((i - U)-1) % len(p))])
    else:
        q.append(0)

print(q)