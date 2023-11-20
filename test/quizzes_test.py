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
        

if __name__ == '__main__':
    unittest.main()