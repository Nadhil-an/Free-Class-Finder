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
        return f"{self.block} | {self.free_day} | {self.free_hour}"
    
    STATUS_CHOICE =(
        ('Available','Available'),
        ('Occupied','Occupied')
    )

    
    TYPE_CHOICE = (
        ('classroom','Classroom'),
        ('Computer Lab','Computer Lab')
    )

    block = models.CharField(max_length=10)
    free_day = models.CharField(max_length=10, choices=DAY_CHOICES)
    free_hour = models.CharField(max_length=10, choices=TIME_CHOICES)
    room_status = models.CharField(max_length=20,choices=STATUS_CHOICE,default=False)
    room_type = models.CharField(max_length=20,choices=TYPE_CHOICE)
    is_occupied = models.BooleanField(default=False)


    