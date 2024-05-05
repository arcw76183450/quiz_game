from question_model import QuestionModel
from quiz_brain import QuizBrain
import requests
import base64


def retrieve_data_from_api():
    """
    gets the questions and answers from the trivia API
    :return: the list of questions and answers, exits the code otherwise
    """
    no_of_questions = int(input("How many true/false questions do you want?"))
    response = requests.get(f"https://opentdb.com/api.php?amount={no_of_questions}&encode=base64&type=boolean")
    if response.status_code == 200:
        json_reply = response.json()
        return json_reply["results"]
    else:
        print("There is a problem with fetching the questions, Try again later")
        exit(0)


def get_all_questions():
    """
    Uses the question set from API and stores in list of QuestionModel object
    :return: List of QuestionModel objects
    """
    questions = []
    question_data = retrieve_data_from_api()
    for quiz_question in question_data:
        question = base64.b64decode(quiz_question["question"]).decode("utf-8")
        answer = base64.b64decode(quiz_question["correct_answer"]).decode("utf-8")
        questions.append(QuestionModel(question, answer))
    return questions


if __name__ == "__main__":
    """
    Driver code for the app
    User can run the following command to run the program
        python main.py
    """
    question_bank = get_all_questions()
    quiz_brain = QuizBrain(question_bank)
    while quiz_brain.is_next_question_present():
        quiz_brain.next_question()

    print("You have completed the quiz")
    print(f"Your final score is {quiz_brain.score}/{len(question_bank)}")
