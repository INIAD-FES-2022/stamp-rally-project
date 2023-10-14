from .models import Stamp
from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin

# ここにQRが持つクエリパラメータを陳列
# https://stampのトップページURL/?sponser=クエリパラメータ
query_lst = ["dummy0", "dummy1", "dummy2", "dummy3", "dummy4", "dummy5"]

class stamp(LoginRequiredMixin, TemplateView):
    template_name = "stamp/stamp.html"
    def get_context_data(self, **kwargs):

        # ユーザー情報取得
        try:
            user_info = Stamp.objects.get(user=self.request.user)

        # 初期設定
        except Stamp.DoesNotExist:
            Stamp.objects.create(user=self.request.user, stamps=[False,False,False,False,False,False])
            user_info = Stamp.objects.get(user=self.request.user)
            print("ユーザー情報を新規作成しました。")

        # htmlに渡すテンプレートの値
        # {{ user }} や {{ stamps }} で取得可能

        # {{ user }} は各ユーザーが持つ一意の文字列
        # {{ stamps }} はbool値のリスト
        context = super().get_context_data(**kwargs)
        context["user"] = user_info.user
        context["stamps"] = user_info.stamps

        # スタンプ付与
        if "sponser" in self.request.GET:
            query = self.request.GET.get("sponser")
            if query in query_lst:
                update_stamps = user_info.stamps
                update_stamps[query_lst.index(query)] = True
                
                user_info.stamps = update_stamps
                user_info.save()

                context["stamps"] = update_stamps

            # デバッグ用
            elif query == "reset":
                update_stamps = user_info.stamps
                update_stamps = [False,False,False,False,False,False]
                
                user_info.stamps = update_stamps
                user_info.save()

                context["stamps"] = update_stamps

            # デバッグ用                
            elif query == "print":
                print(context["user"])
                print(context["stamps"])

        return context

class redirect_stamp(RedirectView):
    url = "http://127.0.0.1:8000/stamp/"
rd_index = redirect_stamp.as_view()