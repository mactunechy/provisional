from django.test import TestCase
from users.models import CustomUser
from .models import Token


class TestToken(TestCase):
    def setUp(self):
        pass

    def test_create_token(self):
        user = CustomUser(username='dellan',email='dellan@test.com')
        user.set_password("test123")
        user.save()

        token = Token.objects.create(user=user)
        print(token)
        self.assertEqual(bool(token),True)

    def test_verify_token(self):
        user = CustomUser(username='dellan',email='dellan@test.com')
        user.set_password("test123")
        user.save()

        token = Token.objects.create(user=user)
        print(token.created_at)
        print(token.expires_at)
        isValid = token.verify()
        self.assertEqual(isValid,True)
        


