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
         
# ...existing code...

    def min_values(self):
        """Return the minimum value for each variable."""
        return {k: np.min(v) for k, v in self.data.items() if v.size > 0}

    def max_values(self):
        """Return the maximum value for each variable."""
        return {k: np.max(v) for k, v in self.data.items() if v.size > 0}

    def median_values(self):
        """Return the median value for each variable."""
        return {k: np.median(v) for k, v in self.data.items() if v.size > 0}

    def quantiles(self, q=[0.25, 0.5, 0.75]):
        """Return specified quantiles for each variable."""
        return {k: np.quantile(v, q) for k, v in self.data.items() if v.size > 0}

    def value_ranges(self):
        """Return the range (max-min) for each variable."""
        return {k: np.ptp(v) for k, v in self.data.items() if v.size > 0}

    def summary_stats(self):
        """Return a summary of stats for each variable."""
        return {
            k: {
                "mean": np.mean(v),
                "std": np.std(v),
                "min": np.min(v),
                "max": np.max(v),
                "median": np.median(v),
                "range": np.ptp(v)
            }
            for k, v in self.data.items() if v.size > 0
        }

# ...existing code...
        # SLEEP
    def all_sleep_mean(self): return np.mean(self.data.get('all_sleep')) if 'all_sleep' in self.data else None
    def REM_mean(self): return np.mean(self.data.get('REM')) if 'REM' in self.data else None
    def deep_mean(self): return np.mean(self.data.get('deep')) if 'deep' in self.data else None
    def light_mean(self): return np.mean(self.data.get('light')) if 'light' in self.data else None
    def sleep_duration_mean(self): return np.mean(self.data.get('sleep_duration')) if 'sleep_duration' in self.data else None
    def wake_up_mean(self): return np.mean(self.data.get('wake_up')) if 'wake_up' in self.data else None
    def sleep_rhythm_mean(self): return np.mean(self.data.get('sleep_rhythm')) if 'sleep_rhythm' in self.data else None
    def sleep_efficiency_mean(self): return np.mean(self.data.get('sleep_efficiency')) if 'sleep_efficiency' in self.data else None
    def sleep_disturbance_mean(self): return np.mean(self.data.get('sleep_disturbance')) if 'sleep_disturbance' in self.data else None
    def sleep_points_mean(self): return np.mean(self.data.get('sleep_points')) if 'sleep_points' in self.data else None

    # STRESS & HEART
    def stress_bpm_mean(self): return np.mean(self.data.get('stress_bpm')) if 'stress_bpm' in self.data else None
    def bpm_change_mean(self): return np.mean(self.data.get('bpm_change')) if 'bpm_change' in self.data else None
    def RHR_mean(self): return np.mean(self.data.get('RHR')) if 'RHR' in self.data else None
    def bpm_mean(self): return np.mean(self.data.get('bpm')) if 'bpm' in self.data else None
    def breath_depth_mean(self): return np.mean(self.data.get('breath_depth')) if 'breath_depth' in self.data else None
    def stress_index_mean(self): return np.mean(self.data.get('stress_index')) if 'stress_index' in self.data else None
    def recovery_mean(self): return np.mean(self.data.get('recovery')) if 'recovery' in self.data else None
    def skin_temp_mean(self): return np.mean(self.data.get('skin_temp')) if 'skin_temp' in self.data else None

    # ACTIVITY
    def steps_mean(self): return np.mean(self.data.get('steps')) if 'steps' in self.data else None
    def move_efficiency_mean(self): return np.mean(self.data.get('move_efficiency')) if 'move_efficiency' in self.data else None
    def distance_mean(self): return np.mean(self.data.get('distance')) if 'distance' in self.data else None
    def hours_standing_mean(self): return np.mean(self.data.get('hours_standing')) if 'hours_standing' in self.data else None
    def activity_mean(self): return np.mean(self.data.get('activity')) if 'activity' in self.data else None
    def calocies_mean(self): return np.mean(self.data.get('calocies')) if 'calocies' in self.data else None
    def excercises_mean(self): return np.mean(self.data.get('excercises')) if 'excercises' in self.data else None

    # DAILY
    def skin_mean(self): return np.mean(self.data.get('skin')) if 'skin' in self.data else None
    def EDA_mean(self): return np.mean(self.data.get('EDA')) if 'EDA' in self.data else None
    def bpm_areas_mean(self): return np.mean(self.data.get('bpm_areas')) if 'bpm_areas' in self.data else None
    def daily_stress_mean(self): return np.mean(self.data.get('daily_stress')) if 'daily_stress' in self.data else None

    # HORMONES
    def period_mean(self): return np.mean(self.data.get('period')) if 'period' in self.data else None
    def ovulation_mean(self): return np.mean(self.data.get('ovulation')) if 'ovulation' in self.data else None

    # Example: add std, min, max, median, quantiles for one variable
    def all_sleep_std(self): return np.std(self.data.get('all_sleep')) if 'all_sleep' in self.data else None
    def all_sleep_min(self): return np.min(self.data.get('all_sleep')) if 'all_sleep' in self.data else None
    def all_sleep_max(self): return np.max(self.data.get('all_sleep')) if 'all_sleep' in self.data else None
    def all_sleep_median(self): return np.median(self.data.get('all_sleep')) if 'all_sleep' in self.data else None
    def all_sleep_quantiles(self, q=[0.25, 0.5, 0.75]): 
        arr = self.data.get('all_sleep')
        return np.quantile(arr, q) if arr is not None and arr.size > 0 else None
