import random

rolls = [random.randint(1, 6) for i in range(100)]
print(f"Rolls: {rolls}")

# Use this for random rolls. (Yes, this could have been O(n) and is not).
observed = {i: rolls.count(i) for i in [1,2,3,4,5,6]}

# Use this for hard-coded rolls.
# observed = {1: 16, 2: 15, 3: 20, 4: 16, 5: 16, 6: 17}
print(f"\nObserved counts: {observed}")

# Expected counts are same for all 6 events in a fair die
e_i = (1/6) * len(rolls)
print(f"Expected counts: {e_i:.3f}")

chi_squared = sum([((o_i - e_i)**2)/e_i for o_i in observed.values()])
cv = 11.070 # from table
print(f"\nChi-Squared test statistic: {chi_squared:.3f}")
print(f"Critical value: {cv}")
print(f"Should we reject the null hypothesis? (aka, is the dice unfair?) {chi_squared > cv}")
