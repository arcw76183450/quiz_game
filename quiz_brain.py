class QuizBrain:
    """
    Class for handling all the quiz operations
    """
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        """
        Fetches the next question till the end of quiz
        """
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}. {current_question.text} (true/false): ")
        self.check_answer(current_question.answer, user_answer)

    def is_next_question_present(self):
        """
        Checks if the next question is present or no
        :return: True if next question is present, otherwise False
        """
        return self.question_number < len(self.question_list)

    def check_answer(self, correct_answer, user_answer):
        """
        Checks if the user answered the question correctly
        :param correct_answer: the correct answer of the question
        :param user_answer: the answer user has entered
        """
        if correct_answer.lower() == user_answer.lower():
            self.score += 1
            print("You got it right")
        else:
            print(f"You got it wrong, the correct answer is {correct_answer}")
        print(f"Your score is {self.score}/{self.question_number}\n")
