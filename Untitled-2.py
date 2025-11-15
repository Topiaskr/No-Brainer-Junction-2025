import numpy as np
import pandas as pd
import scipy as sc

df = pd.read_excel(r"C:\Users\makel\Desktop\Test.xlsx", sheet_name="DataSet_3")

data_arrays = {}

for idx, row in df.iterrows():
    first_cell = row.iloc[0]   # <-- toimii aina riippumatta sarakenimistä

    # ohita tyhjät rivit
    if pd.isna(first_cell):
        continue

    row_name = first_cell

    # datan sarakkeet 1 -> loppuun
    data_row_raw = row.iloc[1:].to_numpy()

    # säilytä aikamerkkijonot ja muut ei-numeraaliset sarjat sellaisenaan
    rn = str(row_name).lower()
    keep_strings = any(k in rn for k in [
        'nukaht', 'herää', 'heraa', 'start', 'wake', 'aika', 'time', 'kellon', 'kellonaika'
    ])

    if keep_strings:
        # keep raw strings, filter out NaN/empty
        data_row = np.array([None if pd.isna(x) else str(x) for x in data_row_raw])
        data_row = np.array([x for x in data_row if x is not None and x.strip() != '' and x.lower() != 'nan'])
    else:
        # muunna numeroksi, muut → NaN
        def to_float(x):
            s = str(x).replace(",", ".")
            try:
                return float(s)
            except:
                return np.nan

        data_row = np.array([to_float(x) for x in data_row_raw])
        # poista NaN-arvot
        data_row = data_row[~np.isnan(data_row)]

    # talteen
    data_arrays[row_name] = data_row




# Helper to format arrays with comma as decimal separator
def array_to_comma_string(arr):
    def format_elem(x):
        # If numpy scalar, get python scalar
        try:
            if isinstance(x, (np.floating,)):
                xf = float(x)
                if xf.is_integer():
                    return str(int(xf))
                return str(xf)
            if isinstance(x, (np.integer,)):
                return str(int(x))
            if isinstance(x, float):
                if x.is_integer():
                    return str(int(x))
                return str(x)
            if isinstance(x, int):
                return str(x)
        except Exception:
            pass
        return str(x)

    try:
        a = np.asarray(arr)
        # flatten to 1D list and format each element
        elems = [format_elem(v) for v in a.tolist()]
        return '[' + ', '.join(elems) + ']'
    except Exception:
        # fallback: format string representation
        s = str(arr)
        return s


# Helper: etsi ja tulosta kaikki avaimet, jotka sisältävät annetun merkkijonon
def print_matching_rows(substring, case_sensitive=False):
    s = substring if case_sensitive else substring.lower()
    matches = [k for k in data_arrays.keys() if (k if case_sensitive else k.lower()).find(s) != -1]
    if not matches:
        print(f"No keys contain '{substring}'")
        return
    for k in matches:
        print(f"{k}: {array_to_comma_string(data_arrays[k])}")




# Tulostetaan esim. kaikki avaimet, eli rivin nimet
#print("\nRivien nimet:")
#for key in data_arrays.keys():
    #print(key)



# Map selected keys from `data_arrays` to variables used in the script
# Each mapping entry contains candidate substrings to look for in the keys (case-insensitive).
mapping = {
    'all_sleep': ['kokonaisuni', 'uni', '\buni\b'],
    'REM': ['rem', 'rem-uni', 'rem uni'],
    'deepSleep': ['syvä', 'deep', 'deep sleep', 'deepsleep'],
    'lightSleep': ['kevyt', 'light', 'light sleep', 'lightsleep'],
    'sleepStartTimes': ['nukahtamisaika', 'start', 'nukahta'],
    'wakeUpTimes': ['heräämisaika', 'heraa', 'wake'],
    'sleepRegularity': ['unirytmi', 'regularity', 'sleep regularity'],
    'sleepEfficiency': ['unen tehokkuus', 'efficiency', 'sleep efficiency'],
    'sleepDisturbances': ['unihäiri', 'heräily', 'disturb'],
    'sleepScores': ['unipiste', 'sleep score', 'sleepscore']
}

def _find_key_for_patterns(patterns):
    # patterns are simple substrings; try to find first key that contains any pattern
    for k in data_arrays.keys():
        kl = k.lower()
        for p in patterns:
            if p in kl:
                return k
    return None

