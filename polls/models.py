import datetime
from django.db import models
from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.utils.crypto import get_random_string


def get_timestamp_path(instance, filename):
    return 'polls/file'.join([get_random_string(5) + '_' + filename])


class AdvUser(User):
    img = models.ImageField(max_length=200, upload_to=get_timestamp_path, blank=True, null=True,
                            validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
