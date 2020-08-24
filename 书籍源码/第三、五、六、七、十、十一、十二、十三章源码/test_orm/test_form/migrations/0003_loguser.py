# Generated by Django 2.1.4 on 2019-08-29 04:38

from django.db import migrations, models
import utils.rename_upload


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('test_form', '0002_delete_loguser'),
    ]

    operations = [
        migrations.CreateModel(
            name='loguser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=32, verbose_name='登录账号')),
                ('password', models.CharField(max_length=20, verbose_name='密码')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('gander', models.CharField(max_length=1)),
                ('hobby', models.CharField(max_length=20)),
                ('hair', models.CharField(max_length=1)),
                ('img', models.ImageField(blank=True, null=True, storage=utils.rename_upload.RenameUpload(), upload_to='image')),
            ],
        ),
    ]
