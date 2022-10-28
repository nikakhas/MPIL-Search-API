from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'AR Metadata', views.ARMetadataViewSet)
router.register(r'AR 2010 HMI Magnetogram', views.AR_2010_HMI_Magnetogram_720s_CEA_DefViewSet)
router.register(r'AR 2011 HMI Magnetogram', views.AR_2011_HMI_Magnetogram_720s_CEA_DefViewSet)
router.register(r'AR 2012 HMI Magnetogram', views.AR_2012_HMI_Magnetogram_720s_CEA_DefViewSet)
router.register(r'AR 2013 HMI Magnetogram', views.AR_2013_HMI_Magnetogram_720s_CEA_DefViewSet)
router.register(r'AR 2014 HMI Magnetogram', views.AR_2014_HMI_Magnetogram_720s_CEA_DefViewSet)
router.register(r'AR 2015 HMI Magnetogram', views.AR_2015_HMI_Magnetogram_720s_CEA_DefViewSet)
router.register(r'AR 2016 HMI Magnetogram', views.AR_2016_HMI_Magnetogram_720s_CEA_DefViewSet)
router.register(r'AR 2017 HMI Magnetogram', views.AR_2017_HMI_Magnetogram_720s_CEA_DefViewSet)
router.register(r'AR 2018 HMI Magnetogram', views.AR_2018_HMI_Magnetogram_720s_CEA_DefViewSet)
router.register(r'AR 2019 HMI Magnetogram', views.AR_2019_HMI_Magnetogram_720s_CEA_DefViewSet)



# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]