# Generated by Django 2.0 on 2017-12-20 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apptest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appcasestep',
            name='apptestdata',
            field=models.CharField(max_length=200, null=True, verbose_name='测试数据'),
        ),
    ]
