import os
import json

# Base data folder path
data_folder = r"C:\Users\James Beeching\OneDrive\Home Assistant\material-symbols-2\custom_components\material_symbols\data"

# Define the six icon sets with their corresponding folder paths
icon_sets = {
    "outlined": os.path.join(data_folder, "outlined"),
    "outlined_filled": os.path.join(data_folder, "outlined_filled"),
    "rounded": os.path.join(data_folder, "rounded"),
    "rounded_filled": os.path.join(data_folder, "rounded_filled"),
    "sharp": os.path.join(data_folder, "sharp"),
    "sharp_filled": os.path.join(data_folder, "sharp_filled")
}

# Dictionary to hold icon names per icon set
icons_by_set = {}

# Loop through each icon set and its folder
for icon_set_name, folder in icon_sets.items():
    # Check if the folder exists
    if not os.path.exists(folder):
        print(f"Folder does not exist: {folder}")
        continue

    # Set to store unique icon names for this icon set
    unique_names = set()

    # Get the filenames in the folder
    try:
        for filename in os.listdir(folder):
            if filename.endswith(".svg"):
                # Extract the name without the extension
                name = os.path.splitext(filename)[0]
                # Add it to the set to ensure uniqueness
                unique_names.add(name)
    except Exception as e:
        print(f"Error accessing folder {folder}: {e}")
        continue

    # Sort the names alphabetically
    sorted_names = sorted(unique_names)

    # Create a dictionary where both keys and values are the same
    name_dict = {name: name for name in sorted_names}

    # Add this dictionary to the main dictionary under the icon set name
    icons_by_set[icon_set_name] = name_dict

# Define the path where you want the minified JSON file to be saved
json_output = os.path.join(data_folder, "names.min.json")

# Write the minified JSON file to the specified location
try:
    with open(json_output, "w") as json_file:
        json.dump(icons_by_set, json_file, separators=(',', ':'))  # Minify the JSON
    print(f"Minified icon names by set saved to {json_output}")
except Exception as e:
    print(f"Error writing JSON file: {e}")