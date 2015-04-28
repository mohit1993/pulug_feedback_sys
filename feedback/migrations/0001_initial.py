# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebDevSeminar2Feedback',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('college', models.CharField(default=b'uiet', max_length=10, choices=[(b'uiet', b'University Institute Of Engineering and Technology,UIET'), (b'pec', b'Panjab Engineering College,PEC')])),
                ('branch', models.CharField(default=b'cse', max_length=10, choices=[(b'cse', b'Computer Science and Engineering'), (b'it', b'Information and Technology'), (b'ece', b'Electronics and Communication Engineering'), (b'eee', b'Electronics and Electrical Engineering'), (b'mech', b'Mechanical Engineering'), (b'civil', b'Civil Engineering'), (b'ca', b'Computer Applications')])),
                ('degree_year', models.CharField(default=b'first', max_length=10, choices=[(b'first', b'1st'), (b'second', b'2nd'), (b'third', b'3rd'), (b'fourth', b'4th'), (b'fifth', b'5th')])),
                ('contact', models.CharField(max_length=10)),
                ('feedback', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
