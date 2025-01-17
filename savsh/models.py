from django.db import models

class Expense(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=30, unique=True)
    amount = models.IntegerField()
    validity = models.CharField(max_length=11)
    value = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name + ' | ' + self.value
    
    
class Meta(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    value = models.CharField(max_length=10)
    description = models.TextField(null=True, blank=True, default="No description")
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.value + ' | ' + self.description
    