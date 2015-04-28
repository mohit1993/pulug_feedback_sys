from django.db import models

class WebDevSeminar2Feedback(models.Model):
    
    colleges = (
               ("uiet","University Institute Of Engineering and Technology,UIET"),
               ("pec","Panjab Engineering College,PEC"),
               )

    branches = (
               ("cse","Computer Science and Engineering"),
               ("it","Information and Technology"),
               ("ece","Electronics and Communication Engineering"),
               ("eee","Electronics and Electrical Engineering"),
               ("mech","Mechanical Engineering"),
               ("civil","Civil Engineering"),
               ("ca","Computer Applications")
               ) 
    years = (
            ('first',"1st"),
            ('second',"2nd"),
            ('third',"3rd"),
            ('fourth',"4th"),
            ('fifth',"5th")
            )    

    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 254)
    college = models.CharField(max_length = 10,choices = colleges,default = "uiet")
    branch = models.CharField(max_length = 10,choices = branches,default = "cse")
    degree_year = models.CharField(max_length = 10,choices = years,default = "first")
    contact = models.CharField(max_length = 10)
    feedback = models.TextField()

    def __str__(self):
        return self.name + " " + self.college + " " + self.branch + " " + self.degree_year + " yr"
    
    
    
