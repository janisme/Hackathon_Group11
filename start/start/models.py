from django.db import models

class UserType(models.TextChoices):
    POSTER = 'poster', 'Poster'
    SOLVER = 'solver', 'Solver'

class ProblemType(models.TextChoices):
    CLIMATE_CHANGE = 'Climate Change', 'Climate Change'
    AIR_POLLUTION = 'Air Pollution', 'Air Pollution'
    WATER_POLLUTION = 'Water Pollution', 'Water Pollution'
    DEFORESTATION = 'Deforestation', 'Deforestation'
    LOSS_OF_BIODIVERSITY = 'Loss of Biodiversity', 'Loss of Biodiversity'
    WASTE_MANAGEMENT = 'Waste Management', 'Waste Management'
    OVERFISHING = 'Overfishing', 'Overfishing'
    RESOURCE_DEPLETION = 'Resource Depletion', 'Resource Depletion'

class Event(models.Model):
    typeofproblem = models.CharField(
        max_length=100,
        choices=ProblemType.choices,
        default=ProblemType.CLIMATE_CHANGE
    )

    location = models.CharField(max_length=50)
    time = models.TimeField()
    date = models.DateField()

class IssueLog(models.Model):
    username = models.CharField(max_length=50)
    issue_id = models.CharField(max_length=6)
    longitude = models.FloatField()
    latitude = models.FloatField()
    zipcode = models.IntegerField()

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='issue_logs'
    )

    typeofproblem = models.CharField(
        max_length=100,
        choices=ProblemType.choices,
        default=ProblemType.CLIMATE_CHANGE
    )
    
    events = models.CharField(max_length=50)
    
    usertype = models.CharField(
        max_length=10,
        choices=UserType.choices,
        default=UserType.POSTER
    )

class Likes(models.Model):
    Liking = models.BooleanField()
    issue = models.ForeignKey(
        IssueLog,
        on_delete=models.CASCADE,
        related_name='likes'
    )

class Map(models.Model):
    longitude = models.FloatField()
    latitude = models.FloatField()
    zipcode = models.IntegerField()
    city = models.CharField(max_length=20)

    related_issue = models.ForeignKey(
        IssueLog,
        on_delete=models.CASCADE,
        related_name='maps'
    )