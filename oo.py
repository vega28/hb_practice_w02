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

    def ask_and_evaluate(self):
        """ Ask the user a question and evaluate the answer.    
        e.g.
            >>> q1 = Question('Who is the cutest?','Kepler')
            >>> q1.ask_and_evaluate()
            Who is the cutest? > Kepler
            True
        """
        user_answer = input(f'{self.question} > ')
        return user_answer == self.answer



class Exam:
    """ An entire exam. """

    def __init__(self, name):
        self.name = name
        self.questions = [] # this will be a list of Question objects

    def add_question(self, question):
        """ Add a Question object to the Exam.
        e.g.
            >>> set_q = Question('What is the method for adding an element to a set?')
            >>> exam = Exam('midterm')
            >>> exam.add_question(set_q)
        """
        self.questions.append(question)

    def administer(self):
        """ Administer all examp questions and return user's final score. 
        e.g.
            >>> q1 = Question('who is the cutest?','Kepler')
            >>> q2 = Question('what is your name?','Kelsi')
            >>> q3 = Question('do you want to play BOTW?','yesss')
            >>> midterm = Exam('midterm 1')
            >>> midterm.add_question(q1)
            >>> midterm.add_question(q2)
            >>> midterm.add_question(q3)
            >>> midterm.administer()
            who is the cutest? >>> Kepler
            what is your name? >>> me
            do you want to play BOTW? >>> yesss
            0.67
        """
        score = 0
        for q in self.questions:
            if q.ask_and_evaluate():
                score += 1 # add score
        return round(score/len(self.questions),2)


# copy-paste into interactive mode to test...
# q1 = Question('who is the cutest?','Kepler')
# q2 = Question('what is your name?','Kelsi')
# q3 = Question('do you want to play BOTW?','yesss')
# midterm = Exam('midterm 1')
# midterm.add_question(q1)
# midterm.add_question(q2)
# midterm.add_question(q3)
# midterm.administer()


