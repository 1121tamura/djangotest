from django.shortcuts import render

# 追加
from django.views import generic
from django.views.generic import TemplateView
from .models import Fstatement  # この行を追加


class IndexView(TemplateView):
    template_name = 'finchart/index.html'

    # ========以下すべて追加========
    def get_context_data(self, **kwargs):
        fstatement_list = Fstatement.objects.all().order_by('company')
        params = {
            'fstatement_list': fstatement_list,
        }
        return params