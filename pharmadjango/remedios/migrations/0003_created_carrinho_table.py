# Generated by Django 4.2.1 on 2023-06-01 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remedios', '0002_alter_remedio_precisa_receita'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrinho',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remedios', models.JSONField()),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
    ]