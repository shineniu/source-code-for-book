# Generated by Django 2.1.4 on 2019-10-19 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fare', '0004_auto_20191019_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loguser',
            name='user_obj',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rbac.UserInfo'),
        ),
    ]
