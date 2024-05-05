class QuestionModel:
    """
    Class for the question along with answer
    """
    def __init__(self,text,answer):
        """
        Basic initialisation for question model
        :param text: the question text associated to it
        :param answer: answer of the question
        """
        self.text = text
        self.answer = answer
