from math_stuff import analysis

# Basic statistics
means = analysis.means()
stds = analysis.stds()
mins = analysis.min_values()
maxs = analysis.max_values()
medians = analysis.median_values()
quantiles = analysis.quantiles()
ranges = analysis.value_ranges()
summary = analysis.summary_stats()

# Specific variables
rem_mean = analysis.REM_mean()
deep_mean = analysis.deep_mean()
steps_mean = analysis.steps_mean()
period_mean = analysis.period_mean()

# Combination functions
rem_all_sleep_ratio = analysis.rem_to_all_sleep_ratio()
deep_all_sleep_ratio = analysis.deep_to_all_sleep_ratio()
sleep_stress_bpm_corr = analysis.sleep_stress_bpm_correlation()
total_activity = analysis.total_activity()
avg_stress = analysis.avg_stress_combined()
skin_temp_range = analysis.skin_temp_range()
high_sleep_eff_pct = analysis.sleep_efficiency_high_pct()
calories_per_step = analysis.calocies_per_step()