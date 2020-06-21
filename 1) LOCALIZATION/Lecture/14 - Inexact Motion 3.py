# What's the distribution after the motion given the following:
#
# p = [0.2, 0.2, 0.2, 0.2, 0.2]
# U = 2
#
# TargetU = 0.8
# Under1 = 0.1
# Over1 = 0.1
#
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# p = [0.2, 0.2, 0.2, 0.2, 0.2]
#
# U = 2
# pHit = 0.8
# pOver = 0.1
# pUnder = 0.1
#
#
# q = []
#
# def Normalize(U,pHit,pOver,pUnder):
#     pRight = p[(((i - U)+1) % len(p))]
#     pLeft = p[(((i - U)-1) % len(p))]
#     pTarget = p[(((i - U)) % len(p))]
#
#     for i in range(len(p)):
#         if pLeft != 0 and pTarget != 0 and pRight != 0:
#             q.append(pL)
#
#
# for i in range(len(p)):
#
#     if p[((i - U) % len(p))] != 0:
#         q.append(pHit * p[((i - U) % len(p))])
#     elif ((p[(((i - U)+1) % len(p))] != 0) and (p[(((i - U)-1) % len(p))] != 0)):
#         q.append((pUnder * p[(((i - U)+1) % len(p))])+(pOver * p[(((i - U)-1) % len(p))]))
#     elif p[(((i - U)+1) % len(p))] != 0:
#         q.append(pUnder * p[(((i - U)+1) % len(p))])
#     elif p[(((i - U)-1) % len(p))] != 0:
#         q.append(pOver * p[(((i - U)-1) % len(p))])
#     else:
#         q.append(0)
#
# print(q)

p = [0.2, 0.2, 0.2, 0.2, 0.2]

def normalize(U, pHit, pRight, pLeft):

    p2 = []
    for i in range(len(p)):
        motion = ((i - U) % len(p))
        p2.append(p[motion])

    p3 = []
    for i in range(len(p2)):
        Hit_Reward = (p2[i] * pHit)
        Right_Reward = (p2[((i - 1) % len(p2))] * pRight)
        Left_Reward = (p2[((i + 1) % len(p2))] * pLeft)
        p3.append(Hit_Reward + Right_Reward + Left_Reward)

    return p3

print(normalize(1, 0.8, 0.1, 0.1))


