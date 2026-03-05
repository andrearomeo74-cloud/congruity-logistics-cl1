# Congruity Logistics, CL 1.0

![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.x-blue)
![Status](https://img.shields.io/badge/status-research%20prototype-orange)
![Reproducibility](https://img.shields.io/badge/reproducible-yes-brightgreen)

## What this is
This repository is a minimal, auditable demo of **Congruity Logistics (CL 1.0)**, a single metric that measures how much **useful logistics service** is produced per unit of **total dissipation**.

Core idea, logistics waste is measurable, empty kilometers, idle time, replanning, exceptions, rework, and energy, CL increases when that dissipation decreases for the same delivered service.

## Metric
CL is defined as

CL = V / (E + I + S + ε)

Where

V, useful logistic value  
E, energy dissipation  
I, informational dissipation  
S, structural dissipation  
ε, small constant to avoid division by zero

## Operational definitions

## Quick Start

Clone the repository

```bash
git clone https://github.com/andrearomeo74-cloud/congruity-logistics-cl1.git
cd congruity-logistics-cl1
```

### V, useful logistic value
Preferred

V = Σ(payload × useful_km)

Alternative proxies

V = Σ(passenger_km)  
V = Σ(delivered_orders × distance_weight × on_time_weight)

### E, energy dissipation
Use the best available signal

E = Σ(fuel_liters)  
E = Σ(kWh)  
E = Σ(energy_cost)  
E = Σ(total_km × average_consumption), proxy

### I, informational dissipation
A transparent event score

I = a·R + b·X + c·P + d·W

R, replanning events  
X, operational exceptions  
P, delays beyond threshold  
W, rework operations

Start with a = b = c = d = 1, then document any calibration.

### S, structural dissipation
Network and operational waste

S = u·empty_km + v·idle_time + w·route_deviation

Start with u = v = w = 1, then document any calibration.

## Dataset, minimal columns
One row per trip, delivery, or transport event.

id_event  
timestamp  
origin  
destination  
total_km  
useful_km  
empty_km  
payload  
fuel_or_energy  
idle_time  
delay_minutes  
replans  
exceptions  
rework

If some variables are missing, use declared proxies and keep the audit trail.

## Experiment design
Use two comparable windows

Baseline period, before optimization  
Optimized period, after reducing dissipation

Primary metric

ΔCL, percentage change in CL

Secondary checks

Δempty_km, Δenergy, Δexceptions, Δidle_time

## Reproducibility
Every term in CL is measurable or a declared proxy, weights are documented, calculations are repeatable.

## License
MIT

## Author
Andrea Romeo
