import os
import json
import shutil

# Directory containing the JSON files
json_dir = 'data'

# Directory to copy non-empty JSON files
copy_dir = 'data/done'

# Iterate over all files in the directory
for filename in os.listdir(json_dir):
    if filename.endswith('.json'):
        file_path = os.path.join(json_dir, filename)
        
        # Check if the JSON file is empty
        with open(file_path, 'r') as file:
            json_data = json.load(file)
            if json_data:
                # Copy the non-empty JSON file to the destination directory
                print("copying file: ", file_path)  
                shutil.copy(file_path, copy_dir)