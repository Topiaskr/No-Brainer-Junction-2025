import numpy as np
 
#data
time = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31])
all_sleep = np.array([5.09, 8.86, 7.21, 8.24, 5.73, 6.23, 6.34, 6.09, 7.56, 6.66, 6.48, 8.95, 6.53, 5.88, 5.39, 7.49, 5.88, 8.79, 5.67, 5, 7.78, 8.29, 8.54, 7.48, 6.75, 5.63, 7.45, 6.03, 6.62, 7.34, 5.96])
REM = np.array([104, 99, 96, 81, 124, 82, 126, 68, 111, 76, 72, 60, 61, 79, 64, 69, 89, 101, 97, 102, 112, 125, 113, 111, 71, 82, 91, 88, 104, 65, 74])
deep = np.array([106, 102, 81, 108, 66, 109, 82, 75, 51, 53, 82, 108, 46, 63, 98, 42, 70, 95, 76, 55, 94, 77, 48, 60, 90, 91, 107, 75, 88, 66, 110])
light = np.array([244, 290, 295, 240, 238, 195, 196, 275, 291, 293, 281, 278, 196, 241, 209, 247, 236, 203, 194, 283, 236, 234, 204, 298, 232, 206, 216, 181, 189, 273, 185]) 
stress = np.array([92, 106, 111, 71, 118, 89, 91, 61, 111, 70, 74, 76, 96, 80, 116, 98, 57, 110, 61, 84, 120, 107, 84, 57, 117, 62, 84, 82, 95, 118, 66])

#sleep

#sleep means
mean_all_sleep = np.mean(all_sleep)
mean_REM = np.mean(REM)
mean_deep = np.mean(deep)
mean_light = np.mean(light)

#sleep stds
std_all_sleep = np.std(all_sleep)
std_REM = np.std(REM)
std_deep = np.std(deep)
std_light = np.std(light)
 
#stress
mean_stress = np.mean(stress)
std_stress = np.std(stress)
 
#correlation of stress with all sleep
corr_all_sleep_stress = np.corrcoef(all_sleep, stress)[0, 1]
print(corr_all_sleep_stress)