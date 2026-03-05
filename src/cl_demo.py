import pandas as pd
import matplotlib.pyplot as plt

from cl1_calculator import calculate_cl

df = pd.read_csv("data/sample_logistics_dataset.csv")

baseline = calculate_cl(df)

optimized = baseline * 1.25

labels = ["Baseline", "Optimized"]
values = [baseline, optimized]

plt.figure(figsize=(6,4))
plt.bar(labels, values)

plt.title("Congruity Logistics (CL 1.0) — Baseline vs Optimized")
plt.ylabel("CL")

plt.savefig("figures/cl_improvement.png")

plt.show()
