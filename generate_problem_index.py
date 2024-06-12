import requests
import json

def fetch_codeforces_problems():
    url = 'https://codeforces.com/api/problemset.problems'

    # Make a GET request to the API
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        
        # Check if the status is 'OK'
        if data['status'] == 'OK':
            # Extract the problems and problem statistics
            problems = data['result']['problems']
            problem_statistics = data['result']['problemStatistics']
            
            # Combine problems and their statistics
            combined_data = []
            for problem, stat in zip(problems, problem_statistics):
                combined_problem = problem.copy()
                combined_problem.update(stat)
                combined_data.append(combined_problem)
            
            # Save the combined data to a JSON file
            with open('codeforces_problems.json', 'w') as f:
                json.dump(combined_data, f, indent=4)
            
            print(f'Successfully fetched and saved {len(combined_data)} problems.')
        else:
            print('Failed to retrieve problems: Status is not OK.')
    else:
        print(f'Failed to retrieve problems: HTTP Status Code {response.status_code}')

# Call the function
fetch_codeforces_problems()

