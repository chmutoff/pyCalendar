from django.conf.urls import url

from calendario.views import index, get_day_events, get_month_bookings,new_booking


urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^getmonthevents', get_month_bookings, name='monthevents'),
    url(r'^getdayevents', get_day_events, name='dayevents'),
    url(r'^newbooking', new_booking, name='new_booking'),

]
