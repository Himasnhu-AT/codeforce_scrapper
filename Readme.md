# CodeForces Scrapper

This is a python script to scrape data from codeforces.com. It uses the codeforces API to get the problem set (basically their `ContestId | id` and `index` along with few other details). After parsing this info, we scrape html from api: `https://codeforces.com/problemset/problem/{contestId}/{index}` to get the problem statement and the input/output format.
