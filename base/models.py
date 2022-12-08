from django.db import models

# Create your models here.

class Room(models.Model):
    # host =
    # topic= 
    name = models.CharField(max_length =200) # specify the attribute and its value
    description = models.TextField(null = True, blank = True) # by default null is set to False. Null = true means description can be blank. Null is for database and blank is for the form
    # participants = 
    updated = models.DateTimeField(auto_now = True) #snapshot every time we save
    created = models.DateTimeField(auto_now_add = True) #snapshot the first time we add it

    def __str__(self):
        return self.name

