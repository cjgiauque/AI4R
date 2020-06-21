# Belief = Probability (must always sum to 1)
# Sense = Product followed by normalization
# Move = Convolution (i.e. Addition)
#
#
# Bayes Rule:
# P(X|Z) = (P(Z|X) * P(X)) / P(Z)
# i.e. Posterior = (Measure Probability * Prior) / Normalizer
#
# where...
# X = grid cell
# Z = measurement
# P(X|Z)..."POSTERIOR: The probability of 'X' being true, given 'Z' is true."
# P(Z|X)..."MEASURE PROBABILITY: The probability of 'Z' being true, given 'X' is true."
# P(X)..."PRIOR: The probability 'X' being true. This is the knowledge."
# P(Z)..."NORMALIZER: The probability 'Z' being true; P(Z) = summation of P(Z|Xi) * P(Xi)"
#
# ----------------------------------------------------------------------
# CANCER TEST EXAMPLE:
#
# P(C) = 0.001  <<< Probability of having the cancer
# P(≠C) = 0.999  <<< Probability of not having the cancer
# P(POS|C) = 0.8  <<< Probability that test comes out positive
# P(POS|≠C) = 0.1  <<< Probability of false positive test
#
# P(C|POS) = ???  <<< What's the probability of cancer given positive test?
#
# Nomenclature:
# p̂ = pHat = Not Normalized
# α = Normalizer
#
# ----------------------------------------------------------------------
#
# QUIZ:
# P(C|POS)= (P(POS|C) * P(C)) / P(POS)
#
# P(POS|C) = 0.8
# P(C) = 0.001
# P(POS|≠C) = 0.1
# P(POS) = ?
#
# SOLUTION:
# p̂(C|POS) = 0.8 * 0.001 = 0.0008
# p̂(≠C|POS) = 0.999 * 0.001 = 0.0999
# α = 0.008 + 0.0999 = 0.1007
# P(C|POS) = 0.0008 / 0.1007 = 0.0079
#
# ----------------------------------------------------------------------

def P_Cancer_Given_Pos(P_Positive_Given_C, P_Cancer, P_FalsePositive):
    P_NonNorm_C_Given_Pos = (P_Positive_Given_C * P_Cancer)
    P_NonNorm_notC_Given_Pos = ((1 - P_Cancer) * P_FalsePositive)
    Normalizer = (P_NonNorm_C_Given_Pos + P_NonNorm_notC_Given_Pos)
    return (P_NonNorm_C_Given_Pos / Normalizer)

print(P_Cancer_Given_Pos(0.8, 0.001, 0.1))


