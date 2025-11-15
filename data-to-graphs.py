import matplotlib.pyplot as plt
import numpy as np
import os
import json


# Load the list of dictionaries from array_data_to_dictionary
with open("array_data_list.json", "r", encoding="utf-8") as f:
    data_list = json.load(f)

# Find 'kokonaisuni' (all_sleep) from the list
all_sleep = None
for item in data_list:
    if "kokonaisuni" in item["name"].lower():
        all_sleep = np.array(item["values"])
        break

if all_sleep is None:
    print("Error: 'kokonaisuni' not found in array_data_list.json")
    print("Available keys:")
    for item in data_list[:10]:
        print(f"  - {item['name']}")
else:
    # Generate x-axis (1..N)
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
    try:
        os.startfile("sleep_chart.png")
    except Exception:
        pass
