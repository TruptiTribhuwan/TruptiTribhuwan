

from django.db import models

class Conversation(models.Model):
    user_message = models.CharField(max_length=255)
    bot_response = models.CharField(max_length=255)
