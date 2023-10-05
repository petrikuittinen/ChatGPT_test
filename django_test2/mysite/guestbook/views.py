from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from .models import Post

class GuestbookListView(ListView):
    model = Post
    template_name = 'guestbook/guestbook.html'
    context_object_name = 'latest_posts'
    ordering = ['-creation_date']
    paginate_by = 10

class GuestbookCreateView(CreateView):
    model = Post
    template_name = 'guestbook/guestbook_form.html'
    fields = ['author', 'message']
    success_url = reverse_lazy('guestbook:guestbook')
