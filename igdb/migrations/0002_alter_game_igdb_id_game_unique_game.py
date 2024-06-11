# Generated by Django 5.0.1 on 2024-06-11 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('igdb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='igdb_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AddConstraint(
            model_name='game',
            constraint=models.UniqueConstraint(fields=('user', 'igdb_id'), name='unique game'),
        ),
    ]