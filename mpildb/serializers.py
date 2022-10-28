from rest_framework import serializers 
from .models import (ARMetadata, AR_2010_HMI_Magnetogram_720s_CEA_Def, AR_2011_HMI_Magnetogram_720s_CEA_Def, AR_2012_HMI_Magnetogram_720s_CEA_Def, 
AR_2013_HMI_Magnetogram_720s_CEA_Def, AR_2014_HMI_Magnetogram_720s_CEA_Def, AR_2015_HMI_Magnetogram_720s_CEA_Def, AR_2016_HMI_Magnetogram_720s_CEA_Def, 
AR_2017_HMI_Magnetogram_720s_CEA_Def, AR_2018_HMI_Magnetogram_720s_CEA_Def, AR_2019_HMI_Magnetogram_720s_CEA_Def)

columns = ['harp_num', 'start_time', 'noaar_nums', 'num_pils', 'sum_pil_length', 
'sum_ropi_area', 'sum_mag_field_strength', 'fra_dim', 'eige_vals', 
'convexity', 'hu1', 'hu2', 'hu3', 'hu4', 'hu5', 'hu6', 'hu7', 
'patch_shape', 'detection_flag', 'instrument', 'series', 
'projection', 'cadence', 'data_segment']

class ARMetadataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ARMetadata
        fields = ['harp_num', 'start_time', 'noaar_nums']

class AR_2010_HMI_Magnetogram_720s_CEA_DefSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AR_2010_HMI_Magnetogram_720s_CEA_Def
        fields = columns

class AR_2011_HMI_Magnetogram_720s_CEA_DefSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AR_2011_HMI_Magnetogram_720s_CEA_Def
        fields = columns

class AR_2012_HMI_Magnetogram_720s_CEA_DefSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AR_2012_HMI_Magnetogram_720s_CEA_Def
        fields = columns

class AR_2013_HMI_Magnetogram_720s_CEA_DefSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AR_2013_HMI_Magnetogram_720s_CEA_Def
        fields = columns

class AR_2014_HMI_Magnetogram_720s_CEA_DefSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AR_2014_HMI_Magnetogram_720s_CEA_Def
        fields = columns

class AR_2015_HMI_Magnetogram_720s_CEA_DefSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AR_2015_HMI_Magnetogram_720s_CEA_Def
        fields = columns

class AR_2016_HMI_Magnetogram_720s_CEA_DefSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AR_2016_HMI_Magnetogram_720s_CEA_Def
        fields = columns

class AR_2017_HMI_Magnetogram_720s_CEA_DefSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AR_2017_HMI_Magnetogram_720s_CEA_Def
        fields = columns

class AR_2018_HMI_Magnetogram_720s_CEA_DefSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AR_2018_HMI_Magnetogram_720s_CEA_Def
        fields = columns

class AR_2019_HMI_Magnetogram_720s_CEA_DefSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AR_2019_HMI_Magnetogram_720s_CEA_Def
        fields = columns

