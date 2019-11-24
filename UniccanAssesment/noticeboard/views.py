from django.shortcuts import render,HttpResponse

from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import NoticeBoard

def index(request):
	return HttpResponse("""<a href="/noticeboard-createview/">Create Notice</a><br>
						   <a href="/noticeboard-listview/">List Notices</a>""")

class NoticeBoardCreateView(CreateView):
    model = NoticeBoard
    fields = ['title','text']
    success_url = '/'

class NoticeBoardDeleteView(DeleteView):
    model = NoticeBoard
    template_name_suffix='_delete'
    success_url = '/'

class NoticeBoardListView(ListView):

    model = NoticeBoard
  # paginate_by = 100  # if pagination is desired

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class NoticeBoardDetailView(DetailView):
    model = NoticeBoard

class NoticeBoardUpdateView(UpdateView):
    model = NoticeBoard
    success_url = '/'
    template_name_suffix ='_form'
    fields = ['text','title']
