import os
import glob
import json

# Directory containing JSON files
directory = '/Users/himanshu/codes/startup/openedu/codeforce_scrapper/data/done'

# Get all JSON files in the directory
json_files = glob.glob(os.path.join(directory, '*.json'))

# List to hold all questions
questions = []

# Loop through each JSON file
for file in json_files:
    with open(file, "r") as json_file:
        data = json.load(json_file)
        # Check if the loaded data is a dictionary (i.e., a single question)
        if isinstance(data, dict):
            questions.append(data)
        else:
            print(f"Warning: File {file} does not contain a single question JSON object")

# Save the merged questions to final.json
with open("final.json", "w") as file:
    json.dump({"questions": questions}, file, indent=4)

print("Merging complete. Output saved to final.json")
