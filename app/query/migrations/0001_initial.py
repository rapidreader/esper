# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-29 10:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Commercial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_frame', models.IntegerField()),
                ('max_frame', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Face',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bbox_x1', models.FloatField()),
                ('bbox_x2', models.FloatField()),
                ('bbox_y1', models.FloatField()),
                ('bbox_y2', models.FloatField()),
                ('bbox_score', models.FloatField()),
                ('background', models.BooleanField(default=False)),
                ('is_host', models.BooleanField(default=False)),
                ('blurriness', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FaceFeatures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('features', models.BinaryField()),
                ('distto', models.FloatField(null=True)),
                ('face', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.Face')),
            ],
        ),
        migrations.CreateModel(
            name='FaceGender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('face', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.Face')),
            ],
        ),
        migrations.CreateModel(
            name='FaceIdentity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('face', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.Face')),
            ],
        ),
        migrations.CreateModel(
            name='Frame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(db_index=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Identity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Labeler',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frame', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.Frame')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Pose',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keypoints', models.BinaryField()),
                ('labeler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.Labeler')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.Person')),
            ],
        ),
        migrations.CreateModel(
            name='ScannerJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Segment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_frame', models.IntegerField()),
                ('max_frame', models.IntegerField()),
                ('polarity', models.FloatField(null=True)),
                ('subjectivity', models.FloatField(null=True)),
                ('labeler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.Labeler')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Shot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_frame', models.IntegerField()),
                ('max_frame', models.IntegerField()),
                ('in_commercial', models.BooleanField(default=False)),
                ('labeler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.Labeler')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_frame', models.IntegerField()),
                ('max_frame', models.IntegerField()),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.Gender')),
                ('identity', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='query.Identity')),
                ('labeler', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.Labeler')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='ThingType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(db_index=True, max_length=256)),
                ('num_frames', models.IntegerField()),
                ('fps', models.FloatField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('has_captions', models.BooleanField(default=False)),
                ('time', models.DateTimeField()),
                ('commercials_labeled', models.BooleanField(default=False)),
                ('srt_extension', models.CharField(max_length=256)),
                ('channel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.Channel')),
                ('show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.Show')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VideoTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.Tag')),
                ('video', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.Video')),
            ],
        ),
        migrations.AddField(
            model_name='thing',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.ThingType'),
        ),
        migrations.AddField(
            model_name='speaker',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.Video'),
        ),
        migrations.AddField(
            model_name='shot',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.Video'),
        ),
        migrations.AddField(
            model_name='segment',
            name='things',
            field=models.ManyToManyField(to='query.Thing'),
        ),
        migrations.AddField(
            model_name='segment',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.Video'),
        ),
        migrations.AddField(
            model_name='identity',
            name='thing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='query.Thing'),
        ),
        migrations.AddField(
            model_name='frame',
            name='tags',
            field=models.ManyToManyField(to='query.Tag'),
        ),
        migrations.AddField(
            model_name='frame',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.Video'),
        ),
        migrations.AddField(
            model_name='faceidentity',
            name='identity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.Thing'),
        ),
        migrations.AddField(
            model_name='faceidentity',
            name='labeler',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.Labeler'),
        ),
        migrations.AddField(
            model_name='facegender',
            name='gender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.Gender'),
        ),
        migrations.AddField(
            model_name='facegender',
            name='labeler',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.Labeler'),
        ),
        migrations.AddField(
            model_name='facefeatures',
            name='labeler',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.Labeler'),
        ),
        migrations.AddField(
            model_name='face',
            name='labeler',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.Labeler'),
        ),
        migrations.AddField(
            model_name='face',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.Person'),
        ),
        migrations.AddField(
            model_name='face',
            name='shot',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='query.Shot'),
        ),
        migrations.AddField(
            model_name='commercial',
            name='labeler',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.Labeler'),
        ),
        migrations.AddField(
            model_name='commercial',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='query.Video'),
        ),
        migrations.AlterUniqueTogether(
            name='thing',
            unique_together=set([('name', 'type')]),
        ),
        migrations.AlterUniqueTogether(
            name='pose',
            unique_together=set([('labeler', 'person')]),
        ),
        migrations.AlterUniqueTogether(
            name='faceidentity',
            unique_together=set([('labeler', 'face')]),
        ),
        migrations.AlterUniqueTogether(
            name='facegender',
            unique_together=set([('labeler', 'face')]),
        ),
        migrations.AlterUniqueTogether(
            name='facefeatures',
            unique_together=set([('labeler', 'face')]),
        ),
        migrations.AlterUniqueTogether(
            name='face',
            unique_together=set([('labeler', 'person')]),
        ),
    ]