# Assign variables and also create comma-separated string versions
for var_name, patterns in mapping.items():
    key = _find_key_for_patterns(patterns)
    if key is not None:
        val = data_arrays[key]
        # ensure numpy array
        val = np.array(val)
        globals()[var_name] = val
        # create CSV string; convert elements to strings first
        try:
            # convert elements to strings and replace decimal point with comma
            csv_str = ','.join([str(x).replace('.', ',') for x in val.tolist()])
        except Exception:
            csv_str = ''
        globals()[f"{var_name}_csv"] = csv_str
        #print(f"Assigned variable '{var_name}' from key '{key}' ({len(val)} items)")
    #else:
        #print(f"No match found for variable '{var_name}'")

for key, data in data_arrays.items():
    # data is expected to be a NumPy array; check `.size` to see if it's empty
    try:
        if getattr(data, 'size', 0) > 0:
            print(f"{key}: {array_to_comma_string(data)}")
    except Exception:
        # fallback: truthiness for other iterable types
        if data:
            print(f"{key}: {data}")






#data

#sleep data
all_sleep = np.array([5.09, 8.86, 7.21, 8.24, 5.73, 6.23, 6.34, 6.09, 7.56, 6.66, 6.48, 8.95, 6.53, 5.88, 5.39, 7.49, 5.88, 8.79, 5.67, 5, 7.78, 8.29, 8.54, 7.48, 6.75, 5.63, 7.45, 6.03, 6.62, 7.34, 5.96])
REM = np.array([104, 99, 96, 81, 124, 82, 126, 68, 111, 76, 72, 60, 61, 79, 64, 69, 89, 101, 97, 102, 112, 125, 113, 111, 71, 82, 91, 88, 104, 65, 74])
deepSleep = np.array([106, 102, 81, 108, 66, 109, 82, 75, 51, 53, 82, 108, 46, 63, 98, 42, 70, 95, 76, 55, 94, 77, 48, 60, 90, 91, 107, 75, 88, 66, 110])
lightSleep = np.array([244, 290, 295, 240, 238, 195, 196, 275, 291, 293, 281, 278, 196, 241, 209, 247, 236, 203, 194, 283, 236, 234, 204, 298, 232, 206, 216, 181, 189, 273, 185])
sleepStartTimes  = np.array(["22:50","24:15","23:44","23:26","24:41","23:32","21:28","23:54","22:05","23:45","21:22","22:12","23:36","24:55","22:30","22:12","23:07","21:39","24:10","21:28","24:02","21:57","24:51","22:59","21:04","22:56","24:26","22:10","24:22","23:09","24:35"])
wakeUpTimes  = np.array(["08:35","05:30","08:59","07:50","08:30","06:26","07:58","08:46","07:21","07:42","08:19","05:45","09:32","08:56","05:00","07:29","05:02","09:10","08:13","09:49","07:33","05:20","09:04","09:15","05:51","06:37","09:28","08:42","08:34","06:01","07:14"])
sleepRegularity  = np.array([60,92,83,95,99,86,63,94,62,95,98,97,72,89,81,87,89,100,88,84,81,93,76,87,74,93,92,70,63,62,86])
sleepEfficiency  = np.array([80,99,78,80,74,84,87,81,70,95,78,73,99,70,87,83,95,98,85,72,87,83,92,95,72,87,92,81,84,88,73])
sleepDisturbances  = np.array([5,2,1,1,5,0,4,5,3,4,4,5,3,5,1,2,1,1,5,0,2,3,4,0,1,5,2,0,1,1,0])
sleepScores  = np.array([70,80,78,100,90,73,92,63,76,66,79,76,93,89,84,74,78,89,64,83,68,66,97,97,93,80,70,79,73,61,76])

