from scipy.optimize import root_scalar

cash_flows = [-10000, 3000, 3500, 4000, 2500]
def npv(rate):
    return sum(cf / (1 + rate)**t for t, cf in enumerate(cash_flows))
def d_npv(rate):
    return sum(-t*cf/(1+rate)**(t+1) for t, cf in enumerate(cash_flows) if t > 0)

newton = root_scalar(npv, fprime=d_npv, x0=0.10, method="newton", xtol=1e-12)
secant = root_scalar(npv, x0=0.05, x1=0.20, method="secant", xtol=1e-12)
print("ORIGINAL CASE: INVESTMENT INTERNAL RATE OF RETURN")
print(f"Newton-Raphson IRR: {newton.root:.6%}")
print(f"Secant IRR: {secant.root:.6%}")
print(f"NPV at Newton solution: {npv(newton.root):.6f}")

# Parameter change: increase initial investment from 10,000 to 11,000
changed_flows = [-11000, 3000, 3500, 4000, 2500]
def changed_npv(rate):
    return sum(cf/(1+rate)**t for t, cf in enumerate(changed_flows))
changed = root_scalar(changed_npv, x0=.10, x1=.20, method="secant")
print("\nCHANGED INPUT: INITIAL INVESTMENT = 11,000")
print(f"New estimated IRR: {changed.root:.6%}")

# Related case: estimate the break-even discount rate for a small equipment purchase
equipment_flows = [-5000, 1800, 1800, 1800, 1800]
def equipment_npv(rate):
    return sum(cf/(1+rate)**t for t, cf in enumerate(equipment_flows))
equipment_irr = root_scalar(equipment_npv, x0=.10, x1=.30, method="secant")
print("\nRELATED CASE: EQUIPMENT PURCHASE")
print(f"Break-even rate: {equipment_irr.root:.6%}")
