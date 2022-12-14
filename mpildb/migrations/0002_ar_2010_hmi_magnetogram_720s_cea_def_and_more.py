# Generated by Django 4.1.2 on 2022-10-28 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mpildb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AR_2010_HMI_Magnetogram_720s_CEA_Def',
            fields=[
                ('harp_num', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField()),
                ('noaar_nums', models.CharField(max_length=1000)),
                ('num_pils', models.PositiveIntegerField()),
                ('sum_pil_length', models.PositiveIntegerField()),
                ('sum_ropi_area', models.PositiveIntegerField()),
                ('sum_mag_field_strength', models.DecimalField(decimal_places=10, max_digits=20)),
                ('fra_dim', models.DecimalField(decimal_places=10, max_digits=20)),
                ('eige_vals', models.CharField(max_length=500)),
                ('convexity', models.DecimalField(decimal_places=10, max_digits=20)),
                ('hu1', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu2', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu3', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu4', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu5', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu6', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu7', models.DecimalField(decimal_places=10, max_digits=30)),
                ('patch_shape', models.CharField(max_length=50)),
                ('detection_flag', models.BooleanField(default=False)),
                ('instrument', models.CharField(max_length=50)),
                ('series', models.CharField(max_length=50)),
                ('projection', models.CharField(max_length=50)),
                ('cadence', models.CharField(max_length=50)),
                ('data_segment', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AR_2011_HMI_Magnetogram_720s_CEA_Def',
            fields=[
                ('harp_num', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField()),
                ('noaar_nums', models.CharField(max_length=1000)),
                ('num_pils', models.PositiveIntegerField()),
                ('sum_pil_length', models.PositiveIntegerField()),
                ('sum_ropi_area', models.PositiveIntegerField()),
                ('sum_mag_field_strength', models.DecimalField(decimal_places=10, max_digits=20)),
                ('fra_dim', models.DecimalField(decimal_places=10, max_digits=20)),
                ('eige_vals', models.CharField(max_length=500)),
                ('convexity', models.DecimalField(decimal_places=10, max_digits=20)),
                ('hu1', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu2', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu3', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu4', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu5', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu6', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu7', models.DecimalField(decimal_places=10, max_digits=30)),
                ('patch_shape', models.CharField(max_length=50)),
                ('detection_flag', models.BooleanField(default=False)),
                ('instrument', models.CharField(max_length=50)),
                ('series', models.CharField(max_length=50)),
                ('projection', models.CharField(max_length=50)),
                ('cadence', models.CharField(max_length=50)),
                ('data_segment', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AR_2012_HMI_Magnetogram_720s_CEA_Def',
            fields=[
                ('harp_num', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField()),
                ('noaar_nums', models.CharField(max_length=1000)),
                ('num_pils', models.PositiveIntegerField()),
                ('sum_pil_length', models.PositiveIntegerField()),
                ('sum_ropi_area', models.PositiveIntegerField()),
                ('sum_mag_field_strength', models.DecimalField(decimal_places=10, max_digits=20)),
                ('fra_dim', models.DecimalField(decimal_places=10, max_digits=20)),
                ('eige_vals', models.CharField(max_length=500)),
                ('convexity', models.DecimalField(decimal_places=10, max_digits=20)),
                ('hu1', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu2', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu3', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu4', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu5', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu6', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu7', models.DecimalField(decimal_places=10, max_digits=30)),
                ('patch_shape', models.CharField(max_length=50)),
                ('detection_flag', models.BooleanField(default=False)),
                ('instrument', models.CharField(max_length=50)),
                ('series', models.CharField(max_length=50)),
                ('projection', models.CharField(max_length=50)),
                ('cadence', models.CharField(max_length=50)),
                ('data_segment', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AR_2013_HMI_Magnetogram_720s_CEA_Def',
            fields=[
                ('harp_num', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField()),
                ('noaar_nums', models.CharField(max_length=1000)),
                ('num_pils', models.PositiveIntegerField()),
                ('sum_pil_length', models.PositiveIntegerField()),
                ('sum_ropi_area', models.PositiveIntegerField()),
                ('sum_mag_field_strength', models.DecimalField(decimal_places=10, max_digits=20)),
                ('fra_dim', models.DecimalField(decimal_places=10, max_digits=20)),
                ('eige_vals', models.CharField(max_length=500)),
                ('convexity', models.DecimalField(decimal_places=10, max_digits=20)),
                ('hu1', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu2', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu3', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu4', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu5', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu6', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu7', models.DecimalField(decimal_places=10, max_digits=30)),
                ('patch_shape', models.CharField(max_length=50)),
                ('detection_flag', models.BooleanField(default=False)),
                ('instrument', models.CharField(max_length=50)),
                ('series', models.CharField(max_length=50)),
                ('projection', models.CharField(max_length=50)),
                ('cadence', models.CharField(max_length=50)),
                ('data_segment', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AR_2014_HMI_Magnetogram_720s_CEA_Def',
            fields=[
                ('harp_num', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField()),
                ('noaar_nums', models.CharField(max_length=1000)),
                ('num_pils', models.PositiveIntegerField()),
                ('sum_pil_length', models.PositiveIntegerField()),
                ('sum_ropi_area', models.PositiveIntegerField()),
                ('sum_mag_field_strength', models.DecimalField(decimal_places=10, max_digits=20)),
                ('fra_dim', models.DecimalField(decimal_places=10, max_digits=20)),
                ('eige_vals', models.CharField(max_length=500)),
                ('convexity', models.DecimalField(decimal_places=10, max_digits=20)),
                ('hu1', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu2', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu3', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu4', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu5', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu6', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu7', models.DecimalField(decimal_places=10, max_digits=30)),
                ('patch_shape', models.CharField(max_length=50)),
                ('detection_flag', models.BooleanField(default=False)),
                ('instrument', models.CharField(max_length=50)),
                ('series', models.CharField(max_length=50)),
                ('projection', models.CharField(max_length=50)),
                ('cadence', models.CharField(max_length=50)),
                ('data_segment', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AR_2015_HMI_Magnetogram_720s_CEA_Def',
            fields=[
                ('harp_num', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField()),
                ('noaar_nums', models.CharField(max_length=1000)),
                ('num_pils', models.PositiveIntegerField()),
                ('sum_pil_length', models.PositiveIntegerField()),
                ('sum_ropi_area', models.PositiveIntegerField()),
                ('sum_mag_field_strength', models.DecimalField(decimal_places=10, max_digits=20)),
                ('fra_dim', models.DecimalField(decimal_places=10, max_digits=20)),
                ('eige_vals', models.CharField(max_length=500)),
                ('convexity', models.DecimalField(decimal_places=10, max_digits=20)),
                ('hu1', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu2', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu3', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu4', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu5', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu6', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu7', models.DecimalField(decimal_places=10, max_digits=30)),
                ('patch_shape', models.CharField(max_length=50)),
                ('detection_flag', models.BooleanField(default=False)),
                ('instrument', models.CharField(max_length=50)),
                ('series', models.CharField(max_length=50)),
                ('projection', models.CharField(max_length=50)),
                ('cadence', models.CharField(max_length=50)),
                ('data_segment', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AR_2016_HMI_Magnetogram_720s_CEA_Def',
            fields=[
                ('harp_num', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField()),
                ('noaar_nums', models.CharField(max_length=1000)),
                ('num_pils', models.PositiveIntegerField()),
                ('sum_pil_length', models.PositiveIntegerField()),
                ('sum_ropi_area', models.PositiveIntegerField()),
                ('sum_mag_field_strength', models.DecimalField(decimal_places=10, max_digits=20)),
                ('fra_dim', models.DecimalField(decimal_places=10, max_digits=20)),
                ('eige_vals', models.CharField(max_length=500)),
                ('convexity', models.DecimalField(decimal_places=10, max_digits=20)),
                ('hu1', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu2', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu3', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu4', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu5', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu6', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu7', models.DecimalField(decimal_places=10, max_digits=30)),
                ('patch_shape', models.CharField(max_length=50)),
                ('detection_flag', models.BooleanField(default=False)),
                ('instrument', models.CharField(max_length=50)),
                ('series', models.CharField(max_length=50)),
                ('projection', models.CharField(max_length=50)),
                ('cadence', models.CharField(max_length=50)),
                ('data_segment', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AR_2017_HMI_Magnetogram_720s_CEA_Def',
            fields=[
                ('harp_num', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField()),
                ('noaar_nums', models.CharField(max_length=1000)),
                ('num_pils', models.PositiveIntegerField()),
                ('sum_pil_length', models.PositiveIntegerField()),
                ('sum_ropi_area', models.PositiveIntegerField()),
                ('sum_mag_field_strength', models.DecimalField(decimal_places=10, max_digits=20)),
                ('fra_dim', models.DecimalField(decimal_places=10, max_digits=20)),
                ('eige_vals', models.CharField(max_length=500)),
                ('convexity', models.DecimalField(decimal_places=10, max_digits=20)),
                ('hu1', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu2', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu3', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu4', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu5', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu6', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu7', models.DecimalField(decimal_places=10, max_digits=30)),
                ('patch_shape', models.CharField(max_length=50)),
                ('detection_flag', models.BooleanField(default=False)),
                ('instrument', models.CharField(max_length=50)),
                ('series', models.CharField(max_length=50)),
                ('projection', models.CharField(max_length=50)),
                ('cadence', models.CharField(max_length=50)),
                ('data_segment', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AR_2018_HMI_Magnetogram_720s_CEA_Def',
            fields=[
                ('harp_num', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField()),
                ('noaar_nums', models.CharField(max_length=1000)),
                ('num_pils', models.PositiveIntegerField()),
                ('sum_pil_length', models.PositiveIntegerField()),
                ('sum_ropi_area', models.PositiveIntegerField()),
                ('sum_mag_field_strength', models.DecimalField(decimal_places=10, max_digits=20)),
                ('fra_dim', models.DecimalField(decimal_places=10, max_digits=20)),
                ('eige_vals', models.CharField(max_length=500)),
                ('convexity', models.DecimalField(decimal_places=10, max_digits=20)),
                ('hu1', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu2', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu3', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu4', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu5', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu6', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu7', models.DecimalField(decimal_places=10, max_digits=30)),
                ('patch_shape', models.CharField(max_length=50)),
                ('detection_flag', models.BooleanField(default=False)),
                ('instrument', models.CharField(max_length=50)),
                ('series', models.CharField(max_length=50)),
                ('projection', models.CharField(max_length=50)),
                ('cadence', models.CharField(max_length=50)),
                ('data_segment', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AR_2019_HMI_Magnetogram_720s_CEA_Def',
            fields=[
                ('harp_num', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField()),
                ('noaar_nums', models.CharField(max_length=1000)),
                ('num_pils', models.PositiveIntegerField()),
                ('sum_pil_length', models.PositiveIntegerField()),
                ('sum_ropi_area', models.PositiveIntegerField()),
                ('sum_mag_field_strength', models.DecimalField(decimal_places=10, max_digits=20)),
                ('fra_dim', models.DecimalField(decimal_places=10, max_digits=20)),
                ('eige_vals', models.CharField(max_length=500)),
                ('convexity', models.DecimalField(decimal_places=10, max_digits=20)),
                ('hu1', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu2', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu3', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu4', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu5', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu6', models.DecimalField(decimal_places=10, max_digits=30)),
                ('hu7', models.DecimalField(decimal_places=10, max_digits=30)),
                ('patch_shape', models.CharField(max_length=50)),
                ('detection_flag', models.BooleanField(default=False)),
                ('instrument', models.CharField(max_length=50)),
                ('series', models.CharField(max_length=50)),
                ('projection', models.CharField(max_length=50)),
                ('cadence', models.CharField(max_length=50)),
                ('data_segment', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ARMetadata',
            fields=[
                ('harp_num', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('noaar_nums', models.CharField(max_length=1000)),
                ('start_time', models.DateTimeField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Test',
        ),
    ]
