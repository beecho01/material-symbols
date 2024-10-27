import os
import json

# Base data folder path
data_folder = r"C:\Github\material-symbols\custom_components\material_symbols\data"

# Define the six icon sets with their corresponding folder paths
icon_sets = {
    "m3o": os.path.join(data_folder, "m3o"),
    "m3of": os.path.join(data_folder, "m3of"),
    "m3r": os.path.join(data_folder, "m3r"),
    "m3rf": os.path.join(data_folder, "m3rf"),
    "m3s": os.path.join(data_folder, "m3s"),
    "m3sf": os.path.join(data_folder, "m3sf")
}

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

    # Sort the names alphabetically and convert to the required structure
    icons_array = [{"name": name} for name in sorted(unique_names)]

    # Define the path for the icons.json file for this icon set
    json_output = os.path.join(folder, "icons.json")

    # Write the JSON file in the correct format
    try:
        with open(json_output, "w") as json_file:
            json.dump(icons_array, json_file, indent=2)  # Pretty print for readability
        print(f"icons.json file saved to {json_output}")
    except Exception as e:
        print(f"Error writing JSON file for {icon_set_name}: {e}")