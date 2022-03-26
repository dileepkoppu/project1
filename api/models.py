from django.db import models
from django.utils import timezone
from django.utils.html import mark_safe
from django.db.models.signals import post_save
from django.core.mail import send_mail

class kid(models.Model):
    kid_name = models.CharField(max_length=30)
    kid_age = models.IntegerField()
    parent_phone_number = models.CharField(max_length=10)
    parent_email_address = models.EmailField()
    def __str__(self) -> str:
        return self.kid_name



class image(models.Model):
    food_groups=[
        ('Veg','Veg'),
        ('Fruit','Fruit'),
        ('Grain','Grain'),
        ('Protein','Protein'),
        ('Dairy','Dairy'),
        ('Confectionery','Confectionery'),
        ('Unknown','Unknown')
    ]
    kid= models.ForeignKey(kid,on_delete=models.CASCADE)
    Image = models.URLField()
    is_Approved = models.BooleanField(default=False)
    approved_by = models.CharField(max_length=40)
    food_group = models.CharField(choices=food_groups,max_length=20)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now_add=True)
    @property
    def thumbnail_preview(self):
        return mark_safe('<img src="{}" width="300" height="300" />'.format(self.Image))


def post_user_created_signal(sender, instance, created, **kwargs):
    print(sender,instance.food_group,created)
    if instance.food_group=='Unknown':
        send_mail(
            's',
            'm',
            'anjanidileep@gmail.com',
            [instance.kid.parent_email_address]
        )

post_save.connect(post_user_created_signal, sender=image)