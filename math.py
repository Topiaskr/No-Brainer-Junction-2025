import numpy as np
import scipy as sc
from array_data_to_dictionary import list_of_dicts

class SleepStressAnalysis:
    def __init__(self, import_data):
        # Convert array of dicts to a single dict of arrays
        self.data = {}
        for entry in import_data:
            for k, v in entry.items():
                self.data[k] = v
        # Build matrix for selected keys (excluding 'time')
        keys = [k for k in self.data.keys() if k != "time"]
        self.all_matrix = np.vstack([self.data[k] for k in keys])

    def means(self):
        return {k: np.mean(v) for k, v in self.data.items() if k != "time"}

    def stds(self):
        return {k: np.std(v) for k, v in self.data.items() if k != "time"}

    def correlation_sleep_stress(self):
        if "all_sleep" in self.data and "stress" in self.data:
            return np.corrcoef(self.data["all_sleep"], self.data["stress"])[0, 1]
        return None

    def regression_sleep_stress(self):
        if "all_sleep" in self.data and "stress" in self.data:
            slope, intercept, r_value, p_value, std_err = sc.stats.linregress(self.data["all_sleep"], self.data["stress"])
            return {
                "slope": slope,
                "intercept": intercept,
                "r_value": r_value,
                "p_value": p_value,
                "std_err": std_err
            }
        return None

    def month_migraine_score(self, matrix, weight):
        bits = ""
        for array in matrix:
            if np.mean(array) > np.median(array) + weight * np.std(array):
                bits += "1"
            else:
                bits += "0"
        result = 10 * bits.count("1") / len(bits)
        return result

# Example import_data (as in your original code)
import_data = list_of_dicts

# Example usage
analysis = SleepStressAnalysis(import_data)

print("Means:", analysis.means())
print("Standard deviations:", analysis.stds())

corr = analysis.correlation_sleep_stress()
if corr is not None:
    print("Correlation (all_sleep, stress):", corr)

reg = analysis.regression_sleep_stress()
if reg is not None:
    print("Regression (all_sleep, stress):", reg)

std_weight = 0.1
print("Month migraine score:", analysis.month_migraine_score(analysis.all_matrix, std_weight))