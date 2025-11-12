import google.generativeai as genai
from django.shortcuts import render
from django.conf import settings
from .forms import AISuggestionForm
import os
# Create your views here.


def index(request):
    return render(request, 'core/index.html')


def ai_suggestion(request):
    form = AISuggestionForm()
    result = None

    if request.method == 'POST':
        form = AISuggestionForm(request.POST)
        if form.is_valid():
            mode = form.cleaned_data['mode']
            goal = form.cleaned_data['goal']

            # Gemini API設定
            genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
            model = genai.GenerativeModel("gemini-1.5-flash")

            # モードに応じてプロンプトを変更
            if mode == 'training':
                prompt = f"自宅でできる、{goal}向けの10分間トレーニングメニューを日本語で提案してください。"
            else:
                prompt = f"{goal}向けの1日の健康的な献立を日本語で提案してください。"

            # AIへ問い合わせ
            response = model.generate_content(prompt)
            result = response.text

    return render(
        request, 'core/ai_suggestion.html', {'form': form, 'result': result}
        )
