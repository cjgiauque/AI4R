# Use product rule to adjust probabilities given provided weights.

R = 0.6
G = 0.2
colors = [G,R,R,G,G]
p = []

for i in range(len(colors)):
    p.append(colors[i] * (1/len(colors)))

print(p)
