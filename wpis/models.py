from django.db import models


# class DiaryModels(models.)


class diary(models.Model):
    name_user = models.CharField(max_length=200)
    data = models.DateTimeField('date_activity')
    activity = models.CharField(max_length=200)
    emotions = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.data} - {self.activity}"