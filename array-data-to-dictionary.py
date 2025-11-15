import json
import argparse
from load_data import load_excel_data


def arrays_to_dict(data_arrays):
    """Convert a dict of numpy arrays to a JSON-serializable dict.

    Args:
        data_arrays (dict): mapping row_name -> numpy array (or array-like)

    Returns:
        dict: mapping row_name -> Python list of values
    """
    out = {}
    for key, val in data_arrays.items():
        try:
            # If NumPy array or similar
            lst = val.tolist()
        except Exception:
            # Fallback: try to iterate
            try:
                lst = list(val)
            except Exception:
                # Last resort: stringify
                lst = [str(val)]
        out[str(key)] = lst
    return out


def arrays_to_list_of_dicts(data_arrays):
    """Convert data_arrays to a list of {'name': key, 'values': [...] } objects."""
    out = []
    for key, val in data_arrays.items():
        try:
            lst = val.tolist()
        except Exception:
            try:
                lst = list(val)
            except Exception:
                lst = [str(val)]
        out.append({"name": str(key), "values": lst})
    return out


def main(output_path="array_data.json", sample=5, full=False):
    # load data (load_data uses default example_data.xlsx and DataSet_3)
    data = load_excel_data()

    # convert arrays to plain lists
    converted = arrays_to_dict(data)

    # write to JSON (this contains ALL data)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(converted, f, ensure_ascii=False, indent=2)

    # Also write a list-of-dicts variant so consumers can iterate easily
    list_output = output_path.replace('.json', '') + '_list.json'
    list_data = arrays_to_list_of_dicts(data)
    with open(list_output, 'w', encoding='utf-8') as f:
        json.dump(list_data, f, ensure_ascii=False, indent=2)

    print(f"Wrote list-of-dicts to {list_output}")

    print(f"Wrote {len(converted)} entries to {output_path}")

    # Print entries: either full or a short sample per key
    keys = list(converted.keys())
    if full:
        print("\nFull data dump:")
        for k in keys:
            print(f"{k}: {converted[k]}")
    else:
        print("\nSample of entries (use --full to print everything):")
        for k in keys[:min(50, len(keys))]:
            vals = converted[k]
            if sample == 0:
                # print all values for this key
                print(f" - {k}: {vals}")
            else:
                snippet = vals[:sample]
                more = '...' if len(vals) > sample else ''
                print(f" - {k}: {snippet}{more}")


if __name__ == "__main__":
    # Load data and convert to list of dicts
    data = load_excel_data()
    list_of_dicts = arrays_to_list_of_dicts(data)
    
    # Print the list of dictionaries
    print(json.dumps(list_of_dicts, ensure_ascii=False, indent=2))
    
    # Also save to file
    with open("array_data_list.json", "w", encoding="utf-8") as f:
        json.dump(list_of_dicts, f, ensure_ascii=False, indent=2)
