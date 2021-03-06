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
        """ Administer all exam questions and return user's final score. """
        score = 0
        for q in self.questions:
            if q.ask_and_evaluate():
                score += 1 # add score
        return round(score/len(self.questions)*100,0)



class Quiz(Exam):
    """ A quiz is a subclass of exam which is scored as pass/fail. """

    def administer(self):
        """ Administer all quiz questions and 
            return 1 if user passed, 0 if not. """
        # score = 0
        # for q in self.questions:
        #     if q.ask_and_evaluate():
        #         score += 1 # add score
        # return 1 if score/len(self.questions) >= 0.5 else 0

        # refactored version:
        score = super(Quiz, self).administer()
        return 1 if score >= 50 else 0



class StudentExam:
    """ Create an exam for a Student. """
    
    def __init__(self, student, assessment):
        self.student = student
        self.assessment = assessment
        self.score = 0


    def take_test(self):
        self.score = self.assessment.administer()
        print(f'Your score on {self.assessment.name} is {self.score}%')



class StudentQuiz(StudentExam):
    """ Create a quiz for a student (this is a subclass of StudentExam) """

    def take_quiz(self):
        self.score = self.assessment.administer()
        if self.score == 1:
            print(f'You passed {self.assessment.name}!')
        else:
            print(f'You failed {self.assessment.name}. Please study harder next time.')

    

def exam_example():
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



def quiz_example():
    """ Create an example to demonstrate the awesome subclasses you created. """

    quiz1 = Quiz("Quiz 1")
    q1 = Question('Who is the cutest?','Kepler')
    q2 = Question('What is your name?','Kelsi')
    q3 = Question('Do you want to play BOTW right now?','yesss')
    quiz1.add_question(q1)
    quiz1.add_question(q2)
    quiz1.add_question(q3)
    kelsi = Student('Kelsi','Flatland','not my address')
    kelsi_quiz = StudentQuiz(kelsi, quiz1)
    kelsi_quiz.take_quiz()