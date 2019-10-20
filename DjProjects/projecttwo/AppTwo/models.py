from django.db import models

# Create your models here.
class My_user(models.Model):
    u_name = models.CharField(max_length=264)
    u_lastname = models.CharField(max_length=264)
    u_email = models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.u_email

class Company(models.Model):
    comp_name = models.CharField(max_length=264, db_column='comp_name')
    comp_house_count=models.IntegerField(db_column='comp_house_count')

    def __str__(self):
        return self.comp_name

class House(models.Model):
    house_addr=models.CharField(max_length=264,db_column='House_addr')
    geo_lat = models.FloatField(db_column='geo_lat')
    geo_lon = models.FloatField(db_column='geo_lon')
    comp_id= models.ForeignKey(Company,on_delete=models.CASCADE)
    def __str__(self):
        return self.house_addr
