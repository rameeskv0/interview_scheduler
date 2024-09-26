from django.db import models

class User(models.Model):
    USER_TYPES = (
        ('CANDIDATE', 'Candidate'),
        ('INTERVIEWER', 'Interviewer'),
    )
    user_type = models.CharField(max_length=20, choices=USER_TYPES)
    name = models.CharField(max_length=100)

class Availability(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='availabilities')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        unique_together = ('user',)
