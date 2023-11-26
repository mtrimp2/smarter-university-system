This is the current status of the Smarter University System (SUS) backend. The communication between instructors and students as well as across students is immensely important for an academic institution. The SUS is designed to support instructors in delivering their lectures more effectively and efficiently. It also aims to provide students with the information they need to participate with as little overhead as possible.

# Code organization

The source code is divided into three main directories:

* `app`: contains all the application source code
* `test`: specifies test cases that will execute functions in `app`
* `data`: contains JSON files that store the data that is managed in the application

# Setup

The majority of the application can be executed without installing any additional dependencies. You have several choices of running the program. You can run the tests in the `test` folder or you can write your own python module that calls the functions in the application.

The application also has the beginning of an API. The endpoints are specified in `app/api.py`. The API is implemented using the Flask framework. Hence, to be able to run the API (which is not required), you should set up a virtual environment and install the application dependencies from within the root directory (Unix and Mac commands):

```bash
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

The Windows commands are very similar. Please post on the discussion board if you need support with this setup.

Once the dependencies are installed, the server can be started by running:

```bash
python app/server.py
```

If you are in VSCode, you can run the `Server Start` runtime configuration. That allows you to debug the source code. You can then use Postman or any other API tool of your choice to submit API calls.

# Test

This repository already configures the tests to successfully run in VSCode. After you open the project in VSCode, you should be able to click on the erlenmeyer flask symbol in the right-hand menu bar. That should open a list of all current test cases.

For more information about running tests in VSCode, see:

https://code.visualstudio.com/docs/python/testing

## Quizzes_Test.py Test Cases

Three unit tests have been created by team two as part of the ENPM611 term project. python 3.10 was used for each of the tests. 

### Test 1
The first unit test is meant to test the use of an integer value instead of boolean value in the add_answer method. 

The intended method call is \
`add_answer(self, question_id:str, text:str, is_correct:bool)`\
Instead, the method is called as \
`self.ctrl.add_answer(test_quiz_id, "true", 1)`

Since integer value 1 is used in place of a boolean, the test crashes, with error message

`./quizzes_test.py::QuizzesTest::test_expose_failure_01 Failed with Error: 'NoneType' object is not iterable`


### Test 2
The second unit test is meant to test the use of parameter None instead of string in the add_quiz method. 

The intended method call is \
`add_quiz(self, title:str, text:str, available_date:datetime, due_date:datetime)`\
Instead, the method is called as\
`self.ctrl.add_quiz(None,"Math quiz 1",datetime.datetime(2020, 5, 17),datetime.datetime(2020, 5, 18))`

This call fails to create a quiz, since the title parameter is None, rather than the expected string.
The test crashes, with error message

`./quizzes_test.py::QuizzesTest::test_expose_failure_02 Failed with Error: unsupported operand type(s) for +: 'NoneType' and 'str'`

### Test 3
The third unit test is meant to test the addition of a question to a quiz, using a datetime object as input rather than a string.

The intended method call is \
`add_question(self, quiz_id:str, title:str, text:str)`\
Instead, the method is called as \
`self.ctrl.add_question(quiz_id,datetime.datetime.now(),"quiz question")`

Since datetime object datetime.datetime.now() is used in place of a string, the test crashes, with error message\
`./quizzes_test.py::QuizzesTest::test_expose_failure_03 Failed with Error: Object of type datetime is not JSON serializable`

NOTE: Upon each execution of unit test 3, the json file must be manually changed to "[]." This must be done each time if the user wants to execute any other unit tests afterwards. Unit test 3 erases the json file. 