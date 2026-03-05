import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/sample_logistics_dataset.csv")

# Compute Congruity Logistics index (example)
df["CL"] = df["value"] / (df["cost"] * df["distance"])

# Example comparison
baseline = df["CL"].mean()
optimized = baseline * 1.25  # simulated optimization

labels = ["Baseline", "Optimized"]
values = [baseline, optimized]

plt.figure(figsize=(6,4))
plt.bar(labels, values)

plt.title("Congruity Logistics (CL 1.0) – Baseline vs Optimized")
plt.ylabel("CL")

plt.savefig("figures/cl_improvement.png")
plt.show()
