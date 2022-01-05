# Interacts with the user and question objects

def check_answer(guess, answer):
    """
    Check if the player guess is correct
    :param guess:
    :param answer:
    :return:
    """
    if guess == answer:
        return True
    else:
        return False


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0  # current question number
        self.question_list = q_list  # list of questions
        self.score = 0  # current player score

    def still_has_questions(self):
        """
        Checks if there are no more questions

        :return: True if the current question number is less than the total number of questions
        """
        if self.question_number < len(self.question_list):
            return True
        else:
            return False

    def next_question(self):
        """
        Main Quiz Method\n
        Gets player guess and calls other methods to check it

        :return:
        """
        current_question = self.question_list[self.question_number]
        guess = ""
        while guess not in ["True", "False"]:
            guess = input(f"Q{self.question_number + 1}: {current_question.text} (true or false): ").title()
        if check_answer(guess, current_question.answer):
            self.score += 1
            print("Correct! You earned a point!")
            print(f"Your current score: {self.score}\n")
        else:
            print("That was incorrect...")
            print(f"Your current score: {self.score}\n")
        self.question_number += 1
