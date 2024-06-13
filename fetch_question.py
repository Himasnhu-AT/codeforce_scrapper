import os
import json
import codeforces_wrapper

with open("codeforces_problems.json", 'r') as f:
    problems_json = json.load(f)

total_question = len(problems_json)
count = 0

for problem in problems_json:
    count += 1

    if os.path.exists(f'data/{problem["contestId"]}_{problem["index"]}.json'):
        print(f'Skipping problem {problem["contestId"]}_{problem["index"]} as it already exists.')
        continue

    problem_link = f'https://codeforces.com/problemset/problem/{problem["contestId"]}/{problem["index"]}'
    print(f'Fetching details for problem {count}/{total_question}: {problem_link}')

    problem_details = codeforces_wrapper.parse_problem(problem_link)

    if problem_details == None:
        with open(f'data/{problem["contestId"]}_{problem["index"]}.json', 'w') as f:
            json.dump({}, f, indent=4) 
            continue

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