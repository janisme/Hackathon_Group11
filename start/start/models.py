from django.db import models

class IssueLog(models.Model):
    username = models.CharField(max_length=50)
    issue_id = models.CharField(max_length=6)
    longitude = models.FloatField()
    latitude = models.FloatField()
    zipcode = models.IntegerField()

    TYPE_CHOICES = [
        ('Climate Change', 'Climate Change'),
        ('Air Pollution', 'Air Pollution'),
        ('Water Pollution', 'Water Pollution'),
        ('Deforestation', 'Deforestation'),
        ('Loss of Biodiversity', 'Loss of Biodiversity'),
        ('Waste Management', 'Waste Management'),
        ('Overfishing', 'Overfishing'),
        ('Resource Depletion', 'Resource Depletion'),
    ]

    typeofproblem = models.CharField(
        max_length=100,
        choices=TYPE_CHOICES,
        default='Climate Change'
    )