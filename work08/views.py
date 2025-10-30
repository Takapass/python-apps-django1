from django.shortcuts import render, redirect, get_object_or_404
from .models import Memo

import google.generativeai as genai
#from openai import OpenAI
import os

def simple_qa(request):
    # query stringから質問を取得
    api_key = os.getenv("GEMINI_API_KEY")
    genai.configure(api_key=api_key)
    question = request.GET.get("question", "おすすめのレシピは？")

    model = genai.GenerativeModel("gemini-2.0-flash")  # または 'gemini-pro'

    prompt = "質問: {question}\n回答:".format(question=question)

    print(f"送信するプロンプト: {prompt}\n")

    # テキスト生成を実行
    response = model.generate_content(prompt)

    return HttpResponse(f"<pre>{response.text}</pre>")


#def simple_qa_openai(request):
    #client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    # query stringから質問を取得
    #question = request.GET.get("question", "おすすめのレシピは？")
    #prompt = "質問: {question}\n回答:".format(question=question)

    #response = client.chat.completions.create(
     #   model="gpt-4o-mini",  # または "gpt-4o" など
      #  messages=[{"role": "user", "content": prompt}],
    )
    #return HttpResponse(f"<pre>{response.choices[0].message.content}</pre>")


# ここにアクセス: http://127.0.0.1:8000/work11/simple_qa/?question=%E3%83%86%E3%82%B9%E3%83%88

def memo_list(request):
    memos = Memo.objects.all().order_by('-updated_at')
    return render(request, 'work08/memo_list.html', {'memos': memos})

def memo_create(request):
    memo = Memo.objects.create()  # タイトルは "no title" で作成される
    return redirect('memo_edit', memo_id=memo.id)

def memo_edit(request, memo_id):
    memo = get_object_or_404(Memo, id=memo_id)
    if request.method == 'POST':
        memo.title = request.POST.get('title')
        memo.content = request.POST.get('content')
        
        # 画像ファイルが送信された場合のみ保存
        if request.FILES.get('photo'):
            memo.photo = request.FILES['photo']
        
        memo.save()
        return redirect('memo_list')
    return render(request, 'work08/memo_edit.html', {'memo': memo})

def memo_delete(request, memo_id):
    memo = get_object_or_404(Memo, id=memo_id)
    memo.delete()
    return redirect('memo_list')
