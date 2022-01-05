# Quiz Game
"""
Supporting files: data.py, question_model.py, quiz_brain.py

Upgrade from original project: data.py will pull questions randomly from OpenTriviaDB instead of
a static list.  Currently it's set to all categories.  If you want to change this, craft your own API link here

######################################
# https://opentdb.com/api_config.php #
######################################

and paste it into the data.py file API_LINK variable.
"""

import quiz_brain
from question_model import Question
from data import question_data

QUESTION_LIST = []


def main():
    # generate list of questions
    for question in question_data:
        new_question = Question(question["text"], question["answer"])
        QUESTION_LIST.append(new_question)
    # create QuizBrain object
    brain = quiz_brain.QuizBrain(QUESTION_LIST)
    # iterate through questions
    while brain.still_has_questions():
        brain.next_question()
    print(f"Your final score: {brain.score}/{len(QUESTION_LIST)} points")


if __name__ == "__main__":
    main()
