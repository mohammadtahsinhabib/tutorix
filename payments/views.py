from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from payments.models import Payment
from payments.serializers import PaymentSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action


class PaymentViewSet(ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["post"], url_path="pay-tuition")
    def pay_tuition(self, request):
        pass

    @action(detail=False, methods=["post"], url_path="receive-payment")
    def receive_payment(self, request):
        pass

    @action(detail=False, methods=["get"], url_path="history")
    def history(self, request):
        pass
