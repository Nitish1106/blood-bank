# Generated by Django 4.1.2 on 2022-10-19 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='donarmodel',
            name='maritialstatus',
            field=models.CharField(choices=[('unmarried', 'unmarried'), ('married', 'married')], default='unmarried', max_length=15),
        ),
    ]
