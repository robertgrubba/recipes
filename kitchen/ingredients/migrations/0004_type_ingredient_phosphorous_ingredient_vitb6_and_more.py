# Generated by Django 4.0.4 on 2022-05-10 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ingredients', '0003_alter_ingredient_fat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='ingredient',
            name='phosphorous',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='vitb6',
            field=models.FloatField(default=None),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='water',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='zinc',
            field=models.FloatField(default=None),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='carbohydrates',
            field=models.FloatField(help_text='Carbohydrates in 100g [mg]'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='dietaryfiber',
            field=models.FloatField(help_text='Dietary Fiber [g]'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='potasium',
            field=models.FloatField(help_text='Potasium in 100g [mg]'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='protein',
            field=models.FloatField(help_text='Protein in 100g [g]'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='sodium',
            field=models.FloatField(help_text='Sodium in 100g [mg]'),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='vita',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='vitc',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ingredients.type'),
        ),
    ]
