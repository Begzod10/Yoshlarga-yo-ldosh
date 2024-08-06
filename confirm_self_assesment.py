from app import *

questions = [
    "Men o’zimga nisbatan ishonchni his qilmayman",
    "Men tez-tez arzimas narsalardan qizarib ketaman.",
    "Mening uyqum notinch",
    "Men osongina tushkunlikka tushaman.",
    "Men faqat xayoliy muammolar haqida qayg'uraman.",
    "Qiyinchiliklar meni qo'rqitadi.",
    "Men o'z kamchiliklarimni ko'rib chiqishni yaxshi ko'raman.",
    "Meni biror narsaga ishontirish oson.",
    "Men ko’p narsadan shubhalanaman.",
    "Biror narsani kutishda qiynalaman",
    "Ko'pincha vaziyatlar men uchun umidsiz bo'lib tuyuladi garchi undan chiqish yo'lini topish hali mumkin bo’lsa ham",
    "Muammolar meni juda xafa qiladi men ruhan tushkunlikka tushaman",
    "Katta muammolar yuzaga kelganda men hech qanday sababsiz o'zimni ayblashga moyilman.",
    "Baxtsizliklar va muvaffaqiyatsizliklar menga hech narsani o'rgatmaydi.",
    "Men ko'pincha kurashishni samarasiz deb hisoblayman.",
    "Ko'pincha o'zimni himoyasiz his qilaman.",
    "Ba'zida men umidsizlikka tushib qolaman.",
    "Qiyinchiliklar oldida sarosimaga tushman.",
    "Hayotning og'ir damlarida ba'zan o'zimni bolalarcha tutaman odamlarning menga achinishlarini xohlayman.",
    "Men xarakterimdagi kamchiliklarni tuzatib bo'lmaydigan deb bilaman.",
    "Ma’lum bir vaziyatda oxirgi so’zni men aytaman (ya’ni qaror qabul qilish o’z qo’limda bo’ladi)",
    "Ko'pincha suhbatda men suhbatdoshimni gapini bo’laman",
    "Meni osongina jahlim chiqaman.",
    "Men boshqalarning kamchiliklariga izoh berishni yaxshi ko'raman.",
    "Men boshqalar uchun avtoritetda bo'lishni xohlayman.",
    "Men oz narsaga qanoat qilmayman ko'p narsani xohlayman.",
    "G‘azablansam o‘zimni boshqara olmayman.",
    "Men itoat qilishdan ko'ra rahbarlikni afzal ko'raman.",
    "Menda keskin qo'pol imo-ishoralar bor.",
    "Men qasoskorman.",
    "Menga odatlarni o'zgartirishim qiyin.",
    "Diqqatni o'zgartirish oson emas.",
    "Men hamma yangi narsalarga nisbatan juda ehtiyotkorman.",
    "Meni ishontirish qiyin.",
    "Ko'pincha men voz kechish kerak bo’lgan fikrni boshimdan chiqara olmayman.",
    "Odamlarga yaqinlashish men uchun oson emas.",
    "Rejadagi kichik buzilishlar ham meni xafa qildi.",
    "Men tez-tez qaysarlik qilaman.",
    "Men tavakkal qilishni istamayman.",
    "Men kundalik tartibdagi o’zgarishlar haqida juda ham qayg’uraman",
]


# Ballarni hisoblash
def calculate_scores(answers):
    scores = {
        "xavotirlanish": sum(answers[0:10]),
        "umidsizlik": sum(answers[10:20]),
        "agressivlik": sum(answers[20:30]),
        "qat’iyatlik": sum(answers[30:40]),
    }
    return scores


# Natijalarni talqin qilish
def interpret_scores(scores):
    interpretations = {}
    for category, score in scores.items():
        if score <= 7:
            level = "Past daraja"
        elif score <= 14:
            level = "O'rta daraja"
        else:
            level = "Yuqori daraja"
        interpretations[category] = level
    return interpretations


@app.context_processor
def utility_processor():
    return dict(enumerate=enumerate)


@app.route('/confirm_self_assesment', methods=['GET', 'POST'])
def confirm_self_assesment():
    if request.method == 'POST':
        answers = [int(request.form.get(f'question{i + 1}')) for i in range(40)]
        scores = calculate_scores(answers)
        interpretations = interpret_scores(scores)
        return render_template('confirm self-assesment/results.html', interpretations=interpretations)
    return render_template('confirm self-assesment/confirm self-assesment.html', questions=questions)
