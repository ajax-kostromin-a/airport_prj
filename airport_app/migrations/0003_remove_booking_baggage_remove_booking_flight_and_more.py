# Generated by Django 5.0 on 2024-12-16 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('airport_app', '0002_booking_flight_delete_ticket_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='baggage',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='flight',
        ),
        migrations.DeleteModel(
            name='Baggage',
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='Flight',
        ),
    ]
