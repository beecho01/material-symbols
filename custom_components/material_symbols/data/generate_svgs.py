import os
import requests
import json
import shutil

# Constants for the folder paths
FOLDERS = {
    "outlined": "outlined",
    "outline-rounded": "rounded",
    "outline-sharp": "sharp",
    "rounded": "rounded_filled",
    "sharp": "sharp_filled",
    "default": "outlined_filled"  # Remaining files go here
}

# Remove existing folders and create new ones
def create_folders(base_path):
    # Iterate through the folders defined in FOLDERS
    for folder in FOLDERS.values():
        folder_path = os.path.join(base_path, folder)
        
        # If the folder exists, remove it
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
            print(f"Removed existing folder and contents at: {folder_path}")
            
        # Recreate the folder
        os.makedirs(folder_path)
        print(f"Created folder: {folder_path}")

# Fetch the JSON data from the provided URL
def fetch_json(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch JSON data. Status code: {response.status_code}")

# Strip the suffix from the name (e.g., remove '-outline', '-rounded')
def strip_suffix(name):
    if name.endswith("outline"):
        return name.replace("-outline", "")
    elif name.endswith("outline-rounded"):
        return name.replace("-outline-rounded", "")
    elif name.endswith("outline-sharp"):
        return name.replace("-outline-sharp", "")
    elif name.endswith("-rounded"):
        return name.replace("-rounded", "")
    elif name.endswith("-sharp"):
        return name.replace("-sharp", "")
    else:
        return name

# Parse the JSON and export SVG files
def export_svgs(base_path, icons):
    for name, data in icons.items():
        # Replace escaped quotes with regular quotes in the SVG path
        svg_body = data["body"].replace('\"', '"')
        
        # Create the full SVG content with correct quotes
        svg_content = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">{svg_body}</svg>'
        
        # Determine the folder based on the filename (use full name here)
        if name.endswith("outline"):
            folder = FOLDERS["outlined"]
        elif name.endswith("outline-rounded"):
            folder = FOLDERS["outline-rounded"]
        elif name.endswith("outline-sharp"):
            folder = FOLDERS["outline-sharp"]
        elif name.endswith("rounded"):
            folder = FOLDERS["rounded"]
        elif name.endswith("sharp"):
            folder = FOLDERS["sharp"]
        else:
            folder = FOLDERS["default"]

        # Strip the suffix to get the base name
        base_name = strip_suffix(name)

        # Create the full path for the SVG file using the base name
        file_path = os.path.join(base_path, folder, f"{base_name}.svg")
        
        # Write the SVG content to the file
        with open(file_path, "w") as svg_file:
            svg_file.write(svg_content)
        print(f"Exported {base_name}.svg to {folder}")

# Main function
def main():
    url = "https://raw.githubusercontent.com/iconify/icon-sets/refs/heads/master/json/material-symbols.json"
    base_path = r"C:\Users\jbeeching\Downloads\OneDrive-2024-10-21\data"  # Specify your output folder

    # Create (or recreate) the necessary folders
    create_folders(base_path)

    # Fetch and parse the JSON data
    json_data = fetch_json(url)
    
    # Get the icons section
    icons = json_data.get("icons", {})
    
    # Export SVGs
    export_svgs(base_path, icons)

if __name__ == "__main__":
    main()