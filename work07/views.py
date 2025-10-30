from django.shortcuts import render
import random


# トップページ
def index(request):
    return render(request, "work07/index.html")


# おみくじ
def omikuji(request):
    results = ["大吉", "中吉", "小吉", "吉", "末吉", "凶"]
    result = random.choice(results)
    return render(request, "work07/omikuji.html", {"result": result})


# じゃんけん
def janken(request):
    hands = ["グー", "チョキ", "パー"]
    user_hand = request.GET.get("hand")
    cpu_hand = random.choice(hands)

    if not user_hand:
        result = "選んでください！"
    else:
        if user_hand == cpu_hand:
            result = "あいこ"
        elif (
            (user_hand == "グー" and cpu_hand == "チョキ")
            or (user_hand == "チョキ" and cpu_hand == "パー")
            or (user_hand == "パー" and cpu_hand == "グー")
        ):
            result = "あなたの勝ち！"
        else:
            result = "あなたの負け！"

    context = {
        "user_hand": user_hand,
        "cpu_hand": cpu_hand,
        "result": result,
    }
    return render(request, "work07/janken.html", context)


# Hi & Low
def hilow(request):
    current = random.randint(1, 13)
    choice = request.GET.get("choice")
    result = None
    next_card = None

    if choice:
        next_card = random.randint(1, 13)
        if choice == "hi":
            result = "正解！" if next_card >= current else "不正解…"
        elif choice == "low":
            result = "正解！" if next_card <= current else "不正解…"

    context = {
        "current": current,
        "next": next_card,
        "result": result,
    }
    return render(request, "work07/hilow.html", context)
