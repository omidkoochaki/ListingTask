from rest_framework import serializers

from reservation.models import Listing, Room, Reservation, Calendar


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['reservatore', 'reserved_from_date', 'reserve_duration']


class ReservationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['reservatore', 'reserved_from_date', 'is_paid', 'is_checked_out', 'reserve_duration']


class CalendarSerializer(serializers.ModelSerializer):
    reservation = ReservationDetailSerializer()

    class Meta:
        model = Calendar
        fields = ['date', 'reservation']


class RoomSerializer(serializers.ModelSerializer):
    calendar = CalendarSerializer(many=True)

    class Meta:
        model = Room
        fields = ['id', 'capacity', 'fee', 'calendar']


class ListingSerializer(serializers.ModelSerializer):
    rooms = RoomSerializer(many=True)

    class Meta:
        model = Listing
        fields = ['id', 'title', 'owner', 'rooms']

