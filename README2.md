# TWINIA Servo Digital Twin

Experimental dataset and modeling framework for servo motor identification in the quadruped robot **TWINIA**.  
This project supports digital twin development and sim-to-real validation using experimental measurements and integration with NVIDIA Omniverse Isaac Sim for robotic system analysis.

---

# Overview

This repository provides the experimental dataset, mathematical modeling framework, and analysis tools used to identify and validate the dynamic behavior of servo motors used in the quadruped robot **TWINIA**.

The work is part of a doctoral research project focused on the development of **Digital Twins and Physical Artificial Intelligence models for mobile robotics**.

The main goal of the project is to reduce the gap between simulated robotic environments and real robotic systems through a systematic **simulation-to-reality (sim-to-real) validation methodology**.

To achieve this objective, the research followed a multi-stage process including theoretical modeling, experimental approximation, simulation validation, and hardware improvements to the physical robot platform.

---

# Research Motivation

Simulation environments are widely used in robotics to train control algorithms and artificial intelligence models. However, one of the main challenges in robotics research is the **reality gap**, which refers to the difference between simulated robot behavior and real-world performance.

Digital twin technology provides a powerful solution to this problem by creating a high-fidelity virtual representation of the physical system.

This project contributes to this field by developing an experimentally validated model of the servo motors used in a quadruped robot and integrating this model into a simulation environment.

The resulting framework enables more accurate simulation and improves the reliability of sim-to-real transfer for robotic systems.

---

# Development Process

The research conducted during the doctoral internship was developed in several stages.

### 1. Theoretical Mathematical Modeling

The first stage focused on the **theoretical development of the mathematical model of the servo motors** used in the locomotion system of the quadruped robot.

Electrical and mechanical characteristics of the actuators were analyzed in order to derive a mathematical representation describing the dynamic response of the servo motors.

---

### 2. Parameter Approximation Using Real Robot Data

After defining the theoretical model, the next stage involved **approximating the model parameters using measurements obtained from the real quadruped robot**.

Experimental data allowed the adjustment of the mathematical model so that it accurately represented the behavior of the physical actuators.

---

### 3. Simulation and Digital Twin Validation

Once the mathematical model was validated, it was integrated into the **digital twin simulation environment using NVIDIA Omniverse Isaac Sim**.

This stage allowed the comparison between the expected behavior of the simulated robot and the physical robotic platform.

During the simulation process, it was observed that the simulated robot required **higher electrical current consumption than the real robot could safely provide**.

Specifically, the simulation indicated that the robot could demand **more than 8 amperes**, which exceeds the safe current capacity of the physical robot platform.

---

### 4. Hardware Improvement of the Physical Robot

Based on the simulation results, an improvement to the robot's electrical power system was proposed.

The solution involved the integration of **supercapacitors** to support peak current demands during locomotion.

Additionally, **INA current sensing modules (INA219)** were incorporated to monitor voltage drops and current consumption in real time.

This monitoring system allows detection of voltage drops and helps prevent power instability in the robot.

---

# Robot Platform

The experiments were conducted on the quadruped robot **TWINIA**, a research platform designed for the study of autonomous locomotion and robotic perception.

The robot includes:

- Multiple servo motors controlling hip and knee joints
- Embedded control systems
- Electrical sensing for current and voltage monitoring
- Sensors for measuring joint position and motion

The locomotion system relies on servo actuators that must be accurately modeled to ensure realistic simulation.

---

# Experimental Dataset

The repository contains experimental measurements collected during controlled excitation tests applied to the robot's servo motors.

The dataset includes the following variables:

| Variable | Description |
|--------|-------------|
| Time | Time stamp of measurement |
| Voltage | Supply voltage applied to the actuator |
| Current | Electrical current consumed by the servo |
| Angular Position | Measured joint position |
| Angular Velocity | Estimated rotational speed |
| Torque | Estimated mechanical torque |

The data were collected using sensors and measurement systems integrated into the robot platform.

---

# Experimental Protocol

To identify the dynamic characteristics of the servo motors, controlled excitation signals were applied to the actuators.

The following excitation inputs were used:

- Step signals
- Ramp signals
- Chirp signals

These tests allow the identification of both electrical and mechanical parameters of the servo motor system.

The recorded data are used for:

- Parameter estimation
- System identification
- Model validation
- Simulation comparison

---

# Digital Twin Integration

The identified actuator models are integrated into a **digital twin environment** developed in **NVIDIA Omniverse Isaac Sim**.

The digital twin allows simulation of the robot under realistic conditions and enables comparison between simulated and real robot behavior.

The validation process includes evaluation using quantitative performance metrics such as:

- Root Mean Square Error (RMSE)
- Signal correlation
- Energy consumption analysis
- Locomotion performance indicators

This approach enables the development of more accurate robotic simulations.

---

# Repository Structure

The repository is organized as follows:
dataset/
Experimental measurements recorded during servo motor tests

scripts/
Python scripts used for data processing and parameter identification

models/
Mathematical models of the servo motors

figures/
Plots and validation results comparing simulation and real robot behavior

docs/
Dataset documentation and experimental description


---

# Applications

This repository may be useful for researchers working in the following areas:

- Digital Twins
- Quadruped Robotics
- Robot Dynamics
- Actuator Modeling
- System Identification
- Simulation-to-Reality Transfer
- Experimental Robotics

The dataset and modeling tools enable reproducible research in robotic system identification and digital twin validation.

---

# Dataset Availability

The experimental dataset provided in this repository is released in open CSV format to support transparency and reproducibility in robotics research.

The dataset contains measurements recorded during laboratory experiments performed on the quadruped robot TWINIA.

---

# Citation

If you use this dataset or code in your research, please cite:

Cordero Pareja, J. A., López Sotelo, J. A., & Carreño Zagarra, J. J. (2026)  
Experimental Dataset and Servo Motor Modeling for the Quadruped Robot TWINIA.

Dataset DOI (to be generated through Zenodo)

---

# Author

Jhonattan Alexander Cordero Pareja  
Doctoral Researcher in Engineering

## Co-Authors

Jesús Alfonso López Sotelo  
Director of Doctoral Thesis  
Universidad Autónoma del Occidente (UAO)

José Jorge Carreño Zagarra  
Research Tutor – Doctoral Internship  
Universidad Industrial de Santander (UIS)

Research Area:

- Robotics
- Digital Twins
- Artificial Intelligence for Autonomous Systems

---

# License

This project is released under the MIT License.

---

# Acknowledgments

This work was developed as part of a doctoral research project focused on the development of **Digital Twins for Artificial Intelligence in Mobile Robotics**.

The research integrates experimental robotics, system identification, simulation technologies, and hardware improvements to enhance the reliability of robotic simulations and improve the energy performance of the physical robotic platform.
