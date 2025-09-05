from rest_framework.viewsets import ModelViewSet
from .models import Tuition
from .serializers import *

class TuitionViewset(ModelViewSet):
    http_method_names = ["get","patch","delete","post"]
    queryset = Tuition.objects.all()
    serializer_class = TuitionSerializer