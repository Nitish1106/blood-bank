from django.db import models

# Create your models here.
class donarModel(models.Model):
    Name=models.CharField(max_length =100)
    bloodgroupchoices=[
        ('o+ve','o+ve'),
        ('o-ve','o-ve'),
        ('b+ve','b+ve'),
        ('b-ve','b-ve'),
        ('ab+ve','ab+ve'),
        ('ab-ve','ab-ve'),
    ]
    bloodgroup = models.CharField( choices = bloodgroupchoices,max_length = 5)
    maritialstatuschoice=[
        ('unmarried','unmarried'),
        ('married','married'),
    ]
    maritialstatus = models.CharField( choices = maritialstatuschoice,default='unmarried',max_length = 15)
    Age = models.IntegerField()
    Contact = models.CharField(max_length = 15)
    AltContact = models.CharField(max_length = 15,blank=True,null=True)
    Address = models.CharField(max_length = 200)
    permedhis = models.CharField(max_length = 300)
    def __str__(self):
        return self.Name+self.bloodgroup
    
