from rest_framework.test import APITestCase
from .models import Exam
from questions.models import Question

class TestExam(APITestCase):
    def setUp(self):
        pass

    def test_create_test(self):

        Question.objects.create(
            description="question one",
            answers="dngs,sudg ,dahgiouehtg,fo heo,fughef",
            correct_answer="dgodbg"
        )
        Question.objects.create(
            description="question one",
            answers="dngs,sudg ,dahgiouehtg,fo heo,fughef",
            correct_answer="dgodbg"
        )
        Question.objects.create(
            description="question 2",
            answers="dngs,sudg ,dahgiouehtg,fo heo,fughef",
            correct_answer="dgodbg"
        )
        Question.objects.create(
            description="question 3",
            answers="dngs,sudg ,dahgiouehtg,fo heo,fughef",
            correct_answer="dgodbg"
        )
        exam = Exam.objects.create(
            description="first test"
        )
        questions_count = exam.questions.count()

        self.assertEqual(questions_count,3)




        

