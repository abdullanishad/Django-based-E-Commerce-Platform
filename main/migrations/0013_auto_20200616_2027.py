# Generated by Django 3.0.4 on 2020-06-16 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_orderdetail_panchayath'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinstance',
            name='size',
            field=models.CharField(blank=True, choices=[('Extra Small', 'Extra Small'), ('Small', 'Small'), ('Medium', 'Medium'), ('Large', 'Large'), ('Extra Large', 'Extra Large')], default='S', help_text='Book availability', max_length=20),
        ),
    ]