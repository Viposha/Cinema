# Generated by Django 4.1.6 on 2023-02-15 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_hall_session'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seat_id', models.IntegerField()),
                ('raw', models.IntegerField()),
                ('seat', models.IntegerField()),
                ('user', models.CharField(blank=True, max_length=50)),
                ('time', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name': 'Квитки',
                'verbose_name_plural': 'Квитки',
                'ordering': ['seat_id'],
            },
        ),
    ]
