from django.db import models

class Employee(models.Model):  
    eid = models.CharField(max_length=20)  
    ename = models.CharField(max_length=100)  
    eaddress = models.CharField(max_length=100)  
    ektpid = models.CharField(max_length=15) 

    def __str__(self):
        return "%s " %(self.ename) 
    class Meta:  
        db_table = "employee"

class Education(models.Model):
    edid = models.CharField(max_length=20)
    eid = models.ForeignKey(Employee, on_delete=models.CASCADE)
    edschoolname = models.CharField(max_length=100)
    edmajor = models.CharField(max_length=50)
    edyearentry = models.DateField()
    edyeargraduation = models.DateField()

    def __str__(self):
        return "%s " %(self.edschoolname)
    class Meta:
        db_table = "education" 

class Experience(models.Model):
    exid = models.CharField(max_length=20)
    eid = models.ForeignKey(Employee, on_delete=models.CASCADE)
    company = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    year = models.DateField()
    information = models.CharField(max_length=255)

    def __str__(self):
        return "%s " %(self.company)
    class Meta:
        db_table = "experience"

class Picture(models.Model):
    eid = models.ForeignKey(Employee, on_delete=models.CASCADE)
    pict = models.ImageField(upload_to='images/')

    def __str__(self):
        return "%s " %(self.pict)
    class Meta:
        db_table = "picture"

    eid = models.ForeignKey(Employee, on_delete=models.CASCADE, default=None, null=True)