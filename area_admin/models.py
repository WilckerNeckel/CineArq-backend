from django.db import models
from django.contrib.auth.models import User

class EnableForm(models.Model):
    is_enabled = models.BooleanField(default=True)
    last_modified_user_id =  models.ForeignKey(User, on_delete=models.CASCADE)
    last_modified_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.is_enabled)
    
