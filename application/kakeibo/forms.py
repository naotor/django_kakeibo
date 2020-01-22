from django import forms
from .models import Kakeibo

class KakeiboForm(forms.ModelForm):
    """
    支出登録・更新用フォーム
    """

    class Meta:
        model = Kakeibo
        fields = [
            'date',
            'category',
            'money',
            'memo',
        ]