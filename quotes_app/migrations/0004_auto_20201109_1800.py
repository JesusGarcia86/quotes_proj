# Generated by Django 2.2 on 2020-11-09 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotes_app', '0003_auto_20201109_0558'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessagePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='job',
            name='added_users',
        ),
        migrations.RemoveField(
            model_name='job',
            name='categories',
        ),
        migrations.RemoveField(
            model_name='job',
            name='created_by_user',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='user',
            name='updated_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Job',
        ),
        migrations.AddField(
            model_name='messagepost',
            name='poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='quotes_app.User'),
        ),
        migrations.AddField(
            model_name='messagepost',
            name='user_likes',
            field=models.ManyToManyField(related_name='liked_posts', to='quotes_app.User'),
        ),
    ]
