import unittest

from app.controllers.quizzes_controller import QuizzesController

class QuizzesTest(unittest.TestCase):

    def setUp(self):
        # Run tests on non-production data
        self.ctrl = QuizzesController('quizzes_test.py')
        
    def test_expose_failure_01(self):
        """
        Test retrieval of a quiz that does not exist 
        This unit test will fail at file controller.py, line 117 
        """
        self.ctrl.clear_data()

        # Check that we have no quizzes in the list
        quizzes = self.ctrl.get_quizzes()
        self.assertEquals(len(quizzes), 0, "There are no quizzes in the list.")

        # Try to retrieve quiz with incorrect id 
        quiz = self.ctrl.get_quiz_by_id("random quiz id") #arbitrary string

        self.assertIsNotNone(quiz, "The quiz can be retrieved.")
        # This unit test should fail at file quizzes_controller.py, line 117 (?)

    def test_expose_failure_02(self):
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
