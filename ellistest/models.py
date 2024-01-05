from django.db import models
from django.contrib.auth.base_user import BaseUserManager
class User(models.Model):
    objects = BaseUserManager()
    username = models.CharField(max_length=255,unique=True)
    age = models.IntegerField()
    userid = models.BigAutoField(primary_key=True,unique=True)
    is_active = models.BooleanField(default=True,)
    REQUIRED_FIELDS = ['userid']
    USERNAME_FIELD = 'username'
    class Meta:
        db_table='ellistest'
        
        
    @property
    def is_anonymous(self):
        """
        Always return False. This is a way of comparing User objects to
        anonymous users.
        """
        return False

    @property
    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True
# Create your models here.
