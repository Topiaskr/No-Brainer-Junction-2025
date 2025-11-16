import matplotlib.pyplot as plt
import scores_and_results

# Example: Plot means from results
variables = list(scores_and_results.means.keys())
mean_values = list(scores_and_results.means.values())

plt.figure(figsize=(12, 6))
plt.bar(variables, mean_values)
plt.xticks(rotation=90)
plt.title("Mean Values from Results")
plt.ylabel("Mean")
plt.tight_layout()
plt.show()

# Example: Plot standard deviations from results
std_values = list(scores_and_results.stds.values())

plt.figure(figsize=(12, 6))
plt.bar(variables, std_values)
plt.xticks(rotation=90)
plt.title("Standard Deviations from Results")
plt.ylabel("Standard Deviation")
plt.tight_layout()
plt.show()

# Example: Use a score variable
if hasattr(scores_and_results, 'rem_all_sleep_ratio'):
    print("REM/All Sleep Ratio:", scores_and_results.rem_all_sleep_ratio)

# You can use any variable from results.py in your plots or calculations
