from .models import Stamp
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# 各地のQRが持つURL
# https://ドメイン/stamp/get/UUID/

# パンフレットに載せるQRが持つURL
# https://ドメイン/stamp/ もしくは https://ドメイン/login/

# 各協賛のUUID
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
            Stamp.objects.create(user=self.request.user, stamps=[False,False,False,False,False,False])
            user_info = Stamp.objects.get(user=self.request.user)
            print("ユーザー情報を新規作成しました。")

        # htmlに渡すテンプレートの値
        # {{ user }} や {{ stamps }} で取得可能

        # {{ user }} は各ユーザーが持つ一意の文字列
        # {{ stamps }} はbool値のリスト
        # {{ stamps[0]~[4] が各地のスタンプ、stamps[5] は景品の獲得有無 }}

        context = super().get_context_data(**kwargs)
        context["user"] = user_info.user
        context["stamps"] = user_info.stamps

        return context
    
class stamp_get(LoginRequiredMixin, TemplateView):
    template_name = "stamp/stamp_get.html"
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
        # {{ user }} や {{ stamped }} で取得可能

        # {{ user }} は各ユーザーが持つ一意の文字列
        # {{ stamped }} はスタンプが新たに押されたかどうかのbool値
            # 初回のみ演出ではない場合、無視してもらって大丈夫です。

        context = super().get_context_data(**kwargs)
        context["user"] = user_info.user
        context["stamped"] = False

        # スタンプ付与
        query = self.kwargs["sponser"]
        if query in query_lst:
            update_stamps = user_info.stamps
            if not update_stamps[query_lst.index(query)]:
                context["stamped"] = True
            update_stamps[query_lst.index(query)] = True
                
            user_info.stamps = update_stamps
            user_info.save()

        # デバッグ用
        if query == "reset":
            update_stamps = user_info.stamps
            update_stamps = [False,False,False,False,False,False]
                
            user_info.stamps = update_stamps
            user_info.save()

            context["stamps"] = update_stamps

        # デバッグ用                
        elif query == "print":
            print(context["user"])
            print(context["stamped"])
            print(user_info.stamps)

        return context
    
class stamp_prize(LoginRequiredMixin, TemplateView):
    template_name = "stamp/stamp_prize.html"
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
        # {{ stamps[0]~[4] が各地のスタンプ、stamps[5] は景品の獲得有無 }}

        context = super().get_context_data(**kwargs)
        context["user"] = user_info.user
        context["stamps"] = user_info.stamps

        # 景品の管理
        query = self.request.GET.get("used")
        if query=="true":
            update_stamps = user_info.stamps
            update_stamps[5] = True
                
            user_info.stamps = update_stamps
            user_info.save()

            context["stamps"] = update_stamps

        return context

class stamp_map(LoginRequiredMixin, TemplateView):
    template_name = "stamp/stamp_map.html"