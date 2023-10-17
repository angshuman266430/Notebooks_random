import os
import pandas as pd

# Directory path
dir_path = "Z:\LWI2023-24\LWI_Reference_Deliverables\HEC-RAS"

# Get all files from the directory, excluding .lock files
files = [f for f in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, f)) and not f.endswith('.lock')]

# Extracting extensions and filenames
extensions = [os.path.splitext(f)[1] for f in files]
full_filenames = files

# Create DataFrame
df = pd.DataFrame({
    'Sl_No': list(range(1, len(files) + 1)),
    'Types': extensions,
    'Filenames': full_filenames
})

# Write DataFrame to Excel
output_path = os.path.join(dir_path, "file_list.xlsx")
df.to_excel(output_path, index=False)
