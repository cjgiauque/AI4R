# Now, normalize the probabilities by dividing each by 0.36 and then confirm the sum equals one."
# p(Xi|Z) = "Posterior Distribution of place Xi given Z"
#
# colors = [G,R,R,G,G]
# R = 0.6
# G = 0.2
#
# ----------------------------------------------------------------------

R = 0.6
G = 0.2
colors = [G,R,R,G,G]
p1 = []
sum1 = 0

for i in range(len(colors)):
    p1.append(colors[i] * (1/len(colors)))
    sum1 += (colors[i] * (1/len(colors)))

p2 = []
sum2 = 0
for i in range(len(p1)):
    p2.append(p1[i]/sum1)
    sum2 += (p2[i])

print(p2)
print(sum2)