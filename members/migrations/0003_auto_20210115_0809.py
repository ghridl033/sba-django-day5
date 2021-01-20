# Generated by Django 3.1.5 on 2021-01-15 08:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_members_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='members',
            options={'verbose_name': '오픈튜토리얼스 사용자', 'verbose_name_plural': 'o2 사용자'},
        ),
        migrations.AddField(
            model_name='members',
            name='update',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='수정일시'),
            preserve_default=False,
        ),
    ]
