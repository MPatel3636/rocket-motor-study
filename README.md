# Solid Rocket Motor Propulsion Performance Study

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/) [![openMotor](https://img.shields.io/badge/Simulation-openMotor-orange.svg)](https://github.com/reilleya/openMotor) [![OpenRocket](https://img.shields.io/badge/Simulation-OpenRocket-green.svg)](https://openrocket.info/) [![NumPy](https://img.shields.io/badge/NumPy-Numerical%20Computing-013243.svg)](https://numpy.org/) [![SciPy](https://img.shields.io/badge/SciPy-Scientific%20Computing-8CAAE6.svg)](https://scipy.org/) [![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C.svg)](https://matplotlib.org/)

**Status:** 🔄 Propellant Comparison | 🚀 Flight Simulation | 📊 Nozzle Expansion Study

---

## 📖 Abstract

This project investigates the effects of propellant selection and nozzle expansion on solid rocket motor performance and rocket flight. Three propellant formulations are simulated in openMotor using a consistent grain geometry and nozzle configuration. The resulting thrust curves are imported into OpenRocket to evaluate their effects on rocket flight performance.

An additional Python-based nozzle expansion study examines the relationship between expansion ratio, ambient pressure, and ideal thrust coefficient. Together, these analyses provide a comparative study of propulsion performance from motor-level internal ballistics to vehicle-level flight behavior.

---

## 🔬 Project Pipeline

### 1️⃣ Propellant Performance Comparison — openMotor

Three different propellant property sets are evaluated using the same grain geometry and nozzle configuration to isolate the effects of propellant selection.

Propellant cases:
```
KNSB — Baseline propellant
KNDX — Second comparison
Third propellant — Additional comparison case
```

| KNSB | KNDX | Third Propellant |
|:---:|:---:|:---:|
| <img width="531" height="533" alt="Screenshot 2026-10-31 181911" src="https://github.com/user-attachments/assets/bf93b14e-15ef-4471-aa02-2c6467836256" />  | <img width="530" height="527" alt="Screenshot 2026-10-31 181920" src="https://github.com/user-attachments/assets/40bbc836-4196-4ea5-9370-f76255288e5d" /> | <img width="536" height="533" alt="Screenshot 2026-10-31 181900" src="https://github.com/user-attachments/assets/1fbb7741-a59b-4af9-8ca5-553982a0cc63" />|


### 2️⃣ Rocket Flight Simulation — OpenRocket

The three motor simulations are imported into OpenRocket and evaluated using a common rocket design.

The flight simulations investigate how differences in motor thrust characteristics influence the rocket's trajectory and flight performance.

| [Rocket Design](assets/openrocket_design.png) |
|:---:|
| <img width="678" height="143" alt="image" src="https://github.com/user-attachments/assets/e65db89f-819c-4450-881c-3b5c48465463" />
 |

Flight comparison metrics:
```
Apogee
Maximum velocity
Maximum acceleration
Time to apogee
Velocity off rod
```

| [Rocket Simulations](assets/openrocket_design.png) |

| KNSB | KNDX | Third Propellant |
|:---:|:---:|:---:|
| <img width="1024" height="768" alt="KNSB" src="https://github.com/user-attachments/assets/aeb5007e-ae5a-409e-91b6-75390fa87bde" />| <img width="1024" height="768" alt="KNDX" src="https://github.com/user-attachments/assets/823a39e4-bf7e-4488-a6b5-b2c19b2d0c9f" />| <img width="1024" height="768" alt="BlueThunder" src="https://github.com/user-attachments/assets/07bfc5b5-8368-405c-9029-4de2ae93587b" />|


### 3️⃣ Nozzle Expansion Study — Python

A Python script, `NozzleStudy.py`, investigates the effects of nozzle expansion ratio and ambient pressure on ideal thrust coefficient.

The script solves the isentropic nozzle exit-pressure relationship using SciPy's `brentq` root-finding method and evaluates the ideal thrust coefficient across a range of expansion ratios.

**Ambient-pressure conditions:**
```
Sea level: 101,325 Pa
5 km:       54,048 Pa
10 km:      26,436 Pa
Vacuum:          0 Pa
```

The expansion ratio is varied from 1.5 to 30, with the ideal thrust coefficient calculated for each condition.

The script generates:
- Thrust coefficient versus expansion ratio curves
- Maximum ideal thrust coefficient within the evaluated range
- Corresponding ideal specific impulse
- Comparison of thrust coefficient at an expansion ratio of 6

| [Nozzle Expansion Results](assets/nozzle_study.png) |
|:---:|
| <img width="1200" height="750" alt="nozzle_study" src="https://github.com/user-attachments/assets/98826cf7-7491-4133-b01c-4c96361b72a7" /> |

---

## 🎯 Key Technical Highlights

| Skill Domain | Implementation |
|---|---|
| Propulsion Engineering | Comparative solid motor simulations using consistent geometry |
| Internal Ballistics | Thrust curves, chamber pressure, impulse, and specific impulse analysis |
| Rocket Flight Dynamics | OpenRocket flight simulations using custom motor data |
| Compressible Flow | Isentropic nozzle expansion and exit-pressure calculations |
| Numerical Methods | SciPy root-finding with `brentq` |
| Scientific Computing | NumPy calculations and Matplotlib visualization |

---

## 🛠️ Python Implementation

The nozzle expansion study uses:

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
```

Install dependencies:

```bash
pip install numpy scipy matplotlib
```

Run the study:

```bash
python NozzleStudy.py
```

The script prints a performance table and saves the generated plot as `nozzle_study.png`.

---

## 📈 Results and Discussion

The project compares propulsion performance at two levels:

- **Motor level:** How propellant properties influence thrust characteristics and overall motor performance.
- **Vehicle level:** How differences in motor thrust curves affect rocket flight.

The nozzle expansion study provides an analytical perspective on how nozzle geometry and ambient pressure influence ideal thrust coefficient and specific impulse.

The combined results illustrate the relationship between propellant characteristics, nozzle performance, and rocket flight behavior.

---

## 🚀 Future Work

- Automate propellant comparisons using Python.
- Generate overlaid thrust curves and performance comparison tables.
- Expand the nozzle study to additional expansion ratios and ambient pressures.
- Compare analytical nozzle predictions with openMotor simulation results.
- Investigate the influence of grain geometry and nozzle configuration.

---

## ⚠️ Modeling Assumptions

The results are based on computational simulations and idealized nozzle-flow calculations. They represent modeled performance rather than experimentally validated motor performance.

The nozzle study assumes idealized flow and does not account for all real-world nozzle losses or combustion effects.

All comparisons are based on consistent modeling assumptions and simulation settings.
