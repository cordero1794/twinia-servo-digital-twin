# Dataset Description

## Overview

This dataset contains experimental measurements collected for the identification and validation of servo motor dynamics used in the quadruped robot **TWINIA**. The data were obtained through controlled laboratory experiments designed to characterize the electrical and mechanical behavior of the actuators responsible for the robot’s locomotion system.

The dataset was developed as part of a doctoral research project focused on **Digital Twins and Physical Artificial Intelligence models for mobile robotics**. The primary objective is to support the modeling, validation, and improvement of servo motor models used in the locomotion system of the robot.

The collected data allow the estimation of actuator parameters and the construction of mathematical models that can be integrated into digital twin simulation environments such as **NVIDIA Omniverse Isaac Sim**.

---

# Research Context

Robotic simulations are widely used to design control strategies, train artificial intelligence models, and evaluate robotic behaviors before deploying them on physical platforms. However, one of the main challenges in robotics research is the **reality gap**, which refers to the difference between simulated models and the real-world behavior of robotic systems.

Digital twin technology offers a promising solution by creating high-fidelity virtual models that replicate the behavior of physical systems. To achieve reliable digital twins, accurate actuator models are required.

This dataset contributes to reducing the simulation-reality gap by providing experimental measurements that enable the identification and validation of servo motor dynamics used in the quadruped robot TWINIA.

---

# Development Methodology

The dataset was generated during several stages of the doctoral research process.

### 1. Theoretical Mathematical Modeling

The first stage focused on developing the **theoretical mathematical model of the servo motors** used in the locomotion system of the robot. Electrical and mechanical characteristics of the actuators were analyzed to derive a dynamic model describing their behavior.

### 2. Parameter Approximation Using Real Robot Measurements

After the theoretical model was defined, the model parameters were adjusted using **measurements obtained from the physical quadruped robot**. This step allowed the model to better represent the real behavior of the actuators.

### 3. Simulation and Digital Twin Validation

Once the mathematical model was validated, it was integrated into the **digital twin simulation environment using NVIDIA Omniverse Isaac Sim**.

During simulation tests, it was observed that the robot could demand **electrical currents higher than 8 amperes**, which exceeds the safe current capacity of the physical robot platform.

### 4. Hardware Improvement

Based on the simulation results, improvements to the robot's electrical system were proposed. The solution included the integration of:

- **Supercapacitors** to support peak current demand
- **INA current sensing modules (INA219)** to monitor current consumption and detect voltage drops in real time

This improvement helps prevent voltage instability and improves energy management in the robotic platform.

---

# Robot Platform

The dataset was collected using the quadruped robot **TWINIA**, a research robotic platform designed for the study of autonomous locomotion and robotic control.

The robot includes:

- Multiple servo motors controlling hip and knee joints
- Embedded microcontroller-based control system
- Electrical sensors for monitoring current and voltage
- Sensors for measuring joint position and motion

The locomotion system relies on servo actuators that must be accurately modeled to ensure realistic simulation results.

---

# Data Acquisition

The experimental data were collected using sensors integrated into the robotic platform and external measurement systems.

The following signals were recorded during the experiments:

| Variable | Description |
|--------|-------------|
| Time | Timestamp of the recorded measurement |
| Voltage | Electrical supply voltage applied to the servo motor |
| Current | Electrical current consumed by the actuator |
| Angular Position | Measured joint angle |
| Angular Velocity | Estimated rotational velocity |
| Torque | Estimated mechanical torque output |

These signals were recorded during controlled excitation experiments designed to stimulate the dynamic response of the actuator.

---

# Experimental Protocol

To identify the dynamic characteristics of the servo motors, controlled excitation signals were applied.

The following excitation signals were used:

### Step Input
A sudden change in the actuator command signal used to observe transient and steady-state behavior.

### Ramp Input
A gradually increasing command signal used to analyze actuator response across a continuous input variation.

### Chirp Signal
A frequency-sweeping signal used to excite a wide range of dynamic frequencies in the actuator system.

These experiments enable the identification of both electrical and mechanical parameters of the servo motor system.

---

# Sampling Characteristics

The measurements were collected at sampling frequencies ranging between **100 Hz and 200 Hz**, allowing the capture of both slow and fast actuator dynamics.

Each experiment contains time-series data representing the actuator response under specific excitation conditions.

---

# Dataset Structure

The dataset is organized as follows:
dataset/
servo_test_step_01.csv
servo_test_ramp_01.csv
servo_test_chirp_01.csv
servo_test_step_02.csv


Each file corresponds to an experimental test and contains time-series measurements of the actuator variables.

---

# File Format

All data files are provided in **CSV (Comma-Separated Values) format**, ensuring compatibility with multiple analysis tools including:

- Python
- MATLAB
- R
- Excel

Each CSV file contains the following columns:
time, voltage, current, position, velocity, torque


All variables are expressed in **SI units**.

---

# Intended Use

The dataset can be used for research in the following areas:

- Servo motor modeling
- System identification
- Robot actuator analysis
- Digital twin development
- Simulation-to-reality validation
- Robotics simulation calibration

Researchers may use this dataset to estimate actuator parameters, build mathematical models, and compare simulation results with experimental data.

---

# Reproducibility

To support reproducible research, the repository also includes scripts used for:

- Data preprocessing
- Parameter identification
- Visualization of experimental results

These scripts allow researchers to reproduce the modeling process and verify the experimental results.

---

# Limitations

The dataset focuses on servo motors used in the quadruped robot TWINIA and may not represent the behavior of other actuator types or robotic platforms. Environmental conditions, mechanical loads, and hardware variations may influence the recorded measurements.

---

# Acknowledgments

This dataset was generated as part of a doctoral research project focused on **Digital Twins for Artificial Intelligence in Mobile Robotics**.

The research integrates theoretical modeling, experimental robotics, digital twin simulation, and hardware improvements to enhance the reliability of robotic simulations and improve the energy performance of the physical robotic platform.

---

# Citation

If you use this dataset in your research, please cite:

Cordero Pareja, J. A., López Sotelo, J. A., & Carreño Zagarra, J. J. (2026).  
Experimental Dataset and Servo Motor Modeling for the Quadruped Robot TWINIA.  
GitHub Repository.
