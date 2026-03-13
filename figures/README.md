# Experimental Results and Visualization

The figures generated from the dataset provide a visual representation of the dynamic behavior of the servo motors used in the quadruped robot **TWINIA**. These plots illustrate the electrical and mechanical responses of the actuators under different excitation signals, allowing the evaluation of actuator performance and supporting the validation of the mathematical model developed during the doctoral internship.

The plots are automatically generated using the analysis scripts included in the repository and are stored in the **figures/** directory.

---

## Step Response Analysis

![Step Response](figures/servo_test_step_01_current.png)

The step response plots illustrate the actuator behavior when a sudden change in the control input is applied to the servo motor. These graphs are used to analyze the transient dynamics of the actuator, including rise time, stabilization time, and the initial current demand required to move the robot joint.

The step experiment provides important insights into the dynamic response of the actuator and helps estimate key parameters of the servo motor model used in the digital twin simulation.

---

## Ramp Response Analysis

![Ramp Response](figures/servo_test_ramp_01_current.png)

The ramp response plots represent the behavior of the servo motor when the input signal increases gradually over time. This type of excitation simulates smooth joint movements similar to those that occur during locomotion.

Ramp tests allow the evaluation of velocity tracking performance, actuator stability during continuous motion, and the electrical power consumption associated with gradual joint displacement.

These results are important for validating the actuator model under realistic robotic motion conditions.

---

## Chirp Excitation Analysis

![Chirp Response](figures/servo_test_chirp_01_current.png)

The chirp excitation plots show the response of the servo motor when subjected to a frequency sweep signal. In this test, the frequency of the input signal increases progressively, allowing the actuator to be excited across a wide range of dynamic frequencies.

This experiment is particularly useful for identifying the frequency response characteristics of the actuator and detecting possible resonant behaviors. The results contribute to improving the accuracy of the actuator model used in the digital twin environment.

---

## Combined System Behavior

![Combined Variables](figures/servo_test_step_01_combined.png)

The combined plots show the relationship between several measured variables, including voltage, current consumption, joint position, angular velocity, and estimated torque. By analyzing these variables simultaneously, it is possible to better understand the interaction between the electrical and mechanical components of the actuator system.

These visualizations support the evaluation of the overall system performance and provide evidence for the validation of the digital twin model.

---

## Energy Behavior and Power Analysis

During the simulation stage carried out in NVIDIA Omniverse Isaac Sim, the robot exhibited current demands that exceeded the power capabilities of the physical platform. The experimental plots reveal how current consumption evolves during different actuator excitations.

To address this limitation, an energy improvement strategy based on **supercapacitors and INA219 current monitoring sensors** was proposed. This approach allows the detection of voltage drops and improves power stability during high dynamic loads.

---

## Reproducibility

All figures can be reproduced automatically by running the analysis script:

```bash
python scripts/plot_servo_results.py
