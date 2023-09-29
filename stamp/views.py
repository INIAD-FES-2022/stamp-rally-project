from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView

# Create your views here.

class stamp(TemplateView):
    template_name = "stamp/stamp.html"

class redirect_stamp(RedirectView):
    url = "http://127.0.0.1:8000/stamp/"
rd_index = redirect_stamp.as_view()