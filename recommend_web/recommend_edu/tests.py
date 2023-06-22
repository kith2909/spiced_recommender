import requests

from django.test import TestCase
from django.utils import timezone
from django.test import Client
from django.test.utils import setup_test_environment
from .models import Profile
from django.urls import reverse




class ProfileModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.

        coc = self.request.COOKIES.get('chat_to_grow')
        future_pro, created = Profile(user_id=coc)
        self.assertIs(future_pro.user_id, 'chat_to_grow')
 """




