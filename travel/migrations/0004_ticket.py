# Generated by Django 3.0.6 on 2020-10-24 06:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travel', '0003_delete_ticket'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(choices=[('bamenda', 'Bamenda'), ('douala', 'Douala'), ('yaounde', 'Yaounde'), ('buea', 'Buea'), ('bafoussam', 'Bafoussam'), ('ngaoundere', 'Ngaoundere')], max_length=20)),
                ('destination', models.CharField(choices=[('bamenda', 'Bamenda'), ('douala', 'Douala'), ('yaounde', 'Yaounde'), ('buea', 'Buea'), ('bafoussam', 'Bafoussam'), ('ngaoundere', 'Ngaoundere')], max_length=20)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('time', models.CharField(choices=[('morning', 'Morning'), ('evening', 'Evening')], max_length=20)),
                ('id_number', models.CharField(max_length=50)),
                ('available', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['time'],
            },
        ),
    ]
