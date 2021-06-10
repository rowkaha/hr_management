# Generated by Django 3.2.3 on 2021-06-10 10:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hr_management_app', '0006_remove_staffs_office_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffs',
            name='office_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='hr_management_app.office'),
            preserve_default=False,
        ),
    ]
