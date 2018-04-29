from django.db import models


class Test(models.Model):
    text = models.CharField(max_length=30)
    detail = models.TextField()

    def __str__(self):
        return self.test
