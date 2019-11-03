from django.db import models

# Create your models here.

class Blog(models.Model):
    titile=models.CharField(max_length=200)
    pub_date=models.DateTimeField(auto_now_add= True)
    image=models.ImageField(upload_to="images/")
    body=models.TextField()

    def summary(self):
        return self.body[:100]

    def __str__(self):
        return self.titile


    # def pub_date_pretty(self):
    #     return self.pub_date.strftime('%B %d %Y')

class Data(models.Model):
    name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
