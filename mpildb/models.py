from django.db import models

# Creation of the models 

class ARMetadata(models.Model):
    harp_num = models.CharField(max_length=50, primary_key=True)
    start_time = models.DateTimeField(null=True)
    noaar_nums = models.CharField(max_length=1000)

class ARMagnetogramByYear(models.Model):
    harp_num = models.CharField(max_length=50, primary_key=True)
    start_time = models.DateTimeField(null=False)
    noaar_nums = models.CharField(max_length=1000)
    num_pils = models.PositiveIntegerField()
    sum_pil_length = models.PositiveIntegerField()
    sum_ropi_area = models.PositiveIntegerField()
    sum_mag_field_strength = models.DecimalField(max_digits=20, decimal_places=10)
    fra_dim = models.DecimalField(max_digits=20, decimal_places=10)
    eige_vals = models.CharField(max_length=500)
    convexity = models.DecimalField(max_digits=20, decimal_places=10)
    hu1 = models.DecimalField(max_digits=30, decimal_places=10)
    hu2 = models.DecimalField(max_digits=30, decimal_places=10)
    hu3 = models.DecimalField(max_digits=30, decimal_places=10)
    hu4 = models.DecimalField(max_digits=30, decimal_places=10)
    hu5 = models.DecimalField(max_digits=30, decimal_places=10)
    hu6 = models.DecimalField(max_digits=30, decimal_places=10)
    hu7  = models.DecimalField(max_digits=30, decimal_places=10)
    patch_shape = models.CharField(max_length=50)
    detection_flag = models.BooleanField(default=False)
    instrument = models.CharField(max_length=50)
    series = models.CharField(max_length=50)
    projection = models.CharField(max_length=50) 
    cadence = models.CharField(max_length=50) 
    data_segment = models.CharField(max_length=50)
     
    class Meta:
        abstract = True

class AR_2010_HMI_Magnetogram_720s_CEA_Def(ARMagnetogramByYear):
    pass

class AR_2011_HMI_Magnetogram_720s_CEA_Def(ARMagnetogramByYear):
    pass

class AR_2012_HMI_Magnetogram_720s_CEA_Def(ARMagnetogramByYear):
    pass

class AR_2013_HMI_Magnetogram_720s_CEA_Def(ARMagnetogramByYear):
    pass

class AR_2014_HMI_Magnetogram_720s_CEA_Def(ARMagnetogramByYear):
    pass

class AR_2015_HMI_Magnetogram_720s_CEA_Def(ARMagnetogramByYear):
    pass

class AR_2016_HMI_Magnetogram_720s_CEA_Def(ARMagnetogramByYear):
    pass

class AR_2017_HMI_Magnetogram_720s_CEA_Def(ARMagnetogramByYear):
    pass

class AR_2018_HMI_Magnetogram_720s_CEA_Def(ARMagnetogramByYear):
    pass

class AR_2019_HMI_Magnetogram_720s_CEA_Def(ARMagnetogramByYear):
    pass