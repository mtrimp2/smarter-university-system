import unittest
import datetime
from app.controllers.quizzes_controller import QuizzesController

class QuizzesTest(unittest.TestCase):

    def setUp(self):
        # Run tests on non-production data
        self.ctrl = QuizzesController('assignment_test.json')

    def test_expose_failure_01(self): # Maggie test
        """
        Fails because None object is forced to be an iterable 
        """
        #clears previous test 
        self.ctrl.clear_data()
        #create quiz 1 and question 1 
        quiz1 = self.ctrl.add_quiz("Quiz #1", "Biology", datetime.datetime(2020, 5, 17), datetime.datetime(2020, 5, 18))
        self.ctrl.add_question(quiz1, "Question 1", "what is the power house of the cell")
        
        #attempt to create quiz 2 and question 1
        quiz2 = self.ctrl.add_quiz("Quiz #2", "History ", datetime.datetime(2020, 5, 17), datetime.datetime(2020, 5, 18))
        self.ctrl.quizzes[0].sections = None
        quiz2question1 = self.ctrl.add_question(quiz2, "Question 1", "Where is the Roman empire located")
        """
        File "/home/arup/Documents/Enpm611/smarter-university-system-main/app/controllers/quizzes_controller.py", line 81, in add_question
            self._save_data()
        File "/home/arup/Documents/Enpm611/smarter-university-system-main/app/controllers/quizzes_controller.py", line 54, in _save_data
            json_data:any = [q.to_json() for q in self.quizzes]
        File "/home/arup/Documents/Enpm611/smarter-university-system-main/app/controllers/quizzes_controller.py", line 54, in <listcomp>
            json_data:any = [q.to_json() for q in self.quizzes]
        File "/home/arup/Documents/Enpm611/smarter-university-system-main/app/model/assignments.py", line 117, in to_json
            jobj['sections'] = [s.to_json() for s in self.sections]
        TypeError: 'NoneType' object is not iterable

        """
        self.assertIsNotNone(quiz2question1,"Does not expect the 2nd quiz's question to be created")
    
        

    def test_expose_failure_02(self):#Joshua and Shwe's code
        """  
        Fails to create a quiz, since the title parameter is None, expecting a string 
        """
        
        #Deletes contents in assignment.json
        self.ctrl.clear_data()

        #Add a sample quiz to assignment.json files  
        test_quiz_id = self.ctrl.add_quiz(None,"Math quiz 1",datetime.datetime(2020, 5, 17),datetime.datetime(2020, 5, 18))
        
        """
        File "/home/arup/Documents/Enpm611/smarter-university-system-maggie_branch/app/controllers/quizzes_controller.py", line 63
        """
        # Try to retrieve recently incorrectly created quiz 
        self.assertIsNotNone(test_quiz_id , "The test answer should not be retrievable")
        
        #Deletes contents in assignment.json
        self.ctrl.clear_data()
    

    def test_expose_failure_03(self):#Harsh's unit test
        self.ctrl.clear_data()

        # add quiz 
        quiz_id = self.ctrl.add_quiz("New quiz","New quiz",datetime.datetime.now(),datetime.datetime.now()+ datetime.timedelta(minutes=75))
        # quiz added successfully
        
        # add question
        question_id = self.ctrl.add_question(quiz_id,datetime.datetime.now(),"quiz question")
        # Here it will cause an error as datetime object has been passed to function which requires a string. This will cause the function to crash

        # Failing at 
        """
        File "d:\Fall 23\Software Engineering\smarter-university-system\app\controllers\quizzes_controller.py", line 81, in add_question
        self._save_data()
        ---
        File "d:\Fall 23\Software Engineering\smarter-university-system\app\controllers\quizzes_controller.py", line 55, in _save_data
        save_data(self.file_name,json_data)
        """
        # get question by id
        question = self.ctrl.get_question_by_id(question_id)

        self.assertIsNotNone(question,"Question")

if __name__ == '__main__':
    unittest.main()
