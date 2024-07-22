from dotenv import load_dotenv
import random
import google.generativeai as genai
import json
import os
import time

load_dotenv()

genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

def generate_response(prompt: str, retries: int = 3, delay: int = 2) -> str:
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    for attempt in range(retries):
        try:
            response = model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < retries - 1:
                print(f"Retrying in {delay} seconds...")
                time.sleep(delay)
            else:
                raise  # Re-raise the last exception if all retries fail


def get_random_question(questions: [dict]) -> dict:
    random_index = random.randint(0, len(questions) - 1)
    return questions[random_index]

def ai_prompt(context: str) -> str:
    prompt = f"""You are an AI assistant tasked with rephrasing questions, their samples. 
    {context}

    output:
    {{
        "title: <title>,
        "timelimit": {{
            "value": <value>,
            "unit"" <unit>,
        }},
        "memorylimit": {{
            "value": <value>,
            "unit"" <unit>,
        }},
        "statement": <question>,
        "input_specs": <input_specs>,
        "output_specs": <output_specs>,
        "samples"" [<sample input and outputs>],
        "test_cases": <more test cases>
    }}

    RULES:
    1. JSON should be valid and correct.
    2. Ensure that you don't change too much of the question such that it becomes fundamentally wrong.
    3. Make sure the question is correct along with the options.
    """
    return prompt

def get_question_from_ai(question: dict) -> dict:
    prompt: str = ai_prompt(question)
    response: str = generate_response(prompt)
    data = response.strip("```json").strip("```")
    
    return data


def main():
    ques_no = int(input("How many questions to generate: "))
    filename = input("Enter filename to save the questions: ")

    questions_json = []
    with open("final.json", "r") as file:
        data = json.load(file)
        questions_json = data["questions"]

    all_questions = []
    for index in range(ques_no):
        question: dict = get_random_question(questions_json)
        new_question = get_question_from_ai(question)
        print(f"""
        Question {index}:

        {new_question}\n\n\n\n""")
        all_questions.append(f"{new_question}\n\n")
    
    with open(filename, "w") as file:
        file.write(str(all_questions))

main()
