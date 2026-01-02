import pandas as pd
import os
import re

file_path = 'midterm/data/cars-dataset.csv' 

def extract_production_year(value):
    if value is None:
        return None

    # Convert to string
    value_str = str(value).strip()

    if value_str == "":
        return None

    # Normalize dashes
    value_str = value_str.replace("–", "-")

    # Case: multiple years like "2004, 2006, 2008"
    if "," in value_str:
        try:
            years = [int(y.strip()) for y in value_str.split(",") if y.strip().isdigit()]
            return max(years) if years else None
        except:
            return None

    # Case: range "1998-2000"
    if "-" in value_str:
        parts = value_str.split("-")
        end = parts[-1].strip()
        try:
            return int(end)
        except:
            return None

    # Case: single year "2010"
    try:
        return int(value_str)
    except:
        return None
   
def clean_displacement(value):
    if value is None:
        return None

    value_str = str(value).strip()  # Convert to string

    if value_str == "":
        return None

    # Extract the first number using regex
    match = re.search(r'\d+(\.\d+)?', value_str)
    if match:
        return float(match.group())
    return None    

def clean_top_speed(value):
    if value is None:
        return None
    value_str = str(value).strip()
    if value_str == "":
        return None
    # Extract the first number
    match = re.search(r'\d+', value_str)
    if match:
        return int(match.group())
    return None

def clean_unladen_weight(value):
    if value is None:
        return None
    value_str = str(value).strip()
    # Extract the first number
    match = re.search(r'\d+', value_str)
    if match:
        return float(match.group())
    return None

df = pd.read_csv(file_path, low_memory=False)

# Apply cleaning function to the "Production years" column
df["Production years"] = df["Production years"].apply(extract_production_year) 
df["Displacement"] = df["Displacement"].apply(clean_displacement)
df["Top Speed"] = df["Top Speed"].apply(clean_top_speed)
df['Unladen Weight'] = df['Unladen Weight'].apply(clean_unladen_weight)

# Filter dataset between 2000–2023
df_clean = df[(df["Production years"] >= 2010) & (df["Production years"] <= 2020)]

if len(df_clean) > 9500:
    df_clean = df_clean.sample(n=9499, random_state=42)

columns_to_keep = [
    "Model",
    "Serie",
    "Company",
    "Body style",
    "Segment",
    "Production years",
    "Cylinders",
    "Displacement",
    "Power(HP)",
    "Torque(Nm)",
    "Fuel",
    "Top Speed",
    "Acceleration 0-62 Mph (0-100 kph)",
    "Drive Type",
    "Gearbox",
    "Unladen Weight"
]   

df_clean = df_clean[columns_to_keep]

os.makedirs('midterm/data', exist_ok=True)

# Save cleaned dataset
df_clean.to_csv('midterm/data/cars-cleaned.csv', index=False)


