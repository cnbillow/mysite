# Generated by Django 2.1.1 on 2018-09-22 05:47

import DjangoUeditor.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20180917_1015'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, verbose_name='标题')),
                ('category', models.CharField(blank=True, max_length=100, verbose_name='类目')),
                ('mainPhoto', models.ImageField(upload_to='products')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='date updated')),
                ('content', DjangoUeditor.models.UEditorField(blank=True, verbose_name='内容 ')),
            ],
        ),
    ]
