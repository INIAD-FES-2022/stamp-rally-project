from .models import Stamp
from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView

# Create your views here.

class stamp(TemplateView):
    template_name = "stamp/stamp.html"
    def get_context_data(self, **kwargs):
        try:
            user_info = Stamp.objects.get(user=self.request.user)
        except Stamp.DoesNotExist:
            Stamp.objects.create(user=self.request.user, stamps=[False,False,False,False,False,False])
            user_info = Stamp.objects.get(user=self.request.user)
            print("ユーザー情報を新規作成しました。")

        context = super().get_context_data(**kwargs)
        context["user"] = user_info.user
        context["stamps"] = user_info.stamps

        return context
    
    def post(self, request, *args, **kwargs):
        try:
            user_info = Stamp.objects.get(user=self.request.user)
        except Stamp.DoesNotExist:
            Stamp.objects.create(user=self.request.user, stamps=[False,False,False,False,False,False])
            user_info = Stamp.objects.get(user=self.request.user)
            print("ユーザー情報を新規作成しました。")
        
        update_stamp = user_info.stamps
        update_stamp[request.POST["stamp_num"]] = True

        user_info.stamps = update_stamp
        user_info.save()

        return rd_index(request)

class redirect_stamp(RedirectView):
    url = "http://127.0.0.1:8000/stamp/"
rd_index = redirect_stamp.as_view()