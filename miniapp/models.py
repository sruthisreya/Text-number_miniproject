from django.db import models

# Create your models here.

class conversion(models.Model):
    text=models.CharField(max_length=400)
    convertnum=models.IntegerField()


    def __str__(self):
        return f"{self.text} → {self.convertnum}"
    


class Numconversion(models.Model):
    textitem=models.CharField(max_length=400)
    numberres=models.IntegerField()

    def __str__(self):
        return f"{self.textitem} → {self.numberres}"