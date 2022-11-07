import datetime

from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from reservation.models import Listing, Room, Reservation, Calendar
from reservation.serializers import ListingSerializer, RoomSerializer, ReservationSerializer

# FIXME: All permissions and authentication things are ignored because of the task scope


class ListingViewSet(ModelViewSet):
    serializer_class = ListingSerializer
    queryset = Listing.objects.all()


class RoomViewSet(ModelViewSet):
    serializer_class = RoomSerializer

    def get_queryset(self):
        listing_id = self.kwargs.get('listing_id')
        return Room.objects.filter(listing_id=listing_id)

    def perform_create(self, serializer):
        listing_id = self.kwargs.get('listing_id')
        serializer.save(listing_id=listing_id)


class ReservationViewSet(ModelViewSet):
    serializer_class = ReservationSerializer

    def get_queryset(self):
        room_id = self.kwargs.get('room_id')
        print(self.request.data, '** '*100)
        return Reservation.objects.filter(room_id=room_id)

    def perform_create(self, serializer):
        reserve_duration = self.request.data.get('reserve_duration')
        reserved_from_date = self.request.data.get('reserved_from_date')
        listing_id = self.kwargs.get('listing_id')
        room_id = self.kwargs.get('room_id')
        reservation_instance = serializer.save(room_id=room_id)
        for d in range(reserve_duration):
            date = datetime.datetime.strptime(reserved_from_date, '%Y-%m-%d').date() + datetime.timedelta(days=d+1)
            print(date, '#' * 100)
            c = Calendar(date=date, listing_id=listing_id, room_id=room_id, reservation=reservation_instance)
            c.save()

