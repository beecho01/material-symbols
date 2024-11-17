import os
import requests
import json
import shutil

# Constants for the folder paths
FOLDERS = {
    "outline": "m3o",
    "outline-rounded": "m3r",
    "outline-sharp": "m3s",
    "rounded": "m3rf",
    "sharp": "m3sf",
    "default": "m3of"
}

# Remove existing folders and create new ones
def create_folders(base_path):
    for folder in set(FOLDERS.values()):
        folder_path = os.path.join(base_path, folder)
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
            print(f"Removed existing folder and contents at: {folder_path}")
        os.makedirs(folder_path)
        print(f"Created folder: {folder_path}")

# Fetch the JSON data from the provided URL
def fetch_json(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to fetch JSON data. Status code: {response.status_code}")

# Strip the suffix from the icon name
def strip_suffix(name):
    suffixes = ["-outline", "-outline-rounded", "-outline-sharp", "-rounded", "-sharp"]
    for suffix in suffixes:
        if name.endswith(suffix):
            return name[:-len(suffix)]
    return name

# Determine the folder based on the icon name
def get_folder(name):
    if name.endswith("outline"):
        return FOLDERS["outline"]
    elif name.endswith("outline-rounded"):
        return FOLDERS["outline-rounded"]
    elif name.endswith("outline-sharp"):
        return FOLDERS["outline-sharp"]
    elif name.endswith("rounded"):
        return FOLDERS["rounded"]
    elif name.endswith("sharp"):
        return FOLDERS["sharp"]
    else:
        return FOLDERS["default"]

# Export SVG files and collect icon names by folder
def export_svgs(base_path, icons):
    icon_names_by_folder = {folder: set() for folder in set(FOLDERS.values())}
    for name, data in icons.items():
        svg_body = data["body"].replace('\"', '"')
        svg_content = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">{svg_body}</svg>'
        
        folder = get_folder(name)
        base_name = strip_suffix(name)
        file_path = os.path.join(base_path, folder, f"{base_name}.svg")
        
        with open(file_path, "w") as svg_file:
            svg_file.write(svg_content)
        print(f"Exported {base_name}.svg to {folder}")
    
        # Add the icon name to the set for JSON generation
        icon_names_by_folder[folder].add(base_name)
    
    # Generate icons.json files for each folder
    for folder, icons in icon_names_by_folder.items():
        create_icon_json(base_path, folder, icons)

# Create a JSON file listing all icons in a folder
def create_icon_json(base_path, folder, icons):
    icons_data = [{"name": icon} for icon in sorted(icons)]
    json_path = os.path.join(base_path, folder, "icons.json")
    with open(json_path, "w") as json_file:
        json.dump(icons_data, json_file, indent=4)
    print(f"Created icons.json for {folder} with {len(icons)} icons")

# Main function
def main():
    url = "https://raw.githubusercontent.com/iconify/icon-sets/refs/heads/master/json/material-symbols.json"
    
    # Use the current working directory as the base path
    base_path = os.getcwd()
    
    create_folders(base_path)
    json_data = fetch_json(url)
    icons = json_data.get("icons", {})
    export_svgs(base_path, icons)

if __name__ == "__main__":
    main()