# Generated by Django 4.0.5 on 2022-07-13 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='campeon',
            options={'verbose_name_plural': 'Campeones'},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name_plural': 'Items'},
        ),
        migrations.AlterModelOptions(
            name='posteo',
            options={'verbose_name_plural': 'Posteos'},
        ),
        migrations.RemoveField(
            model_name='campeon',
            name='imagen',
        ),
        migrations.AddField(
            model_name='campeon',
            name='imagen_url',
            field=models.CharField(default='https://ddragon.leagueoflegends.com/cdn/img/champion/splash/Ashe_0.jpg', max_length=255),
            preserve_default=False,
        ),
    ]
