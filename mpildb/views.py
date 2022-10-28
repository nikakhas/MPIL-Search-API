from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializers import (ARMetadataSerializer, AR_2010_HMI_Magnetogram_720s_CEA_DefSerializer, 
AR_2011_HMI_Magnetogram_720s_CEA_DefSerializer, AR_2012_HMI_Magnetogram_720s_CEA_DefSerializer, 
AR_2013_HMI_Magnetogram_720s_CEA_DefSerializer, AR_2014_HMI_Magnetogram_720s_CEA_DefSerializer, AR_2015_HMI_Magnetogram_720s_CEA_DefSerializer, 
AR_2016_HMI_Magnetogram_720s_CEA_DefSerializer, AR_2017_HMI_Magnetogram_720s_CEA_DefSerializer, AR_2018_HMI_Magnetogram_720s_CEA_DefSerializer, 
AR_2019_HMI_Magnetogram_720s_CEA_DefSerializer)

from .models import (ARMetadata, AR_2010_HMI_Magnetogram_720s_CEA_Def, AR_2011_HMI_Magnetogram_720s_CEA_Def, AR_2012_HMI_Magnetogram_720s_CEA_Def, 
AR_2013_HMI_Magnetogram_720s_CEA_Def, AR_2014_HMI_Magnetogram_720s_CEA_Def, AR_2015_HMI_Magnetogram_720s_CEA_Def, AR_2016_HMI_Magnetogram_720s_CEA_Def, 
AR_2017_HMI_Magnetogram_720s_CEA_Def, AR_2018_HMI_Magnetogram_720s_CEA_Def, AR_2019_HMI_Magnetogram_720s_CEA_Def)

class ARMetadataViewSet(viewsets.ModelViewSet):
    queryset = ARMetadata.objects.all().order_by('harp_num')
    serializer_class = ARMetadataSerializer

class AR_2010_HMI_Magnetogram_720s_CEA_DefViewSet(viewsets.ModelViewSet):
    queryset = AR_2010_HMI_Magnetogram_720s_CEA_Def.objects.all().order_by('harp_num')
    serializer_class = AR_2010_HMI_Magnetogram_720s_CEA_DefSerializer

class AR_2011_HMI_Magnetogram_720s_CEA_DefViewSet(viewsets.ModelViewSet):
    queryset = AR_2011_HMI_Magnetogram_720s_CEA_Def.objects.all().order_by('harp_num')
    serializer_class = AR_2011_HMI_Magnetogram_720s_CEA_DefSerializer

class AR_2012_HMI_Magnetogram_720s_CEA_DefViewSet(viewsets.ModelViewSet):
    queryset = AR_2012_HMI_Magnetogram_720s_CEA_Def.objects.all().order_by('harp_num')
    serializer_class = AR_2012_HMI_Magnetogram_720s_CEA_DefSerializer

class AR_2013_HMI_Magnetogram_720s_CEA_DefViewSet(viewsets.ModelViewSet):
    queryset = AR_2013_HMI_Magnetogram_720s_CEA_Def.objects.all().order_by('harp_num')
    serializer_class = AR_2013_HMI_Magnetogram_720s_CEA_DefSerializer

class AR_2014_HMI_Magnetogram_720s_CEA_DefViewSet(viewsets.ModelViewSet):
    queryset = AR_2014_HMI_Magnetogram_720s_CEA_Def.objects.all().order_by('harp_num')
    serializer_class = AR_2014_HMI_Magnetogram_720s_CEA_DefSerializer

class AR_2015_HMI_Magnetogram_720s_CEA_DefViewSet(viewsets.ModelViewSet):
    queryset = AR_2015_HMI_Magnetogram_720s_CEA_Def.objects.all().order_by('harp_num')
    serializer_class = AR_2015_HMI_Magnetogram_720s_CEA_DefSerializer

class AR_2016_HMI_Magnetogram_720s_CEA_DefViewSet(viewsets.ModelViewSet):
    queryset = AR_2016_HMI_Magnetogram_720s_CEA_Def.objects.all().order_by('harp_num')
    serializer_class = AR_2016_HMI_Magnetogram_720s_CEA_DefSerializer

class AR_2017_HMI_Magnetogram_720s_CEA_DefViewSet(viewsets.ModelViewSet):
    queryset = AR_2017_HMI_Magnetogram_720s_CEA_Def.objects.all().order_by('harp_num')
    serializer_class = AR_2017_HMI_Magnetogram_720s_CEA_DefSerializer

class AR_2018_HMI_Magnetogram_720s_CEA_DefViewSet(viewsets.ModelViewSet):
    queryset = AR_2018_HMI_Magnetogram_720s_CEA_Def.objects.all().order_by('harp_num')
    serializer_class = AR_2018_HMI_Magnetogram_720s_CEA_DefSerializer

class AR_2019_HMI_Magnetogram_720s_CEA_DefViewSet(viewsets.ModelViewSet):
    queryset = AR_2019_HMI_Magnetogram_720s_CEA_Def.objects.all().order_by('harp_num')
    serializer_class = AR_2019_HMI_Magnetogram_720s_CEA_DefSerializer

       