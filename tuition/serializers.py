from .models import *
from rest_framework import serializers
from users.serializers import UserSerializer

class TuitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tuition
        fields = "__all__"
    
    tutor = UserSerializer(read_only = True)