# Generated by Django 4.1.1 on 2022-09-24 19:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apuntes', '0005_alter_apunte_options_alter_apunte_contenido_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apunte',
            name='creador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='categoriasapuntes',
            name='apunte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apuntes.apunte'),
        ),
        migrations.AlterField(
            model_name='categoriasapuntes',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apuntes.categoria'),
        ),
        migrations.AlterField(
            model_name='like',
            name='apunte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apuntes.apunte'),
        ),
        migrations.AlterField(
            model_name='like',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='apunte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apuntes.apunte'),
        ),
        migrations.AlterField(
            model_name='mensaje',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
