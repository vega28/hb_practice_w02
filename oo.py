# --- define classes --- #

class Student:
    """ A student. """

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question:
    """ A question for an assessment. """

    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


class Exam:
    """ An entire exam. """

    def __init__(self, name):
        self.name = name
        self.questions = [] # this will be a list of Question objects