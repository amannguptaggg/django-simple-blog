from django.test import TestCase
import datetime

from django.utils import timezone

from .models import Questions

class QuestionsModelTests(TestCase):
    def test_was_published_recently_with_future_question(slef):
        time = timezone.now() + datetime.timedelta(days=30)

        future_question = Questions(pub_date=time)
        self.assertIs(future_question.was_published_recently(),False)
        