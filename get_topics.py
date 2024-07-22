import json

data = {}
with open("final.json", "r") as f:
    data = json.load(f)

questions = data["questions"]

# Set to hold unique tags
unique_tags = set()

# Collect all unique tags
for question in questions:
    unique_tags.update(question.get("tags", []))

# Convert the set back to a list for each question
unique_tags_list = list(unique_tags)

print(unique_tags_list)

