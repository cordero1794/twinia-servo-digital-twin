# Dataset Description

## Overview

This dataset contains experimental measurements collected for the identification and validation of servo motor dynamics used in the quadruped robot **TWINIA**. The data were obtained through controlled laboratory experiments designed to characterize the electrical and mechanical behavior of the actuators responsible for the robot’s locomotion system.

The dataset was created as part of a doctoral research project focused on the development of **Digital Twins and Physical Artificial Intelligence models for mobile robotics**. The primary goal of the dataset is to support the modeling and validation of servo motor dynamics and enable the comparison between simulated and real robotic systems through a **simulation-to-reality (sim-to-real) validation framework**.

The experimental measurements allow the estimation of actuator parameters and the construction of mathematical models that can be integrated into digital twin simulation environments such as **NVIDIA Omniverse**.

---

# Research Context

Robotic simulations are widely used to design control strategies, train artificial intelligence models, and evaluate robotic behaviors before deploying them on physical platforms. However, one of the major challenges in robotics is the **reality gap**, which refers to the difference between simulated models and the real-world behavior of robotic systems.

Digital twin technology offers a promising solution by creating high-fidelity virtual models that replicate the behavior of physical systems. In order to achieve reliable digital twins, accurate models of robot actuators are required.

This dataset contributes to this objective by providing experimental measurements that allow the identification of servo motor dynamics used in the quadruped robot TWINIA. The data support the development and validation of actuator models that can be integrated into robotic simulation environments.

---

# Robot Platform

The dataset was collected using the quadruped robot **TWINIA**, a research robotic platform designed for the study of autonomous locomotion and robotic control.

The robot includes multiple servo motors that control the hip and knee joints of the robot’s legs. These actuators play a critical role in locomotion and must be accurately modeled to ensure realistic simulation results.

The experiments focus on characterizing the dynamic behavior of these servo motors under different excitation inputs.

---

# Data Acquisition

The experimental data were collected using sensors integrated into the robotic platform and external measurement systems. The following signals were recorded during the experiments:

| Variable | Description |
|--------|-------------|
| Time | Timestamp of the recorded measurement |
| Voltage | Electrical supply voltage applied to the servo motor |
| Current | Electrical current consumed by the actuator |
| Angular Position | Measured joint angle |
| Angular Velocity | Estimated rotational velocity of the actuator |
| Torque | Estimated mechanical torque output |

The signals were recorded during controlled excitation tests designed to stimulate the dynamic response of the actuator.

---

# Experimental Protocol

To identify the dynamic characteristics of the servo motors, controlled excitation inputs were applied to the actuators.

The following excitation signals were used:

### Step Input
A sudden change in the actuator command signal to observe transient and steady-state behavior.

### Ramp Input
A gradually increasing command signal used to analyze actuator response over a continuous input variation.

### Chirp Signal
A frequency-sweeping signal used to excite a wide range of dynamic frequencies in the actuator system.

These excitation signals allow the identification of both electrical and mechanical parameters of the servo motor.

---

# Sampling Characteristics

The measurements were collected at sampling frequencies ranging between **100 Hz and 200 Hz**, which allows capturing both slow and fast actuator dynamics.

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

All data files are provided in **CSV (Comma-Separated Values) format**, which ensures compatibility with multiple data analysis tools including:

- Python
- MATLAB
- R
- Excel

Each CSV file contains the following columns:

time, voltage, current, position, velocity, torque


All values are recorded using SI units.

---

# Intended Use

The dataset is intended for research purposes including:

- Servo motor modeling
- System identification
- Robot actuator analysis
- Digital twin development
- Simulation-to-reality validation
- Robotics simulation calibration

Researchers can use this dataset to estimate actuator parameters, build mathematical models, and compare simulation results with real experimental data.

---

# Reproducibility

To support reproducible research, the repository also includes scripts used for:

- Data processing
- Parameter identification
- Visualization of experimental results

These scripts enable researchers to reproduce the modeling process and verify the experimental results.

---

# Limitations

The dataset focuses on servo motors used in the TWINIA quadruped robot and may not represent the behavior of other actuator types. Environmental conditions and mechanical load variations may also influence the recorded measurements.

---

# Acknowledgments

This dataset was generated as part of a doctoral research project on **Digital Twins for Artificial Intelligence in Mobile Robotics**. The work combines experimental robotics, system identification, and simulation technologies to improve the reliability of robotic simulations and facilitate sim-to-real transfer.

---

# Citation

If you use this dataset in your research, please cite:

Cordero Pareja, J. A., López Sotelo, J. A., & Carreño Zagarra, J. J. (2026).  
Experimental Dataset and Servo Motor Modeling for the Quadruped Robot TWINIA.

GitHub Repository.
