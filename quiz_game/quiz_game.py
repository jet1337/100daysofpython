# Quiz Game

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
