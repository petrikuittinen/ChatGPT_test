from django.urls import path
from .views import GuestbookListView, GuestbookCreateView

app_name = 'guestbook'

urlpatterns = [
    path('', GuestbookListView.as_view(), name='guestbook'),
    path('add/', GuestbookCreateView.as_view(), name='add_guestbook_post'),
]
