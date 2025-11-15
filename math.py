import numpy as np
import scipy as sc
from array_data_to_dictionary import list_of_dicts

def is_number(x):
    try:
        float(x)
        return True
    except:
        return False

class SleepStressAnalysis:
    def __init__(self, import_data):
        self.data = {}
        for entry in import_data:
            name = entry.get('name')
            values = entry.get('values', [])
            # Filter only numeric values
            numeric_values = [v for v in values if is_number(v)]
            arr = np.array(numeric_values, dtype=float)
            if arr.ndim == 1 and arr.size > 0:
                self.data[name] = arr
        lengths = [len(arr) for arr in self.data.values()]
        if lengths:
            min_len = min(lengths)
            for k in self.data:
                self.data[k] = self.data[k][:min_len]
            self.all_matrix = np.vstack([self.data[k] for k in self.data])
        else:
            self.all_matrix = np.array([])

    def means(self):
        return {k: np.mean(v) for k, v in self.data.items() if v.size > 0}

    def stds(self):
        return {k: np.std(v) for k, v in self.data.items() if v.size > 0}

    def correlation_sleep_stress(self):
        if "kokonaisuni" in self.data and "stress" in self.data:
            return np.corrcoef(self.data["kokonaisuni"], self.data["stress"])[0, 1]
        return None

    def regression_sleep_stress(self):
        if "kokonaisuni" in self.data and "stress" in self.data:
            slope, intercept, r_value, p_value, std_err = sc.stats.linregress(self.data["kokonaisuni"], self.data["stress"])
            return {
                "slope": slope,
                "intercept": intercept,
                "r_value": r_value,
                "p_value": p_value,
                "std_err": std_err
            }
        return None

    def month_migraine_score(self, matrix, weight):
        if matrix.size == 0:
            return None
        bits = ""
        for array in matrix:
            if np.mean(array) > np.median(array) + weight * np.std(array):
                bits += "1"
            else:
                bits += "0"
        result = 10 * bits.count("1") / len(bits)
        return result

# Use imported data
import_data = list_of_dicts

analysis = SleepStressAnalysis(import_data)

print("Means:", analysis.means())
print("Standard deviations:", analysis.stds())

corr = analysis.correlation_sleep_stress()
if corr is not None:
    print("Correlation (kokonaisuni, stress):", corr)

reg = analysis.regression_sleep_stress()
if reg is not None:
    print("Regression (kokonaisuni, stress):", reg)

std_weight = 0.2
migraine_score = analysis.month_migraine_score(analysis.all_matrix, std_weight)
if migraine_score is not None:
    print("Month migraine score:", migraine_score)
