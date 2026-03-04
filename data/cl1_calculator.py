import pandas as pd

# Load dataset
df = pd.read_csv("data/sample_logistics_dataset.csv")

# ---- V Useful value ----
df["value"] = df["payload"] * df["useful_km"]
V = df["value"].sum()

# ---- E Energy dissipation ----
E = df["fuel"].sum()

# ---- I Informational dissipation ----
I = (
    df["replans"].sum()
    + df["exceptions"].sum()
    + df["delay"].sum()
    + df["rework"].sum()
)

# ---- S Structural dissipation ----
S = df["empty_km"].sum() + df["idle_time"].sum()

# epsilon
epsilon = 1

# Congruity Logistics
CL = V / (E + I + S + epsilon)

print("Useful value V:", V)
print("Energy dissipation E:", E)
print("Informational dissipation I:", I)
print("Structural dissipation S:", S)
print("Congruity Logistics CL:", round(CL, 4))
