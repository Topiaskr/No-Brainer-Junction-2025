#pip install matplotlib
#pip install numpy
#pip install os
#pip install pandas

import matplotlib.pyplot as plt
import numpy as np
import os

# --- your data ---
all_sleep = np.array([5.09, 8.86, 7.21, 8.24, 5.73, 6.23, 6.34, 6.09, 7.56, 6.66,
                      6.48, 8.95, 6.53, 5.88, 5.39, 7.49, 5.88, 8.79, 5.67, 5.00,
                      7.78, 8.29, 8.54, 7.48, 6.75, 5.63, 7.45, 6.03, 6.62, 7.34,
                      5.96])

# Generate x-axis (1..31)
days = np.arange(1, len(all_sleep) + 1)

# --- Plot the chart locally ---
plt.figure(figsize=(10, 5))
plt.plot(days, all_sleep, marker='o')
plt.title("All Sleep Values Over Time")
plt.xlabel("Day")
plt.ylabel("Sleep Duration (hours)")
plt.grid(True)

# --- Save to PNG file ---
plt.savefig("sleep_chart.png", dpi=300)
plt.close()

print("Saved: sleep_chart.png")
os.startfile("sleep_chart.png")
