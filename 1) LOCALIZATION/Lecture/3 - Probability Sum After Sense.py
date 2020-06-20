# What's the sum of all of the values...confirm that it's not valid cause it doesn't equal one."

R = 0.6
G = 0.2
colors = [G,R,R,G,G]
sum = 0

for i in range(len(colors)):
    sum += (colors[i] * (1/len(colors)))

print(sum)
