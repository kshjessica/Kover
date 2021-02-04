# Generated by Django 3.1.5 on 2021-02-04 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kover', '0003_auto_20210204_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='like_people',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='like_people', to='kover.people', verbose_name='관심 배우'),
        ),
        migrations.AlterField(
            model_name='user',
            name='watched_show',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='watched_show', to='kover.show', verbose_name='관람 공연'),
        ),
    ]
