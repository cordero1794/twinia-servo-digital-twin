# TWINIA Servo Digital Twin

Experimental dataset and modeling framework for servo motor identification in the quadruped robot **TWINIA**.  
This project supports digital twin development and sim-to-real validation using experimental measurements and integration with NVIDIA Omniverse for robotic system analysis.

---

# Overview

This repository provides the experimental dataset, mathematical modeling framework, and analysis tools used to identify and validate the dynamic behavior of servo motors used in the quadruped robot **TWINIA**.

The work is part of a doctoral research project focused on the development of **Digital Twins and Physical Artificial Intelligence models for mobile robotics**.

The main goal of the project is to reduce the gap between simulated robotic environments and real robotic systems through a systematic **simulation-to-reality (sim-to-real) validation methodology**.

To achieve this objective, controlled experiments were performed on the servo motors responsible for the locomotion system of the robot. Electrical and mechanical variables were recorded and used to estimate the dynamic parameters of the actuators.

The identified models are then integrated into a **digital twin environment in NVIDIA Omniverse**, allowing comparison between simulated robot behavior and the physical platform.

---

# Research Motivation

Simulation environments are widely used in robotics to train control algorithms and artificial intelligence models. However, one of the main challenges in robotics research is the **reality gap**, which refers to the difference between simulated robot behavior and real-world performance.

Digital twin technology provides a powerful solution to this problem by creating a high-fidelity virtual representation of the physical system.

This project contributes to this field by developing an experimentally validated model of the servo motors used in a quadruped robot and integrating this model into a simulation environment.

The resulting framework enables more accurate simulation and improves the reliability of sim-to-real transfer for robotic systems.

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

The identified actuator models are integrated into a **digital twin environment** developed in NVIDIA Omniverse.

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
