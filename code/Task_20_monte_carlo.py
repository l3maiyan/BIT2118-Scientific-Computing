import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
capacity = 1000.0
mean_demand = 850.0
std_demand = 120.0
N = 100_000
demand = rng.normal(mean_demand, std_demand, N)
overloaded = demand > capacity
probability = overloaded.mean()
print("ORIGINAL CASE: SERVER OVERLOAD RISK")
print(f"Estimated overload probability: {probability:.4%}")
print(f"Overload cases: {overloaded.sum()} out of {N}")
running_probability = np.cumsum(overloaded)/np.arange(1, N+1)
indices = np.unique(np.logspace(1, np.log10(N), 200).astype(int))-1
plt.semilogx(indices+1, running_probability[indices])
plt.xlabel("Number of simulations"); plt.ylabel("Estimated overload probability")
plt.title("Monte Carlo estimate of server-overload risk"); plt.grid(True); plt.show()

# Parameter change: increase average demand from 850 to 900
demand_changed = rng.normal(900.0, std_demand, N)
changed_probability = np.mean(demand_changed > capacity)
print("\nCHANGED PARAMETER: MEAN DEMAND = 900")
print(f"New estimated overload probability: {changed_probability:.4%}")

# Related case: estimate the probability that daily customer arrivals exceed service capacity
customer_arrivals = rng.normal(180, 25, N)
service_capacity = 220
arrival_risk = np.mean(customer_arrivals > service_capacity)
print("\nRELATED CASE: CUSTOMER QUEUE RISK")
print(f"Estimated probability of exceeding 220 customers: {arrival_risk:.4%}")
