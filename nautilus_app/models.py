from django.db import models

class NautilusReviewModel(models.Model):
    reviewid = models.IntegerField(db_column='ReviewID', primary_key=True)
    firstname = models.CharField(db_column='Firstname', max_length=20)
    lastname = models.CharField(db_column='Lastname', max_length=20)
    message = models.TextField(db_column='Message')
    rating = models.CharField(db_column='Rating', max_length=20)
    class Meta:
        db_table = 'reviews'

class NautilusConsultationModel(models.Model):
    ConsultationID = models.IntegerField(db_column='ConsultationID', primary_key=True)
    firstname = models.CharField(db_column='Firstname', max_length=20)
    lastname = models.CharField(db_column='Lastname', max_length=20)
    email = models.CharField(db_column='Email', max_length=50)
    phone = models.CharField(db_column='Phone', max_length=20)
    message = models.TextField(db_column='Message')
    lawType = models.CharField(db_column='LawType', max_length=20)
    class Meta:
        db_table = 'consultation'

class NautilusTeamModel(models.Model):
    TeamID = models.IntegerField(db_column='TeamID', primary_key=True)
    firstname = models.CharField(db_column='Firstname', max_length=20)
    lastname = models.CharField(db_column='Lastname', max_length=20)
    lawField = models.CharField(db_column='LawField', max_length=20)
    teamPhoto = models.CharField(db_column='TeamPhoto', max_length=255)
    class Meta:
        db_table = 'team'