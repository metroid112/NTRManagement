from django.db import models


# Design(date=timezone.now()).save()
class Design(models.Model):
    date = models.DateTimeField('Design date')

    def __str__(self):
        return f'{self.date}'

