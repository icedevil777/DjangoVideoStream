from django.db import models


class Contact(models.Model):
    H_high = models.IntegerField(default=225)
    S_high = models.IntegerField(default=225)
    V_high = models.IntegerField(default=225)
    H_low = models.IntegerField(default=0)
    S_low = models.IntegerField(default=0)
    V_low = models.IntegerField(default=0)

    def __str__(self):
        return self.S_high
