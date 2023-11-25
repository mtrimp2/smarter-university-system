import unittest
import datetime
from app.controllers.quizzes_controller import QuizzesController

class QuizzesTest(unittest.TestCase):

    def setUp(self):
        # Run tests on non-production data
        self.ctrl = QuizzesController('assignment.json')
    
    def test_expose_failure_03(self):
 
        """
        Fails to create a quiz, since the title parameter is None, expecting a string 
        File "/home/arup/Documents/Enpm611/smarter-university-system-maggie_branch/app/controllers/quizzes_controller.py", line 63
        """

        self.ctrl.clear_data()

        #Add a sample quiz to assignment.json files  
        test_quiz_id = self.ctrl.add_quiz(None,"Math quiz 1",datetime.datetime(2020, 5, 17),datetime.datetime(2020, 5, 18))
        # Try to retrieve recently incorrectly created quiz 
        self.assertIsNotNone(test_quiz_id , "The test answer should not be retrievable")
        self.ctrl.clear_data()
if __name__ == '__main__':
    unittest.main()
        

if __name__ == '__main__':
    unittest.main()
