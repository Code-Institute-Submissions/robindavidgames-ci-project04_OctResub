# Generated by Django 3.2 on 2022-07-08 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20220708_1053'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecipeTags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag_name', models.CharField(max_length=100, unique=True)),
                ('recipes', models.ManyToManyField(to='recipes.Recipe')),
            ],
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
