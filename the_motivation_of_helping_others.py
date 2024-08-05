from app import *

questions = [
    "Men boshqa odamlarga hamdard bo'lishga tayyorman.",
    "Boshqalarga kerak bo'lsa ham hozir tashvishlarimdan dam olishim qiyin.",
    "Men boshqalarga yordam bera olishimni his qilaman.",
    "Endi birovning omadini baham ko'ra olmayman.",
    "Agar boshqa odamni unchalik yoqtirmasam, unga yordam berish men uchun qiyin.",
    "Yo'qotilganlar doimo yordam so'rashsa, g'azablanmaslik qiyin.",
    "Yangi narsa yaratish shart emas, eng muhimi odamlar bilan yaxshi munosabatda bo'lishdir.",
    "Odamlar meni bezovta qiladilar.",
    "Men hayotimdagi eng yaxshi narsalarni odamlar bilan baham ko'rmoqchiman.",
    "Ko'p odamlar mening yordamimga muhtojligini his qilaman.",
    "Men uchun har qanday odamda hamdardlik uyg'otadigan xususiyatlarni topish oson.",
    "Hayotda ko'pincha muhtojlarga yordam berishdan bosh tortishdan qo'rqmaslik kerak bo'lgan paytlar bo'ladi."
]


@app.route('/the_motivation_of_helping_others')
def the_motivation_of_helping_others():
    return render_template('the_motivation_of_helping_others_submit/index.html', questions=questions)


@app.route('/the_motivation_of_helping_others_submit', methods=['POST'])
def the_motivation_of_helping_others_submit():
    scores = {
        "Ha bu to'g'ri": 6,
        "Balki shundaydir": 5,
        "Bu to'g'ri yolg'on emas": 4,
        "Aniq javob berish qiyin": 3,
        "Bu haqiqatdan ko'ra noto'g'riroq": 2,
        "Balki unday emasdir": 1,
        "Yo'q unday emas": 0
    }
    total_score = 0
    for i in range(len(questions)):
        answer = request.form.get(f'question_{i}')
        total_score += scores[answer]

    if total_score > 45:
        result = "Yuqori ball (45 dan yuqori) sizni sezgir hamdard odam sifatida tavsiflaydi."
    elif total_score >= 30:
        result = "O'rtacha ball (30 dan 45 gacha) sizni befarq odam sifatida tavsiflaydi."
    else:
        result = "Past ball (30 dan kam) sizni yordam berishdan qochadigan odam sifatida tavsiflaydi."

    return render_template('the_motivation_of_helping_others_submit/result.html', score=total_score, result=result)
