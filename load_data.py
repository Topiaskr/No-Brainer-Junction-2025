import numpy as np
import pandas as pd

EXCEL_PATH = r"C:\Users\makel\Desktop\Test.xlsx"
SHEET_NAME = "DataSet_3"

def load_excel_data(path=EXCEL_PATH, sheet=SHEET_NAME):
    df = pd.read_excel(path, sheet_name=sheet)
    data_arrays = {}

    for idx, row in df.iterrows():
        first_cell = row.iloc[0]
        if pd.isna(first_cell):
            continue
        row_name = first_cell
        data_row_raw = row.iloc[1:].to_numpy()

        # determine if it’s numeric or string
        rn = str(row_name).lower()
        keep_strings = any(k in rn for k in [
            'nukaht', 'herää', 'heraa', 'start', 'wake', 'aika', 'time', 'kellon', 'kellonaika'
        ])

        if keep_strings:
            data_row = np.array([str(x) for x in data_row_raw if pd.notna(x)])
        else:
            def to_float(x):
                try:
                    return float(str(x).replace(",", "."))
                except:
                    return np.nan
            data_row = np.array([to_float(x) for x in data_row_raw])
            data_row = data_row[~np.isnan(data_row)]

        data_arrays[row_name] = np.array(data_row)

    return data_arrays

def get_variable(data_arrays, patterns):
    patterns = [p.lower() for p in patterns]
    for key in data_arrays:
        kl = key.lower()
        for p in patterns:
            if p in kl:
                return data_arrays[key]
    return None
