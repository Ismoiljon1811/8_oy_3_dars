from django.db import models

class Klass(models.Model):
    name = models.CharField(max_length = 100)
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.name
    

class Hotel(models.Model):
    name = models.CharField(max_length = 100)
    number_of_stars = models.IntegerField()
    price = models.IntegerField()

    def __str__(self) -> str:
        return self.name



class Travel(models.Model):
    name = models.CharField(max_length = 100)
    description = models.CharField(max_length = 1000)
    lifetime = models.IntegerField()
    price = models.IntegerField()
    klass = models.ForeignKey(Klass, on_delete = models.CASCADE, related_name = 'klass')
    hotel = models.ForeignKey(Hotel, on_delete = models.CASCADE, related_name = 'hotel')

    def __str__(self) -> str:
        return self.name