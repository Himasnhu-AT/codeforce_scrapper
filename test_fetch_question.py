import json
import codeforces_wrapper

# problems = problems_json

# Base URL for problem links
base_url = 'https://codeforces.com/problemset/problem/27/E'

# List to store all problems details
all_problems_details = []

# Iterate over each problem and fetch its details
# for problem in problems:
    # contest_id = problem['contestId']
    # index = problem['index']
problem_url = f"{base_url}"
problem_details = codeforces_wrapper.parse_problem(problem_url)
   
    # Add additional problem metadata
problem_details.update({
    # "contestId": contest_id,
    "contestId": 27,
    # "index": index,
    "index": "E",
    # "name": problem['name'],
    # "type": problem['type'],
    # "points": problem['points'],
    # "tags": problem['tags'],
    # "solvedCount": problem['solvedCount']
    "name": "Number With The Given Amount Of Divisors",
    "type": "PROGRAMMING",
    "points": 2500.0,
    "rating": 2000,
    "solvedCount": 4021
})
    
all_problems_details.append(problem_details)

# Save all problems details to a JSON file
with open('detailed_codeforces_problems.json', 'w') as f:
    json.dump(all_problems_details, f, indent=4)

print(f'Successfully fetched and saved {len(all_problems_details)} problems.')
