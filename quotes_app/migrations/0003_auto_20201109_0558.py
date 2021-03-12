# Generated by Django 2.2 on 2020-11-09 05:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotes_app', '0002_messagepost_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='messagepost',
            name='poster',
        ),
        migrations.RemoveField(
            model_name='messagepost',
            name='user_likes',
        ),
        migrations.DeleteModel(
            name='Show',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.DeleteModel(
            name='MessagePost',
        ),
        migrations.AddField(
            model_name='job',
            name='added_users',
            field=models.ManyToManyField(related_name='added_jobs', to='quotes_app.User'),
        ),
        migrations.AddField(
            model_name='job',
            name='categories',
            field=models.ManyToManyField(related_name='jobs', to='quotes_app.Category'),
        ),
        migrations.AddField(
            model_name='job',
            name='created_by_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_jobs', to='quotes_app.User'),
        ),
    ]