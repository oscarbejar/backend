# Generated by Django 4.1.2 on 2022-10-30 23:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryLugar',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.basemodel')),
                ('description', models.CharField(max_length=50, unique=True, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Categoria de Lugar',
                'verbose_name_plural': 'Categorias de Lugares',
            },
            bases=('base.basemodel',),
        ),
        migrations.CreateModel(
            name='LugarUnit',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.basemodel')),
                ('description', models.CharField(max_length=50, unique=True, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Lugar Unit',
                'verbose_name_plural': 'Lugares Units',
            },
            bases=('base.basemodel',),
        ),
        migrations.CreateModel(
            name='Lugar',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.basemodel')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Nombre de Lugar')),
                ('description', models.TextField(verbose_name='Descripción del Lugar')),
                ('image', models.ImageField(blank=True, null=True, upload_to='lugares/', verbose_name='Imagen del Lugar')),
                ('category_lugar', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lugares.categorylugar', verbose_name='Categoria del Lugar')),
                ('lugar_unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lugares.lugarunit', verbose_name='Lugar Unit')),
            ],
            options={
                'verbose_name': 'Lugar',
                'verbose_name_plural': 'Lugares',
            },
            bases=('base.basemodel',),
        ),
        migrations.CreateModel(
            name='Indicator',
            fields=[
                ('basemodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.basemodel')),
                ('descount_value', models.PositiveSmallIntegerField(default=0)),
                ('category_lugar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lugares.categorylugar', verbose_name='Indicador de Oferta')),
            ],
            options={
                'verbose_name': 'Indicador de Oferta',
                'verbose_name_plural': 'Indicadores de Ofertas',
            },
            bases=('base.basemodel',),
        ),
        migrations.CreateModel(
            name='HistoricalLugarUnit',
            fields=[
                ('basemodel_ptr', models.ForeignKey(auto_created=True, blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, parent_link=True, related_name='+', to='base.basemodel')),
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creacion')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificacion')),
                ('description', models.CharField(db_index=True, max_length=50, verbose_name='Descripción')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Lugar Unit',
                'verbose_name_plural': 'historical Lugares Units',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalLugar',
            fields=[
                ('basemodel_ptr', models.ForeignKey(auto_created=True, blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, parent_link=True, related_name='+', to='base.basemodel')),
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creacion')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificacion')),
                ('name', models.CharField(db_index=True, max_length=150, verbose_name='Nombre de Lugar')),
                ('description', models.TextField(verbose_name='Descripción del Lugar')),
                ('image', models.TextField(blank=True, max_length=100, null=True, verbose_name='Imagen del Lugar')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('category_lugar', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='lugares.categorylugar', verbose_name='Categoria del Lugar')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('lugar_unit', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='lugares.lugarunit', verbose_name='Lugar Unit')),
            ],
            options={
                'verbose_name': 'historical Lugar',
                'verbose_name_plural': 'historical Lugares',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalIndicator',
            fields=[
                ('basemodel_ptr', models.ForeignKey(auto_created=True, blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, parent_link=True, related_name='+', to='base.basemodel')),
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creacion')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificacion')),
                ('descount_value', models.PositiveSmallIntegerField(default=0)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('category_lugar', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='lugares.categorylugar', verbose_name='Indicador de Oferta')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Indicador de Oferta',
                'verbose_name_plural': 'historical Indicadores de Ofertas',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalCategoryLugar',
            fields=[
                ('basemodel_ptr', models.ForeignKey(auto_created=True, blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, parent_link=True, related_name='+', to='base.basemodel')),
                ('id', models.IntegerField(blank=True, db_index=True)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Creacion')),
                ('modified_date', models.DateField(blank=True, editable=False, verbose_name='Fecha de Modificacion')),
                ('description', models.CharField(db_index=True, max_length=50, verbose_name='Description')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Categoria de Lugar',
                'verbose_name_plural': 'historical Categorias de Lugares',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
