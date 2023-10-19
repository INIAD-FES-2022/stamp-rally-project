from .models import Stamp
from django.shortcuts import render
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin

# ここにQRが持つクエリパラメータを陳列
# https://stampのトップページURL/?sponser=クエリパラメータ
# query_lst[0] = アピレ
# query_lst[1] = イトーヨーカドー
# query_lst[2] = Beans
# query_lst[3] = ビビオ
# query_lst[4] = キャンパス
query_lst = ["404e8cfd-2088-d1e6-3369-d00c3fb8ab4c",
             "d5ba3cc4-d672-e462-91ad-73a437ecc483",
             "9c97ecc8-e619-47d6-4373-a9961b0fef0d",
             "2c548a77-cc36-e843-ffe2-60e9c5c71869",
             "4ac4de3d-dade-8486-5918-19b33fdcfe63",]

class stamp(LoginRequiredMixin, TemplateView):
    template_name = "stamp/stamp.html"
    def get_context_data(self, **kwargs):

        # ユーザー情報取得
        try:
            user_info = Stamp.objects.get(user=self.request.user)

        # 初期設定
        except Stamp.DoesNotExist:
            Stamp.objects.create(user=self.request.user, stamps=[False,False,False,False,False])
            user_info = Stamp.objects.get(user=self.request.user)
            print("ユーザー情報を新規作成しました。")

        # htmlに渡すテンプレートの値
        # {{ user }} や {{ stamps }}、{{stamped}} で取得可能

        # {{ user }} は各ユーザーが持つ一意の文字列
        # {{ stamps }} はbool値のリスト
        # {{ stamped }} は新たに押されたスタンプの番号(query_lst基準)
        #   もし押されていない場合は10と定義します。


        context = super().get_context_data(**kwargs)
        context["user"] = user_info.user
        context["stamps"] = user_info.stamps
        context["stamped"] = 10

        # スタンプ付与
        if "sponser" in self.request.GET:
            query = self.request.GET.get("sponser")
            if query in query_lst:
                update_stamps = user_info.stamps
                if not update_stamps[query_lst.index(query)]:
                    context["stamped"] = [query_lst.index(query)]
                update_stamps[query_lst.index(query)] = True
                
                user_info.stamps = update_stamps
                user_info.save()

                context["stamps"] = update_stamps

            # デバッグ用
            elif query == "reset":
                update_stamps = user_info.stamps
                update_stamps = [False,False,False,False,False]
                
                user_info.stamps = update_stamps
                user_info.save()

                context["stamps"] = update_stamps

            # デバッグ用                
            elif query == "print":
                print(context["user"])
                print(context["stamps"])

        return context
    
class stamp_get(TemplateView):
    template_name = "stamp/stamp_get.html"

class redirect_stamp(RedirectView):
    url = "http://127.0.0.1:8000/stamp/"
rd_index = redirect_stamp.as_view()