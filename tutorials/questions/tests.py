from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status

from .models import Question

class QuestionAPITestcase(APITestCase):
    def setUp(self):
        question = Question.objects.create(
            description="question one",
            answers="dngs,sudg ,dahgiouehtg,fo heo,fughef",
                correct_answer="dgodbg"
            )
    def test_single_post(self):
        questions_count = Question.objects.count()
        self.assertEqual(questions_count,1)
    
    def test_get_list(self):
        data ={}
        url = api_reverse("questions-list")
        resp = self.client.get(url,data,format="json")
        self.assertEqual(resp.status_code,status.HTTP_200_OK)

    def test_get_question(self):
        pass


