from django.db import models


class Sample(models.Model):
   name = models.CharField(max_length = 20)
   email = models.EmailField(max_length = 254)
   phone = models.CharField(max_length = 11)
  
   def __str__(self):
      return self.name+" "+self.phone+" "+self.email
