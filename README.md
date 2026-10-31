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

### ⚙️ Motor Configuration

The BATES grain geometry and nozzle configuration are held constant across the propellant comparison to isolate the effects of propellant selection.

| Parameter | Configuration |
|---|---|
| Grain | BATES, 4 segments × 70 mm |
| Outer diameter | 69 mm |
| Core diameter | 30 mm (20 mm in initial attempt; see Chapter 1) |
| Throat / exit diameter | 15 mm / 36.7 mm |
| Nozzle expansion ratio | 6 |
| Ambient conditions | Sea level |
| Baseline propellant | Nakka KNSB |



Three different propellant property sets are evaluated using the same grain geometry and nozzle configuration to isolate the effects of propellant selection.

Propellant cases:
```
KNSB — Baseline propellant
KNDX — Second comparison
RCS Blue Thunder — Third case
```

| KNSB | KNDX | Blue Thunder |
|:---:|:---:|:---:|
| <img width="531" height="533" alt="Screenshot 2026-10-31 181911" src="https://github.com/user-attachments/assets/bf93b14e-15ef-4471-aa02-2c6467836256" />  | <img width="530" height="527" alt="Screenshot 2026-10-31 181920" src="https://github.com/user-attachments/assets/40bbc836-4196-4ea5-9370-f76255288e5d" /> | <img width="536" height="533" alt="Screenshot 2026-10-31 181900" src="https://github.com/user-attachments/assets/1fbb7741-a59b-4af9-8ca5-553982a0cc63" />|


### 2️⃣ Rocket Flight Simulation — OpenRocket

The three motor simulations are imported into OpenRocket and evaluated using a common rocket design.

The flight simulations investigate how differences in motor thrust characteristics influence the rocket's trajectory and flight performance.

| [Rocket Design] |
|:---:|
| <img width="678" height="143" alt="image" src="https://github.com/user-attachments/assets/e65db89f-819c-4450-881c-3b5c48465463" />|

Flight comparison metrics:
```
Apogee
Maximum velocity
Maximum acceleration
Time to apogee
Velocity off rod
```

| [Rocket Simulations] |

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

| [Nozzle Expansion Results] |
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


### 🔥 Motor-Level Results (openMotor)

All three propellants were run in the same motor: four BATES segments (69 mm outer diameter, 30 mm core, 70 mm long), a 15 mm throat, a 36.7 mm exit, at sea level.

| | KNSB | KNDX | Blue Thunder |
|:---|:---:|:---:|:---:|
| Motor designation | K626 | K859 | L1387 |
| Total impulse | 1,615 N·s | 1,702 N·s | 2,621 N·s |
| Burn time | 2.55 s | 1.95 s | 1.86 s |
| Delivered Isp | 110.9 s | 114.5 s | 193.7 s |
| Average / peak pressure | 421 / 495 psi | 563 / 875 psi | 898 / 1,158 psi |
| Propellant mass | 3.28 lb | 3.34 lb | 3.04 lb |

- Blue Thunder delivers about **70% more Isp** than the two sugar propellants, from a *lighter* grain.
- Faster-burning propellants run at higher chamber pressure in the same nozzle.
- Kn was identical for all three (286.6 initial, 287.8 peak), confirming that only the propellant changed.

**Design iteration:** the first design used a 20 mm core and triggered openMotor warnings (port/throat ratio of 1.78, below the recommended 2.0, and peak mass flux above the limit). Widening the core to 30 mm raised the port/throat ratio to 4.00 and cut peak mass flux from 2.32 to 1.21 lb/(in²·s), at the cost of about 11% less propellant (3.70 to 3.28 lb) and lower impulse (1,894 to 1,615 N·s).

### 🚀 Vehicle-Level Results (OpenRocket)

The three thrust curves were flown in the same rocket.

