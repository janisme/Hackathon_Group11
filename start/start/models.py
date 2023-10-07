from django.db import models


class ProblemType(models.TextChoices):
    CLIMATE_CHANGE = 'Climate Change', 'Climate Change'
    AIR_POLLUTION = 'Air Pollution', 'Air Pollution'
    WATER_POLLUTION = 'Water Pollution', 'Water Pollution'
    DEFORESTATION = 'Deforestation', 'Deforestation'
    LOSS_OF_BIODIVERSITY = 'Loss of Biodiversity', 'Loss of Biodiversity'
    WASTE_MANAGEMENT = 'Waste Management', 'Waste Management'
    OVERFISHING = 'Overfishing', 'Overfishing'
    RESOURCE_DEPLETION = 'Resource Depletion', 'Resource Depletion'


class IssueLog(models.Model):
    username = models.CharField(max_length=50)
    issue_id = models.CharField(max_length=6)
    longitude = models.FloatField()
    latitude = models.FloatField()
    zipcode = models.IntegerField()

    event = models.ForeignKey(
        'Event',
        on_delete=models.CASCADE,  # You can choose the appropriate behavior on deletion
        related_name='issue_logs'
    )

    typeofproblem = models.ForeignKey(
        ProblemType,
        on_delete=models.CASCADE,  # You can choose the appropriate behavior on deletion
    )

    events = models.CharField(max_length=50)


class Event(models.Model):
    typeofproblem = models.ForeignKey(
        ProblemType,
        on_delete=models.CASCADE,  # You can choose the appropriate behavior on deletion
    )

    location = models.CharField(max_length=50)
    time = models.TimeField()
    date = models.DateField()


class Likes(models.Model):
    Liking = models.BooleanField()
    issue = models.ForeignKey(
        IssueLog,
        on_delete=models.CASCADE,  # You can choose the appropriate behavior on deletion
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





