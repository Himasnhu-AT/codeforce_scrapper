import os
import json
import codeforces_wrapper

with open("codeforces_problems.json", 'r') as f:
    problems_json = json.load(f)

all_problems_details = []
count = 0

for problem in problems_json:
    if os.path.exists(f'data/{problem["contestId"]}_{problem["index"]}.json'):
        print(f'Skipping problem {problem["contestId"]}_{problem["index"]} as it already exists.')
        continue
    count += 1

    problem_link = f'https://codeforces.com/problemset/problem/{problem["contestId"]}/{problem["index"]}'
    print(f'Fetching details for problem {count}: {problem_link}')

    problem_details = codeforces_wrapper.parse_problem(problem_link)

    problem_details.update({
        "contestId": problem['contestId'],
        "index": problem['index'],
        "name": problem['name'],
        "type": problem['type'],
        "tags": problem['tags'],
        "solvedCount": problem['solvedCount']
    })

    with open(f'data/{problem["contestId"]}_{problem["index"]}.json', 'w') as f:
        json.dump(problem_details, f, indent=4)

    all_problems_details.append(problem_details)

with open('all_problems.json', 'w') as f:
    json.dump(all_problems_details, f, indent=4)

print(f'Successfully fetched and saved {len(all_problems_details)} problems.')