from django.db import models

class FreeClass(models.Model):
    
    

    DAY_CHOICES = (
        ('Monday','Monday'),
        ('Tuesday','Tuesday'),
        ('Wednesday','Wednesday'),
        ('Thursday','Thursday'),
        ('Friday','Friday'),
    )
    

    TIME_CHOICES = (
        ('9-10am','9-10am'),
        ('10-11am','10-11am'),
        ('11-12am','11-12am'),
        ('12-1pm','12-1pm'),
        ('1-2pm','1-2pm'),
        ('2-3pm','2-3pm'),
        ('3-4pm','3-4pm'),
        ('4-5pm','4-5pm'),
    )
    

    def __str__(self):
        return f"{self.Block} | {self.Day} | {self.Time}"
    
    STATUS_CHOICE =(
        ('Available','Available'),
        ('Occupied','Occupied')
    )

    FLOOR_CHOICE=(
        ('Ground Floor','Ground Floor'),
        ('1 Floor','1 Floor'),
        ('2 Floor','2 Floor'),
        ('3 Floor','3 Floor'),
        ('4 Floor','4 Floor'),
        ('5 Floor','5 Floor'),
        ('6 Floor','6 Floor'),
        ('7 Floor','7 Floor'),
        ('8 Floor','8 Floor'),
        ('9 Floor','9 Floor'),
        ('10 Floor','10 Floor'),
    )

    
    TYPE_CHOICE = (
        ('classroom','Classroom'),
        ('Computer Lab','Computer Lab')
    )

    Block = models.CharField(max_length=10)
    Day = models.CharField(max_length=20,choices=DAY_CHOICES)
    Time= models.CharField(max_length=10,choices=TIME_CHOICES)
    Floor = models.CharField(max_length=20)
    Room_No = models.CharField(max_length=10)
    Room_Status = models.CharField(max_length=20,choices=FLOOR_CHOICE)
    Room_Type = models.CharField(max_length=20,choices=TYPE_CHOICE)
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return f"Hour: {self.Time} - {self.Room_Type} |  {self.Room_No} | {self.Floor} | {self.is_occupied}"


    