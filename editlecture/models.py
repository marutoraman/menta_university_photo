from django.db import models
from myapp.models import User,Major,University

class MenuMaster(models.Model): #授業マスター
    CHOICES = (
        ('Mon', 'Monday'),
        ('Tue', 'Tuesday'),
        ('Wed', 'Wednesday'),
        ('Thu', 'Thursday'),
        ('Fry', 'Fryday'),
        ('Sat','Saturday'),
        ('Sun','Sunday')
    )
    menu_name = models.CharField(max_length=50)
    created_at = models.DateTimeField("登録日時", auto_now_add=True)
    updated_at = models.DateTimeField("更新日時", auto_now=True)
    student = models.ManyToManyField(User,through='RegisterMenu')
    coma = models.ForeignKey("Coma",on_delete=models.CASCADE,null=True,blank=True,related_name='menu_start_time')
    start_coma = models.ForeignKey("Coma",on_delete=models.CASCADE,blank=True,related_name='range_start_time',default='')
    finish_coma = models.ForeignKey("Coma",on_delete=models.CASCADE,blank=True,related_name='range_finish_time',default='')
    major = models.ForeignKey(Major,on_delete=models.CASCADE,null=True,blank=True)
    weekday = models.CharField(max_length=10,choices = CHOICES)

    def __str__(self):
        return self.menu_name

class RegisterMenu(models.Model): #履修
    menu = models.ForeignKey("MenuMaster",on_delete=models.CASCADE,null=True,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return str(self.menu)
    
    
class Coma(models.Model):
    CHOICES = (
        ('1','1コマ'),
        ('2','2コマ'),
        ('3','3コマ'),
        ('4','4コマ'),
        ('5','5コマ'),
        ('6','6コマ')
    )
    r_university = models.ForeignKey(University,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=10,choices = CHOICES,null=True,blank=True)
    start_time = models.TimeField()
    finish_time = models.TimeField()

    def __str__(self):
        return self.name

