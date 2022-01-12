from rest_framework import routers

from rest.viewsets.static_data import StaticDataViewSet

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'', StaticDataViewSet, basename="")
