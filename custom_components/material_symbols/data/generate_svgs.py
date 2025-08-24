import os
import requests
import json
import shutil
import re
from datetime import datetime

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
    folder_counts = {folder: 0 for folder in set(FOLDERS.values())}
    
    # Generate SVG files and count by folder
    for name, data in icons.items():
        svg_body = data["body"].replace('\"', '"')
        svg_content = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24">{svg_body}</svg>'
        
        folder = get_folder(name)
        base_name = strip_suffix(name)
        file_path = os.path.join(base_path, folder, f"{base_name}.svg")
        
        with open(file_path, "w") as svg_file:
            svg_file.write(svg_content)
        
        # Count by folder
        folder_counts[folder] += 1
        
        # Add the icon name to the set for JSON generation
        icon_names_by_folder[folder].add(base_name)
    
    # Process each folder in order and show results
    total_icon_count = 0
    for folder in sorted(FOLDERS.values()):
        if folder in icon_names_by_folder and folder_counts[folder] > 0:
            print("---")
            print(f"{folder}: generated {folder_counts[folder]} icons")
            
            # Create icons.json file for this folder
            create_icon_json(base_path, folder, icon_names_by_folder[folder])
            print(f"{folder}: created icons.json")
            
            total_icon_count += folder_counts[folder]
    
    print("---")
    print()
    print(f"ℹ️ Total generated icon count: {total_icon_count}")
    
    return total_icon_count

# Create a JSON file listing all icons in a folder
def create_icon_json(base_path, folder, icons):
    icons_data = [{"name": icon} for icon in sorted(icons)]
    json_path = os.path.join(base_path, folder, "icons.json")
    with open(json_path, "w") as json_file:
        json.dump(icons_data, json_file, indent=4)

def update_js_version():
    """Update the version in material_symbols.js with current date"""
    js_file_path = os.path.join("..", "material_symbols.js")
    
    if not os.path.exists(js_file_path):
        print(f"❌ JavaScript file not found: {js_file_path}")
        return False
    
    # Generate version string (YYYY.MM.DD format)
    version = datetime.now().strftime("%Y.%m.%d")
    
    try:
        with open(js_file_path, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Update the version in the console.info statement
        # Pattern matches: %c 2025.08.23  "
        version_pattern = r'(%c )\d{4}\.\d{2}\.\d{2}(  ")'
        
        if re.search(version_pattern, content):
            updated_content = re.sub(
                version_pattern,
                rf'\g<1>{version}\g<2>',
                content
            )
            
            # Write back to file
            with open(js_file_path, "w", encoding="utf-8") as file:
                file.write(updated_content)
            
            print(f"✅ Updated material_symbols.js version to: {version}")
            return True
        else:
            print("⚠️ Version pattern not found in JavaScript file")
            return False
            
    except Exception as e:
        print(f"❌ Error updating JavaScript version: {e}")
        return False

def update_manifest_version():
    """Update the version in manifest.json with current date"""
    manifest_file_path = os.path.join("..", "manifest.json")
    
    if not os.path.exists(manifest_file_path):
        print(f"❌ Manifest file not found: {manifest_file_path}")
        return False
    
    # Generate version string (YYYY.MM.DD format)
    version = datetime.now().strftime("%Y.%m.%d")
    
    try:
        with open(manifest_file_path, "r", encoding="utf-8") as file:
            manifest_data = json.load(file)
        
        # Update the version field
        old_version = manifest_data.get("version", "unknown")
        manifest_data["version"] = version
        
        # Write back to file with proper formatting
        with open(manifest_file_path, "w", encoding="utf-8") as file:
            json.dump(manifest_data, file, indent=4)
        
        print(f"✅ Updated manifest.json version: {old_version} → {version}")
        return True
        
    except Exception as e:
        print(f"❌ Error updating manifest version: {e}")
        return False

def update_readme_icon_count(total_icons):
    """Update the README.md with current icon count"""
    readme_path = os.path.join("..", "..", "..", "README.md")
    
    if not os.path.exists(readme_path):
        print(f"❌ README.md not found at {readme_path}")
        return False
    
    try:
        with open(readme_path, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Replace the icon count in the first paragraph
        pattern = r"collection of [\d,]+ Google Material Symbols"
        replacement = f"collection of {total_icons:,} Google Material Symbols"
        updated_content = re.sub(pattern, replacement, content)
        
        if updated_content != content:
            with open(readme_path, "w", encoding="utf-8") as file:
                file.write(updated_content)
            print(f"✅ Updated README.md with icon count: {total_icons:,}")
            return True
        else:
            print("ℹ️ README.md icon count already up to date")
            return True
            
    except Exception as e:
        print(f"❌ Error updating README.md: {e}")
        return False

# Main function
def main():
    url = "https://raw.githubusercontent.com/iconify/icon-sets/refs/heads/master/json/material-symbols.json"
    
    # Use the current working directory as the base path
    base_path = os.getcwd()
    
    create_folders(base_path)
    json_data = fetch_json(url)
    icons = json_data.get("icons", {})
    total_icons = export_svgs(base_path, icons)
    
    # Update the README with the icon count
    update_readme_icon_count(total_icons)
    
    # Update the version in the JavaScript file
    update_js_version()
    
    # Update the version in the manifest file
    update_manifest_version()

if __name__ == "__main__":
    main()