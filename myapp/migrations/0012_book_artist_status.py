# Generated by Django 4.0.3 on 2022-04-02 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_book_artist_booking_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_artist',
            name='status',
            field=models.CharField(default='pending', max_length=100),
        ),
    ]
