# Generated by Django 4.0.3 on 2022-03-02 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('H_high', models.IntegerField(default=225)),
                ('S_high', models.IntegerField(default=225)),
                ('V_high', models.IntegerField(default=225)),
                ('H_low', models.IntegerField(default=0)),
                ('S_low', models.IntegerField(default=0)),
                ('V_low', models.IntegerField(default=0)),
            ],
        ),
    ]
