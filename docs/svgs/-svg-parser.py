import os
import re

# Function to extract SVG path data from an SVG string
def extract_svg_path(svg_string):
    path_match = re.search(r'<path d="([^"]+)"', svg_string)
    if path_match:
        return path_match.group(1)
    return ""

# Function to read an SVG file and extract its content
def read_svg_file(file_path):
    with open(file_path, 'r') as file:
        svg_content = file.read()
    return svg_content

# Function to process SVG files in a directory and convert them to the desired format
def process_svg_files(directory):
    svg_data = {}

    for filename in os.listdir(directory):
        if filename.endswith(".svg"):
            file_path = os.path.join(directory, filename)
            svg_content = read_svg_file(file_path)
            svg_path = extract_svg_path(svg_content)

            if svg_path:
                keywords = filename[:-4].split("-")
                svg_data[filename[:-4]] = {
                    "path": svg_path,
                    "keywords": keywords
                }

    return svg_data

# Replace "directory_path" with the path of the directory containing the SVG files
directory_path = "C:/Users/James Beeching/OneDrive/Home Assistant/hass-material-symbols/outlined"
output_data = process_svg_files(directory_path)

# Print the output in the desired format
for key, value in output_data.items():
    print(f'"{key}":{value},')