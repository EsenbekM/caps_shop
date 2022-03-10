# Generated by Django 3.2.8 on 2022-03-10 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_cap_new_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('new_price', models.FloatField(blank=True, null=True)),
                ('cap', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cap')),
            ],
        ),
    ]
