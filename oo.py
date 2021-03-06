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
        """ Add a Question object to the Exam. """
        self.questions.append(question)

    def administer(self):
        """ Administer all examp questions and return user's final score. """
        score = 0
        for q in self.questions:
            if q.ask_and_evaluate():
                score += 1 # add score
        return round(score/len(self.questions),2)



class StudentExam:
    """ Create an exam for a Student. """
    
    def __init__(self, student, exam):
        self.first_name = student.first_name
        self.last_name = student.last_name
        self.exam = exam
        self.score = 0


    def take_test(self):
        self.score = self.exam.administer()
        print(f'Your score on {self.exam.name} is {self.score}')

    

def example():
    """ Create an example to demonstrate the awesome classes you created. """

    midterm = Exam('Midterm 1')
    q1 = Question('Who is the cutest?','Kepler')
    q2 = Question('What is your name?','Kelsi')
    q3 = Question('Do you want to play BOTW right now?','yesss')
    midterm.add_question(q1)
    midterm.add_question(q2)
    midterm.add_question(q3)
    kelsi = Student('Kelsi','Flatland','not my address')
    kelsi_test = StudentExam(kelsi, midterm)
    kelsi_test.take_test()
    # is there a way to define user input for the questions in this example?



