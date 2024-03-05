# Generated by Django 5.0.1 on 2024-02-28 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_teammembers_alter_client_options_alter_item_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='labmember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('student_id', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.DeleteModel(
            name='TeamMembers',
        ),
    ]
