from .permissions import IsTutorOrReadOnly
from rest_framework.viewsets import ModelViewSet
from .models import Tuition
from .serializers import *
from users.models import Tutor

class TuitionViewset(ModelViewSet):
    http_method_names = ["get","patch","delete","post"]
    serializer_class = TuitionSerializer
    permission_classes = [IsA]
    
    def get_queryset(self):
        tutor_id = self.kwargs.get('tutor_pk')
        if tutor_id:
            tutor_user = Tutor.objects.get(id=tutor_id).user
            return Tuition.objects.filter(tutor=tutor_user)
        return Tuition.objects.all()


    def perform_create(self, serializer):
        tutor_id = self.kwargs.get('tutor_pk') 
        tutor = Tutor.objects.get(id=tutor_id)
        serializer.save(tutor=tutor.user)