| | KNSB | KNDX | Blue Thunder |
|:---|:---:|:---:|:---:|
| Apogee | 2,224 m | 2,314 m | 3,308 m |
| Max velocity | 277 m/s | 295 m/s | 452 m/s |
| Max acceleration | 133 m/s² | 257 m/s² | 338 m/s² |
| Time to apogee | 20.0 s | 19.8 s | 22.4 s |
| Velocity off rod | 16.9 m/s | 23.0 m/s | 25.7 m/s |

- Blue Thunder has 62% more impulse than KNSB but flies only about **49% higher**. Drag grows with the square of speed, so the faster rocket loses more energy to the air.
- KNDX and KNSB have similar total impulse (KNDX is 5% higher, with 4% higher apogee), but KNDX delivers it in a shorter burn, giving nearly **double the peak acceleration** (257 vs 133 m/s²).
- KNSB leaves the launch rod at 16.9 m/s, barely above the usual 15 m/s guideline.
- ⚠️ Blue Thunder reached 452 m/s (about Mach 1.3), and OpenRocket warned that body calculations may not be entirely accurate at supersonic speeds. Its apogee should be treated as approximate, though the trend (more impulse, higher apogee) is expected to hold.

### 📐 Nozzle Expansion Results

**openMotor check (KNSB, sea level):** changing only the exit diameter from 36.7 mm (expansion ratio 6.0) to 55 mm (ratio 13.4) left chamber pressure (495 psi) and burn time (2.55 s) unchanged, but reduced impulse from 1,615 to 1,473 N·s (about 9%) and delivered Isp from 110.9 to 101.1 s. The larger nozzle is over-expanded at sea level.

**Python validation:** with the motor's average chamber pressure (2.9 MPa), the nozzle script reproduces openMotor's ideal thrust coefficient at both expansion ratios.

| Expansion ratio | Python script | openMotor |
|:---:|:---:|:---:|
| 6.0 | 1.495 | 1.49 |
| 13.4 | 1.361 | 1.36 |

**Best nozzle by altitude** (ideal nozzle, with KNSB-like inputs: γ = 1.13, c* = 912 m/s, Pc = 2.9 MPa):

| Condition | Best expansion ratio | Best Cf | Ideal Isp |
|:---|:---:|:---:|:---:|
| Sea level | 5.2 | 1.50 | 139 s |
| 5 km | 8.5 | 1.60 | 149 s |
| 10 km | 15.1 | 1.71 | 159 s |
| Vacuum | 30+ (still rising) | 1.93 | 180 s |

The optimum nozzle grows with altitude because ambient pressure falls relative to chamber pressure.

### ⚠️ Limitations

- Motor hardware mass (case, closures, nozzle) was a placeholder estimate, identical for all three motors. Apogees are for comparing motors, not predicting real flights.
- The nozzle study uses KNSB-like gas properties and pressure, so its altitude results apply to that motor only, not to all three propellants.
- The nozzle script assumes a loss-free nozzle and a single chamber pressure, and ignores flow separation in strongly over-expanded nozzles.
- openMotor does not fully model erosive burning, and OpenRocket is less accurate above Mach 1.
- Propellant data comes from openMotor's built-in library, and real batches vary.
---

## 🚀 Future Work

- **Automated propellant sweep:** write a Python program that loops through many propellants and simulates the same motor for each one with no manual steps, collecting impulse, burn time, Isp, and peak pressure, then ranks and plots them.
- **Automated flight simulation:** export each simulated motor's thrust curve and fly it in the same rocket through a scriptable simulator (such as RocketPy), using a flight model that handles supersonic speeds better than the OpenRocket runs here.
- **Validation:** check the program against the three hand-run cases in this study (K626, K859, L1387) before trusting it on new propellants.
- **Wider design space:** sweep grain geometry and nozzle dimensions alongside propellant, and run the nozzle model with each propellant's own gas properties instead of the KNSB-like values used here.


All comparisons are based on consistent modeling assumptions and simulation settings.
