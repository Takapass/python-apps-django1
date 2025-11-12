# core/forms.py
from django import forms


class AISuggestionForm(forms.Form):
    MODE_CHOICES = [
        ('training', 'トレーニングメニュー'),
        ('meal', '献立メニュー'),
    ]
    GOAL_CHOICES = [
        ('健康維持', '健康維持'),
        ('減量', '減量'),
        ('筋力アップ', '筋力アップ'),
        ('体力向上', '体力向上'),
    ]

    mode = forms.ChoiceField(
        label='提案内容', choices=MODE_CHOICES, widget=forms.RadioSelect
        )
    goal = forms.ChoiceField(label='目的', choices=GOAL_CHOICES)
