# MEXVOFD
MEXVOFD Python package (Mexican Variable-Order Fractional Derivatives Python package), for studying three types of variable fractional derivatives: time-memory (V1), weak order-memory (V2), and strong order-memory (V3)


MEXVOFD Python Package
======================

Authors:
---------
Daniel Clemente-Lopez (Developer and Coder)

Jesus M. Munoz-Pacheco (Conceptualization, Methodology, and Validation)

Overview
--------
The --MEXVOFD Python package-- provides tools for simulating and solving --Variable-Order Fractional Derivatives (VOFD)-- in dynamical systems. This package is designed for researchers and practitioners to analyze and visualize systems modeled with variable-order derivatives, such as chaotic systems, hereditary processes, and control strategies.

The package supports three main types of VO derivatives:
- V1: Caputo Variable-Order Derivative.
- V2,V3: Variable-Order Derivatives with convolution.

The package is optimized using the **Numba JIT** compiler and supports **multiprocessing** for improved computational performance on bifurcation diagrams.

Installation
------------
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repository-url.git
   ```

2. Navigate to the package directory:
   ```bash
   cd mexvofd
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

Usage
-----
### Simulation Setup (simulation_setup.py)
This script demonstrates how to set up and run a simulation for a --Variable-Order Chaotic Chen System--. It uses the **V3 VO derivative** and saves the results.

1. Setup the system: The script defines the Chen system, a commonly used chaotic system, with initial conditions and a time span.
   
2. Run the simulation: It computes the trajectory of the system using the V3 VO derivative.

3. Output: The script saves the results of the simulation (`y1`, `y2`, `y3`) into `.txt` files and generates a plot of `y1` vs. `y3`.

To run the simulation, simply execute:
```bash
python simulation_setup.py
```

### Bifurcation Analysis Setup (bifurcation_setup.py)
This script is used to perform --bifurcation analysis-- of the --Variable-Order Chaotic Chen System--.

1. Setup the system: Similar to the simulation script, but this one focuses on analyzing how the system behavior changes as the bifurcation parameter (`a`) varies.

2. Bifurcation Process: The script calculates bifurcation points for `svar` and `xmax` and stores them in `.txt` files.

3. Output: The bifurcation analysis results are visualized in a plot.

To run the bifurcation analysis, execute:
```bash
python bifurcation_setup.py
```

Key Functions
-------------
- chen_system: Defines the equations of the Chen system (used in both scripts).
- vo_algorithm: Refers to the algorithm used for the VO derivative computation. In the `simulation_setup.py` script, it uses `v3_alg` (V3 VO derivative), while in `bifurcation_setup.py`, it uses `v3_bifurcation` for bifurcation analysis.
- create_figure: A utility function from `utils.plot_data` to create and save plots of the simulation or bifurcation results.

Results Directory
-----------------
Both scripts will save their outputs in the `results` folder:
- Simulation results: `v3_chen_y1.txt`, `v3_chen_y2.txt`, `v3_chen_y3.txt`
- Bifurcation results: `svar_chen_bif_a.txt`, `xmax_chen_bif_y1.txt`

Example Output
--------------
After running the scripts, you should find the following results:
1. Simulation: A plot of `y1` vs. `y3`, showing the evolution of the chaotic system's state.
2. Bifurcation: A plot and text files with bifurcation points (`svar` and `xmax`).

Optimization
------------
- The package utilizes the Numba JIT compiler for performance optimization.
- Multiprocessing is implemented for the system's bifurcation analysis.

License
-------
The MEXVOFD package is open-source software released under the --MIT License--.

Citation
-------
Bugs, Comments, and Collaborations send email to:
jesusm.pacheco@correo.buap.mx

CITED AS: Unified scientific tool to investigate fractional derivatives of arbitrary variable order with time-memory and order-memory: The MEXVOFD Python package; Daniel Clemente-López, Jesus M. Munoz-Pacheco , José de Jesus Rangel-Magdaleno, April 2025 (pre-print).


