import matplotlib.pyplot as plt

V_forward = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.5, 0.5, 0.6, 0.6, 0.7, 0.7, 0.7]
I_forward = [0, 0, 0, 0, 0, 0.1, 0.2, 0.3, 1.3, 4.3, 9.4, 14.5, 19.5]

V_reverse = [1.95, 4.95, 10.03, 15.12, 20.16]
I_reverse = [0, 0, 0, 0, 0]

plt.figure(figsize=(8,6))

plt.plot(V_forward, I_forward, 'o-', color='blue', label='Forward Bias')

plt.plot(V_reverse, I_reverse, 's-', color='red', label='Reverse Bias')

plt.title("I-V Characteristics of a Diode (Measured)")
plt.xlabel("Voltage (V)")
plt.ylabel("Current (mA)")
plt.grid(True, linestyle='--', linewidth=0.6)
plt.legend()
plt.show()
