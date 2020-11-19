# Generated by Django 3.1.3 on 2020-11-19 04:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('LibraryApp', '0003_auto_20201119_0450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activeuser',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Book', to='LibraryApp.book'),
        ),
        migrations.AlterField(
            model_name='activeuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True),
        ),
    ]
