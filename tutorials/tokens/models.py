from django.db import models
from users.models import CustomUser
from django.db.models.signals import pre_save
from datetime import timedelta, datetime
import strgen


class Token(models.Model):
    key              = models.CharField(max_length=255)
    user             = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tokens')
    created_at       = models.DateTimeField(default=datetime.now())
    expires_at       = models.DateTimeField()

    def __str__(self):
        return self.key

    def verify(self):
        if self.created_at <= self.expires_at:
            return True
        self.delete()
        return False


def set_key_expiry(instance, sender, *args,**kwargs):
    instance.key = strgen.StringGenerator("[\d\w]{20}").render()
    print(datetime.now()+ timedelta(days=7))
    instance.expires_at = datetime.now() + timedelta(days=7)

pre_save.connect(set_key_expiry,sender=Token)




