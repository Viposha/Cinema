from django.db import models

# Create your models here.


class CinemaHall(models.Model):
	id = models.BigAutoField(primary_key=True)
	raw = models.IntegerField(),
	seat = models.IntegerField(),
	status = models.BooleanField(default=False),
	user = models.CharField(default='empty')

	def __str__(self):
		if not self.status:
			return f'{self.seat} in {self.raw} is reserved'
		else:
			return f'{self.seat} in {self.raw} is free'
