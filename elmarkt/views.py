from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Participant, Supplier

from .serializers import ParticipantCreateSerializer, ParticipantSerializer, SupplierCreateSerializer, SupplierSerializer
from rest_framework.pagination import LimitOffsetPagination
from .permissions import IsEmployee


class ParticipantCreateView(CreateAPIView):
    """
    Create Participant
    """
    model = Participant
    permission_classes = [IsAuthenticated, IsEmployee]
    serializer_class = ParticipantCreateSerializer


class ParticipantListView(ListAPIView):
    """
    View Participant's list
    """
    queryset = Participant.objects.all()
    permission_classes = [IsAuthenticated, IsEmployee]
    pagination_class = LimitOffsetPagination
    serializer_class = ParticipantSerializer

    def get_queryset(self) -> list[Participant]:

        queryset = Participant.objects.all()
        country = self.request.query_params.get('country')
        if country is not None:
            queryset = queryset.filter(contact__country__contains=country)
        return queryset


class ParticipantView(RetrieveUpdateDestroyAPIView):
    """
    View Participant
    """
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    permission_classes = [IsAuthenticated, IsEmployee]
    
    def get_queryset(self):
        return super().get_queryset()


class SupplierCreateView(CreateAPIView):
    """
    Create Supplier
    """
    model = Supplier
    permission_classes = [IsAuthenticated, IsEmployee]
    serializer_class = SupplierCreateSerializer


class SupplierListView(ListAPIView):
    """
    View Supplier's list
    """
    queryset = Supplier.objects.all()
    permission_classes = [IsAuthenticated, IsEmployee]
    pagination_class = LimitOffsetPagination
    serializer_class = SupplierSerializer

    def get_queryset(self):
        return super().get_queryset()


class SupplierView(RetrieveUpdateDestroyAPIView):
    """
    View Supplier
    """
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated, IsEmployee]

    def get_queryset(self):
        return super().get_queryset()
