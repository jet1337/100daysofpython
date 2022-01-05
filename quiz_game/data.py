# Gets random T/F questions & answers from OpenTriviaDB and puts them into a list of dictionary items

import requests
import json
from html import unescape

question_data = []
NUMBER_OF_QUESTIONS = 10  # change this number to get more questions
API_LINK = f"https://opentdb.com/api.php?amount={NUMBER_OF_QUESTIONS}&type=boolean"

# generate new questions from open trivia db
s = requests.get(API_LINK)
# get the content of the page
content = s.content.decode()
# extract a json object from the string format and turn it into a dictionary
new_dict = json.loads(content)
# access the results list from the dictionary
results = new_dict["results"]
# create a dictionary of extracted question/answers
for item in results:
    question_data.append({"text": item["question"], "answer": item["correct_answer"]})
# get rid of html-encoded characters in each question text
for question in question_data:
    question["text"] = unescape(question["text"])
# print(*question_data, sep="\n")
