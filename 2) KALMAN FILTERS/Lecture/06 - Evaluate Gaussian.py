# first programming exercise...
#
# f(x) = (1/sqrt(2πσ²)) * exp^((-1/2)*((x-µ)/σ)^2
#
# Calculate f(x) given...
# Mu (µ) = 10
# Sigma Squared (σ²) = 4
# x = 8

mu = 10
ss = 4
x = 8
import math
pi = math.pi

P1 = 1/math.sqrt(2*pi*ss)
P2 = math.exp(-1/2)
P3 = ((x-mu)**2/ss)

function = P1*P2*P3