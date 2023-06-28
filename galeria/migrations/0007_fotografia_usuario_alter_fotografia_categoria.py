# Generated by Django 4.2.2 on 2023-06-28 01:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('galeria', '0006_alter_fotografia_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('NEBULOSA', 'Nebulosa'), ('GALÁXIA', 'Galáxia'), ('ESTRELA', 'Estrela'), ('PLANETA', 'Planeta')], default='', max_length=100),
        ),
    ]
