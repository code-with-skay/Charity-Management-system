# Generated by Django 4.0.5 on 2022-06-23 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0004_project_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donation',
            name='payment_method',
            field=models.CharField(choices=[('s', 'Stripe')], default='e', max_length=1),
        ),
    ]
