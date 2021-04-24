from django.contrib.auth.models import User, Follower
from django.test import TestCase

# Create your tests here.

class UserTestCase(TestCase):
    def test_simple (self):
        self.assertEqual(1 + 1, 2)

    def test_unknown_url(self):
        response = self.client.get('/incorrect')
        self.assertEqual(response.status_code,404)

    def test_list_user_with_one_user(self):
        User.objects.create(username='Alex')
        response = self.client.get('/v1/users/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json(),
        {
            "count": 1,
            "next": None,
            "previous": None,
            "results":
            [
                {
                    "url": "http://127.0.0.1:8000/v1/users/Alex/",
                    "username": "Alex",
                    "email": "",
                    "last_name": "",
                    "first_name": "",
                }
            ]
        }
    )

class FalseTestCasee(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(userna='Ken')
        self.user2 = User.objects.create(userna='None')
        self.user3 = User.objects.create(userna='Tom')
        Follower.objects.create(follower=self.user1, follows=self.user3)

    def test_data_exists(self):
        self.assertEqual(User.objects.count(), 3)
        self.assertEqual(Follower.objecs.count(), 1)

    def test_new_follow_correct(self):
        response = self.client.get('/v1/users/')
        self.assertEqual(response.status.code,200)

