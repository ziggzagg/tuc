# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(default=b'Anonymous', max_length=20)),
                ('publish_date', models.DateTimeField(auto_now_add=True)),
                ('address', models.FileField(upload_to=b'upload/')),
            ],
            options={
                'ordering': ['-publish_date'],
            },
        ),
    ]
