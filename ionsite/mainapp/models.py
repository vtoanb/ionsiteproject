from django.db import models

# Create your models here.

class carousel(models.Model):
    carousel_pic = models.ImageField(upload_to = '/home/vtoanb/ionsiteproject/ionsite/static/mainapp/image', default = 'mainapp/image/no_img.jpg')
    carousel_header = models.CharField(max_length=100,default='')
    carousel_text = models.CharField(max_length=500,default='')

class event(models.Model):
    """
     This class show event picture , event-name and event-text description may be count-down timer in the future
     fail link :
     /home/vtoanb/ionsiteproject/ionsite/static/mainapp/image/
    """
    event_pic = models.ImageField(upload_to = '/home/vtoanb/ionsiteproject/ionsite/static/mainapp/image', default = 'mainapp/image/no_img.jpg')
    event_name = models.CharField(max_length = 100,default='')
    event_text = models.CharField(max_length = 500,default='')

class Film_link(models.Model):
    """
    This model use to store video link and caption
    """
    videolink = models.CharField(max_length=200,default='')

class Website_caption(models.Model):
    """
    Caption for Website text
    """
    Event_part_caption = models.CharField(max_length = 2000,default='')
    Film_part_caption = models.CharField(max_length = 2000,default='')
    Marketing_part_caption = models.CharField(max_length = 2000,default='')

class Contact_info(models.Model):
    """
    Contain contact infomation, Phone, Email, Company Address
    """
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=50,default='')
    facebook = models.CharField(max_length=50,default='')
    youtube = models.CharField(max_length=100,default='')
    position_lat = models.CharField(max_length=100,default='')
    position_lon = models.CharField(max_length=100,default='')

class FAQ(models.Model):
    """
    question & answer
    """
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=2000)

class Visiter_message(models.Model):
    """
    Visiter Message Storage, that's a good idea
    """
    name  = models.CharField(max_length=20)
    email = models.CharField(max_length=200,default='')
    note  = models.CharField(max_length=2000)
