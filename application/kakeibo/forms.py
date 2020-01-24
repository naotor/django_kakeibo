from django import forms
from .models import Kakeibo

class KakeiboForm(forms.ModelForm):

    class Meta:
        model = Kakeibo
        fields = [
            'date',
            'category',
            'money',
            'memo',
        ]
        labels = {
            'date': '日付',
            'category': 'カテゴリ',
            'money': '金額',
            'memo': 'メモ',
        }
        widgets = {
            'category': forms.Select(
                attrs={'class': 'ui fluid search dropdown'}
            )
        }

    def __init__(self, *args, **kwargs):
        super(KakeiboForm, self).__init__(*args, **kwargs)

        # プレースホルダの一括設定
        for key, field in self.fields.items():
            field.widget.attrs.update({'placeholder': field.label})