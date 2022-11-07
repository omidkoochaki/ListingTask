from rest_framework import routers

from reservation.views import ListingViewSet, RoomViewSet, ReservationViewSet

listing_router = routers.DefaultRouter()
listing_router.register(prefix='', viewset=ListingViewSet, basename='listings')
listing_urls = listing_router.urls

room_router = routers.DefaultRouter()
room_router.register(prefix='', viewset=RoomViewSet, basename='rooms')
room_urls = room_router.urls

reservation_router = routers.DefaultRouter()
reservation_router.register(prefix='', viewset=ReservationViewSet, basename='reservations')
reservation_urls = reservation_router.urls

