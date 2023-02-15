from django.db import models

# Create your models here.


class Hall(models.Model):
	id = models.BigAutoField(primary_key=True)
	raw = models.IntegerField()
	seat = models.IntegerField()
	status = models.BooleanField(default=False)
	user = models.CharField(max_length=50, default='empty')
	session = models.ForeignKey('Session', on_delete=models.PROTECT, blank=True, default=1)

	def __str__(self):
		return f'Seat: {self.seat}  Raw: {self.raw}'

	class Meta:
		verbose_name = 'Зал'
		verbose_name_plural = 'Зал'
		ordering = ['id']


class Session(models.Model):
	time = models.CharField(max_length=10)
	movie = models.CharField(max_length=50)

	def __str__(self):
		return self.time

	class Meta:
		verbose_name = 'Сеанс'
		verbose_name_plural = 'Cеанси'
		ordering = ['time']


class Tickets(models.Model):
	seat_id = models.IntegerField()
	raw = models.IntegerField()
	seat = models.IntegerField()
	user = models.CharField(max_length=50, blank=True)
	time = models.CharField(max_length=10)

	class Meta:
		verbose_name = 'Квитки'
		verbose_name_plural = 'Квитки'
		ordering = ['seat_id']