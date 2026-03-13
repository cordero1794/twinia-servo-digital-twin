# Electro–Mechanical Mathematical Model of the Servo System

## Overview

This document describes the electro–mechanical mathematical model developed for the servo motor system of the quadruped robot **TWINIA**. The model was designed to support digital twin simulations and energy analysis of the robot during locomotion.

The robot uses **12 MG996 servo motors**, with **three actuators per leg**, powered through a shared electrical bus. All servos are supplied by a **Li-Po 2S battery (7.4 V nominal)** connected to a **DC-DC buck converter regulated at 5 V**.

Since all actuators share the same power bus, simultaneous motor loads during locomotion can generate current peaks and transient voltage drops. These effects must be modeled to analyze the energetic behavior of the system and to enable accurate simulation within the digital twin environment.

---

# 1. Electro–Mechanical Servo Model

Although the MG996 servo includes an internal position controller, for digital twin and energy analysis purposes the actuator can be approximated using an equivalent **DC motor model coupled to a mechanical load**.

This approximation allows modeling the relationship between electrical consumption and mechanical demand.

---

# 2. Electrical Model of the Motor

The electrical dynamics of the servo motor can be described by the classical DC motor equation:

$$
V = L \frac{di}{dt} + Ri + K_e \omega
$$

Where:

- $V$ = voltage applied to the motor  
- $i$ = motor current  
- $R$ = armature resistance  
- $L$ = armature inductance  
- $K_e$ = back electromotive force constant  
- $\omega$ = angular velocity of the motor shaft  

This equation describes how the current evolves depending on the applied voltage and the rotational speed.

---

# 3. Mechanical Model

The mechanical dynamics of the actuator are described by:

$$
J \frac{d\omega}{dt} + B\omega = K_t i - \tau_{load}
$$

Where:

- $J$ = equivalent rotor inertia  
- $B$ = viscous friction coefficient  
- $K_t$ = torque constant  
- $i$ = motor current  
- $\tau_{load}$ = load torque produced by the robot dynamics  

This equation describes the relationship between current consumption and the torque required to move the robot joint.

---

# 4. Integrated Electro–Mechanical Model

Combining the electrical and mechanical equations results in a coupled system describing the actuator dynamics.

This integrated model captures the relationship between:

- electrical supply voltage  
- current consumption  
- actuator velocity  
- mechanical torque  

The model allows analyzing how mechanical loads affect electrical behavior and vice versa.

---

# 5. Aggregated Robot Model (12 Servos)

The quadruped robot uses **12 servo motors connected in parallel to the same power bus**.

If $i_k$ represents the current consumed by servo $k$, the total current drawn from the power bus is:

$$
I_{total} = \sum_{k=1}^{12} i_k
$$

For each actuator, the current is approximately proportional to the required mechanical torque:

$$
i_k \approx \frac{\tau_k}{K_t}
$$

During quadruped locomotion, the load torque $\tau_k$ varies dynamically due to:

- foot contact  
- ground impact  
- posture stabilization  
- gait transitions  

These events may cause **simultaneous current peaks in multiple actuators**.

---

# 6. Power Bus Model

The servo motors are powered through a **shared 5 V power bus** provided by a buck converter.

However, the effective voltage delivered to the servos can decrease due to internal resistance and transient loads.

---

## 6.1 First-Order Resistive Model

The voltage delivered to the servos can be approximated by:

$$
V_{bus} = V_{buck} - R_{eq} I_{total}
$$

Where:

- $V_{buck}$ = nominal output voltage of the DC-DC converter (5 V)  
- $R_{eq}$ = equivalent resistance of the power distribution system  
- $I_{total}$ = total current consumed by the servos  

This model captures voltage drop due to wiring, connectors, regulator resistance, and PCB traces.

---

## 6.2 Capacitive Support Model

To better represent voltage transients during current peaks, a bus capacitance $C_{bus}$ is introduced.

This capacitance represents the combined effect of:

- power bus capacitors  
- wiring capacitance  
- additional supercapacitor support  

The dynamic behavior of the bus voltage can be approximated as:

$$
C_{bus}\frac{dV}{dt} = I_{supply} - I_{total}
$$

This model captures short-term voltage fluctuations during actuator transients.

---

# 7. Sim-to-Real Validation Metrics

To validate the digital twin against the physical robot, several quantitative metrics were defined.

### Minimum Bus Voltage

$$
V_{min} = \min(V_{bus}(t))
$$

### Maximum Voltage Drop

$$
\Delta V = V_{nominal} - V_{min}
$$

### Current Peaks

- Maximum current  
- 95th percentile current  

### Stability Time

Time during which the bus voltage remains below a defined threshold.

### Average Power Consumption

$$
P_{avg} = \frac{1}{T} \int_0^T V_{bus}(t)\, I_{total}(t)\, dt
$$

These metrics allow comparing:

- Base physical prototype  
- Digital twin simulation (Isaac Sim / Omniverse)  
- Improved physical prototype  

---

# 8. Digital Twin Implementation

In **NVIDIA Omniverse Isaac Sim**, the following variables can be obtained for each joint:

- angular position  
- angular velocity  
- torque  

Using these variables, the actuator current can be estimated as:

$$
i = \frac{\tau}{K_t}
$$

The total bus current becomes:

$$
I_{total} = \sum_{k=1}^{12} i_k
$$

This approach extends the digital twin from a purely mechanical representation toward an **energy-aware digital twin capable of predicting power consumption and voltage drops**.

---

# References

Leonhard, W. (2001). *Control of Electrical Drives*. Springer.

Spong, M. W., Hutchinson, S., & Vidyasagar, M. (2006). *Robot Modeling and Control*. John Wiley & Sons.

Åström, K. J., & Murray, R. M. (2010). *Feedback Systems: An Introduction for Scientists and Engineers*. Princeton University Press.

Boldea, I. (2016). *Electric Machines: Steady State, Transients, and Control*. CRC Press.

Zhang, Y., Yang, J., & Yu, J. (2015). Dynamic modeling and parameter identification of DC motors using least squares method.

Corke, P., Haviland, J., & Wingate, D. (2020). A tutorial on robot simulation. IEEE Robotics and Automation Magazine.

Semini, C., Tsagarakis, N. G., Guglielmino, E., Focchi, M., Cannella, F., & Caldwell, D. G. (2011). Design of HyQ – A hydraulically and electrically actuated quadruped robot.

Hwangbo, J., Lee, J., & Hutter, M. (2019). Per-contact iteration method for solving contact dynamics.

Mirbod, O., & Choi, D. (2025). From simulation to field validation: A digital twin-driven sim-to-real transfer approach.
