import os

def rename_file(filename):
    # Extract the extension and the base name of the file
    base_name, ext = os.path.splitext(filename)

    # Extract details from base name
    parts = base_name.split('_')

    if len(parts) < 3:
        return filename

    month_year = parts[0]
    source = parts[1]
    datatype = parts[2]

    # Construct the new filename for both .tif and .vrt extensions
    new_filename = f"Amite_{month_year}_{source}_Max{datatype}{ext}"

    return new_filename

def process_folder(folder_path):
    # Ensure the path exists and is a directory
    if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
        print(f"The path {folder_path} doesn't exist or is not a directory.")
        return

    # Rename files in the folder (.tif and .vrt)
    for old_filename in os.listdir(folder_path):
        new_filename = rename_file(old_filename)
        if new_filename != old_filename:
            old_filepath = os.path.join(folder_path, old_filename)
            new_filepath = os.path.join(folder_path, new_filename)
            os.rename(old_filepath, new_filepath)
            print(f"Renamed {old_filename} to {new_filename}")

def main():
    folders = [
        "Z:\\LWI2023-24\\LWI_Reference_Deliverables\\TCs_Reanalysis_Rasters"
    ]

    for folder in folders:
        process_folder(folder)

if __name__ == "__main__":
    main()
