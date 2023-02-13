from django.db import models

# Create your models here.


class Hall(models.Model):
	id = models.BigAutoField(primary_key=True)
	raw = models.IntegerField()
	seat = models.IntegerField()
	status = models.BooleanField(default=False)
	user = models.CharField(max_length=50, default='empty')

	def __str__(self):
		return f'Seat: {self.seat}  Raw: {self.raw}'

	class Meta:
		verbose_name = 'Зал'
		verbose_name_plural = 'Зал'
		ordering = ['id']

