# Generated by Django 3.2.2 on 2021-07-16 07:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('writer', models.CharField(default='이름을 입력해주세요', max_length=100)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Hashtag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=50)),
                ('post_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blog')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='hashtags',
            field=models.ManyToManyField(blank=True, to='blog.Hashtag'),
        ),
    ]
