from django.db import models

# Create your models here.
class NoticeBoard(models.Model):

    text = models.CharField(blank=False, max_length=5000)
    title = models.CharField(null=True,blank=False, max_length=50)
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "NoticeBoard"
        verbose_name_plural = "NoticeBoards"
    

        

