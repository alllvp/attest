# Generated by Django 4.1.5 on 2023-01-21 20:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, unique=True, verbose_name='Email')),
                ('country', models.CharField(blank=True, max_length=100, verbose_name='Страна')),
                ('city', models.CharField(blank=True, max_length=100, verbose_name='Город')),
                ('street', models.CharField(blank=True, max_length=100, verbose_name='Улица')),
                ('number', models.CharField(blank=True, max_length=10, verbose_name='Номер дома')),
            ],
            options={
                'verbose_name': 'Контакт',
                'verbose_name_plural': 'Контакты',
            },
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Название')),
                ('level', models.PositiveSmallIntegerField(choices=[(0, 'Завод'), (1, 'Розничная сеть'), (2, 'Индивидуальный предприниматель')], default=2, verbose_name='Уровень')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='elmarkt.contact', verbose_name='Контактная информация')),
            ],
            options={
                'verbose_name': 'Участник',
                'verbose_name_plural': 'Участники',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('debt', models.PositiveIntegerField(default=0, verbose_name='Задолженность (в копейках)')),
                ('buyer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='buyer', to='elmarkt.participant', verbose_name='Покупатель')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='seller', to='elmarkt.participant', verbose_name='Продавец')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('model', models.CharField(max_length=255, verbose_name='Модель')),
                ('issued', models.DateTimeField(auto_now_add=True, verbose_name='Дата выхода')),
                ('sellers', models.ManyToManyField(blank=True, related_name='sellers', to='elmarkt.participant')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
        migrations.AddField(
            model_name='participant',
            name='products',
            field=models.ManyToManyField(blank=True, related_name='products', to='elmarkt.product'),
        ),
    ]