# ...existing code...

    # Ratio of REM to total sleep
    def rem_to_all_sleep_ratio(self):
        rem = self.data.get('REM')
        all_sleep = self.data.get('all_sleep')
        if rem is not None and all_sleep is not None and all_sleep.size > 0:
            return np.mean(rem / all_sleep)
        return None

    # Ratio of deep sleep to total sleep
    def deep_to_all_sleep_ratio(self):
        deep = self.data.get('deep')
        all_sleep = self.data.get('all_sleep')
        if deep is not None and all_sleep is not None and all_sleep.size > 0:
            return np.mean(deep / all_sleep)
        return None

    # Correlation between sleep and stress bpm
    def sleep_stress_bpm_correlation(self):
        all_sleep = self.data.get('all_sleep')
        stress_bpm = self.data.get('stress_bpm')
        if all_sleep is not None and stress_bpm is not None and all_sleep.size > 0 and stress_bpm.size > 0:
            return np.corrcoef(all_sleep, stress_bpm)[0, 1]
        return None

    # Sum of steps and activity
    def total_activity(self):
        steps = self.data.get('steps')
        activity = self.data.get('activity')
        if steps is not None and activity is not None and steps.size > 0 and activity.size > 0:
            return np.sum(steps) + np.sum(activity)
        return None

    # Average daily stress and stress index
    def avg_stress_combined(self):
        daily_stress = self.data.get('daily_stress')
        stress_index = self.data.get('stress_index')
        if daily_stress is not None and stress_index is not None and daily_stress.size > 0 and stress_index.size > 0:
            return (np.mean(daily_stress) + np.mean(stress_index)) / 2
        return None

    # Difference between max and min skin temperature
    def skin_temp_range(self):
        skin_temp = self.data.get('skin_temp')
        if skin_temp is not None and skin_temp.size > 0:
            return np.max(skin_temp) - np.min(skin_temp)
        return None

    # Percentage of sleep efficiency above 85%
    def sleep_efficiency_high_pct(self, threshold=85):
        sleep_efficiency = self.data.get('sleep_efficiency')
        if sleep_efficiency is not None and sleep_efficiency.size > 0:
            return np.sum(sleep_efficiency > threshold) / sleep_efficiency.size * 100
        return None

    # Ratio of calories to steps
    def calocies_per_step(self):
        calocies = self.data.get('calocies')
        steps = self.data.get('steps')
        if calocies is not None and steps is not None and steps.size > 0 and calocies.size > 0:
            return np.mean(calocies / steps)
        return None

# ...existing code...
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