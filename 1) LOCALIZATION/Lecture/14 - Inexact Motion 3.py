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


