# Generated by Django 4.0.6 on 2022-07-16 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_isuser_gender'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='isuser',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AlterField(
            model_name='isuser',
            name='gender',
            field=models.CharField(default='Not to say', max_length=10),
        ),
    ]
