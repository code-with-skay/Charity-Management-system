# Generated by Django 3.2 on 2021-12-22 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admins', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='donation',
            options={'verbose_name_plural': 'Donations'},
        ),
        migrations.AlterField(
            model_name='ngo',
            name='contact_email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='contact_no',
            field=models.CharField(default='000 000 000 00', max_length=20),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='name',
            field=models.CharField(default='No Name', max_length=255),
        ),
    ]
