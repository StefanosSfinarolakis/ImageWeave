
# Generated by Django 3.2.8 on 2023-03-23 21:38

# Generated by Django 3.2.8 on 2023-03-23 21:28


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profileimg',
            field=models.ImageField(default='blank_profile_picture.png', upload_to='profile_images'),
        ),
    ]
