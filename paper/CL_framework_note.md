# Congruity Logistics (CL 1.0)

## A Minimal Framework Note

### Overview

Congruity Logistics (CL 1.0) is a minimal metric designed to evaluate the efficiency of logistics systems by comparing **useful service delivered** with **total systemic dissipation**.

The core hypothesis is that many logistics systems suffer from measurable operational waste, including:

- empty kilometers
- idle time
- replanning events
- operational exceptions
- unnecessary energy consumption

CL provides a simple and auditable way to quantify this inefficiency.

---

### Definition

The Congruity Logistics metric is defined as:

CL = V / (E + I + S + ε)

Where:

V = useful logistic value  
E = energy dissipation  
I = informational dissipation  
S = structural dissipation  
ε = small constant to avoid division by zero

---

### Interpretation

The metric measures **useful service per unit of total dissipation**.

Higher CL indicates a system that produces more service while consuming fewer resources and generating less operational waste.

Lower CL indicates structural inefficiencies in the logistics network.

---

### Components

#### Useful Value (V)

Represents productive transport work.

Example metrics:

- payload × useful distance
- passenger × distance
- delivered orders weighted by distance

---

#### Energy Dissipation (E)

Energy required to operate the system.

Possible measurements:

- fuel consumption
- electrical energy
- energy cost proxies

---

#### Informational Dissipation (I)

Operational complexity and coordination overhead.

Examples:

- replanning events
- operational exceptions
- delivery delays
- rework operations

---

#### Structural Dissipation (S)

Network and operational inefficiencies.

Examples:

- empty kilometers
- idle vehicle time
- route deviations

---

### Relation to System Efficiency

CL can be interpreted as a generalized efficiency metric:

Useful Output / Total Dissipation

When demand is fixed, maximizing CL is equivalent to minimizing systemic dissipation.

---

### Purpose of This Repository

This repository provides a **minimal reproducible demonstration** of the CL concept using:

- a small logistics dataset
- a Python calculator script
- a Jupyter notebook simulation

The goal is not to claim a universal law, but to present a transparent metric that can be tested and audited in logistics systems.

---

### Author

Andrea Romeo

Research direction:  
Congruity as a measurable efficiency metric for complex flow systems.