#health data
HRV = np.array([58,44,70,39,73,75,28,49,25,71,85,79,20,45,84,26,34,85,77,51,61,58,80,70,83,25,61,36,38,50,35])
restingHeartRate = np.array([56,48,51,58,69,49,61,54,68,51,65,56,65,51,64,54,57,60,51,62,75,48,70,58,59,51,75,58,48,75,68])
heartRate = np.array([92,106,111,71,118,89,91,61,111,70,74,76,96,80,116,98,57,110,61,84,120,107,84,57,117,62,84,82,95,118,66])
respirationRate = np.array([14.7,14.5,14.1,16.2,13.3,16.7,13.4,17.8,13.2,11.3,14.1,14.7,14.5,13.2,17.6,11.5,17.1,16.7,12.1,13.1,15.9,12.9,12.2,17.3,17.2,17.8,14.4,15.9,17.5,13.3,16.1])
stressIndex = np.array([21,39,70,18,48,44,19,20,41,81,36,79,75,80,20,46,62,63,66,34,40,73,56,71,84,35,32,18,68,32,64])
readiness = np.array([41,63,71,43,93,62,65,32,44,73,83,89,76,91,93,35,48,39,37,63,91,47,84,95,33,82,32,30,60,41,33])
skinTemperature = np.array([35.4,34.2,32.4,33.4,32.8,35.4,35.2,35.5,35,32.6,35,32.4,32.5,32.9,32.9,35.5,34.9,32.8,36.3,32.7,32.4,34.6,32.4,32,34.5,35.6,34.7,34.7,36.2,33.8,32.1])

#activity data
steps = np.array([2675,10369,11990,13393,14359,6155,6482,4857,3691,3295,11448,9542,13362,13332,4919,9942,3997,4200,1329,5314,9534,5843,2454,12169,9564,12561,5879,7496,3265,13363,1595])
MET = np.array([3,5.5,9.5,1.3,8.9,7.6,2.4,3.1,5.7,9.1,7.9,4.5,2.6,3.3,9.9,2.4,7.1,4.1,7.7,4.3,6.3,1.4,1.6,9.8,1,2.1,3.7,8,3.4,6.4,5.3])
distance = np.array([2.88,6.16,10.76,7.65,6.59,11.17,6.29,10.37,4.11,10.14,7.64,5.46,9.02,9.46,9.76,10.83,7.23,7.8,6.45,7.69,3.24,1.24,4.99,3.49,8.75,10.07,11.62,11.66,8.95,8,9.91])
standingHours = np.array([6,15,4,9,4,6,12,4,9,12,7,16,14,15,9,16,11,5,15,15,4,5,13,8,6,5,16,5,12,12,15])
activeMinutes = np.array([101,35,102,77,39,89,47,36,66,102,95,35,120,109,35,63,97,111,27,109,81,39,33,68,94,39,107,69,50,70,91])
caloriesBurned = np.array([3129,1925,2402,3113,2269,1818,3168,1603,1540,2362,1502,1797,2707,2313,2420,1845,2203,2825,3004,1786,2665,2267,2205,2369,1520,2234,3189,2813,1608,3176,3118])
workouts = np.array([1,0,1,2,1,2,2,0,1,2,2,0,0,0,1,2,0,1,2,2,1,0,0,2,2,1,0,2,0,2,2])

#additional data
skinTemperature2 = np.array([36.3,33.8,33.9,32.5,34.6,35.5,35.7,32.3,33.6,34.2,35,32.7,32.4,33.9,35.1,35.5,35.9,35.5,34,35.1,32.3,36.2,32.3,36,36.4,32.7,35.4,32.2,32.8,35.2,34.3])
EDA_stress = np.array([0.62,1.06,2.09,0.63,0.34,1.78,1.37,2.65,1.03,0.87,1.6,2.27,0.13,0.88,1.36,1.99,2.1,0.57,2.66,0.39,1.44,2.78,2.56,2.29,2.36,1.18,1.54,2.31,0.15,2.93,0.06])
dayHeartRateZones = np.array([74,129,96,115,38,123,164,60,156,99,132,133,92,55,157,104,58,129,92,102,70,34,104,101,22,131,176,51,165,47,77])
daytimeStress = np.array([61,73,18,20,57,15,27,84,84,16,40,77,62,63,44,24,77,74,24,85,61,64,51,61,36,43,77,29,12,49,36])



# Calculate mean and standard deviation
mean_x = np.mean(all_sleep)
mean_y = np.mean(REM)
 
#print("Mean of x:", mean_x)
#print("Mean of y:", mean_y)
 
std_x = np.std(all_sleep)
std_y = np.std(REM)
 
#print("Standard deviation of x:", std_x)
#print("Standard deviation of y:", std_y)

