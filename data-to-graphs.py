import matplotlib.pyplot as plt
import numpy as np
import os
from load_data import load_excel_data, get_variable

try:
    data = load_excel_data()
    
    # Map row names to variables
    all_sleep = get_variable(data, ['kokonaisuni', 'uni'])
    REM = get_variable(data, ['rem', 'rem-uni'])
    
    # Check if data was loaded
    if all_sleep is None or len(all_sleep) == 0:
        print("Error: Could not find 'all_sleep' data in Excel file")
        print("Available keys:", list(data.keys())[:10])
        exit()
    
    # Generate x-axis
    days = np.arange(1, len(all_sleep) + 1)
    
    # Create plot
    plt.figure(figsize=(10, 5))
    plt.plot(days, all_sleep, marker='o', label='Total Sleep')
    
    if REM is not None and len(REM) > 0:
        plt.plot(days, REM / 60, marker='x', label='REM (hours)')
    
    plt.title("Sleep Data Over Time")
    plt.xlabel("Day")
    plt.ylabel("Hours")
    plt.grid(True)
    plt.legend()
    
    # Save and display
    plt.savefig("sleep_chart.png", dpi=300)
    plt.close()
    
    print("Saved: sleep_chart.png")
    os.startfile("sleep_chart.png")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
