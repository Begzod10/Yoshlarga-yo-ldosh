from app import *

questions_2 = [
    "Odatda, men barcha muhim qarorlarni tashqi yordamlarisiz qabul qilaman.",
    "Men osongina tortinchoqligimni yengib, avval notanish odam bilan suhbatni boshlay olaman.",
    "Men hech qachon o'z tashabbusim bilan jamoat topshiriqlarini o'z bo'ynimga olmayman.",
    "Akademik darslarga tayyorgarlik ko'rayotganda men ko'pincha ma'ruza yoki darslik bilan cheklanib qolmasdan qo'shimcha adabiyotlarni o'qiyman.",
    "Men uchun muhim bo'lgan insonlarning yonimda yo'qligi (uning maslahatlari, qo'llab-quvvatlashi va boshqalar) kelgusi natijalarimni sezilarli darajada kamaytiradi.",
    "Eng ko'p o'zimni ijodiy sohada sinab ko'rishni yaxshi ko'raman.",
    "Ma'lum bir faoliyat bilan shug'ullanish paytida yangi g'oyalarni o'ylab topishga harakat qilaman.",
    "Agar kimdir meni boshqarsa, o'zimni hotirjam va ishonchli his qilaman.",
    "Biror narsa qilishdan oldin, men doimo tanigan odamlari bilan maslahatlashaman.",
    "Suhbat yoki tanishuvlar paytida men tashabbusni boshqasiga berishga intilaman.",
    "Ishni aniq ma'lum bo'lgan namuna bo'yicha bajarish men uchun eng qulaydir.",
    "Odatda agar boshqalar mening rejalari va g'oyalarimni muvaffaqiyatsiz deb hisoblashsa men ulardan voz kechaman.",
    "Men ijtimoiy ishlarga norasmiy munosabatda bo'laman, uni nafaqat foydali, balki qiziqarli qilishga harakat qilaman.",
    "Har qanday ilmiy mavzuni o'rganayotganda, men test yoki imtihondan o'tish uchun talab qilinganidan ko'proq narsani bilishga intilmayman.",
    "Men odatda biror bir faoliyatning mazmuni haqida o'ylamayman, kattalar taklif qilgan narsani aniq bajaraman.",
    "Men jamoada yangi narsalarning tashkilotchisi bo'lishga intilaman.",
    "Agar men haq ekanligimga amin bo'lsam, men har doim o'zim bilgan usuldan foydalanaman.",
    "Ijodiy jarayonlar meni o'ziga jalb qilmaydi.",
    "Muvaffaqiyatdagi chiqishlarimning natijalari deyarli yaqinlarimning ishtirokiga bog'liq emas.",
    "Men har qanday ishga yangi narsa qo'shishga intilaman, aks holda meni bu ishlar qiziqtirmaydi."
]

# Answer options and their scores
answer_options = {
    "+2": "Bunday bo'lmaydi",
    "+1": "Ehtimol, bu noto'g'ri",
    "0": "Bo'lishi mumkin",
    "-1": "Ehtimol, ha",
    "-2": "Aniq ha"
}


@app.route('/test2')
def test2():
    return render_template('test2.html', questions=questions_2, answer_options=answer_options)


@app.route('/submit_test2', methods=['POST'])
def submit_test2():
    answers = request.json.get('answers', [])
    if not answers or len(answers) != len(questions_2):
        return jsonify({"error": "Barcha savollarga javob bering."}), 400

    scores = [int(answer) for answer in answers]
    total_score = sum(scores) + 20

    if total_score <= 19:
        result = "Sizda tashabbuskorlik va mustaqillikning quyi darajasi."
    elif 20 <= total_score <= 30:
        result = "Sizda tashabbuskorlik va mustaqillikning o'rtacha darajasi."
    else:
        result = "Sizda tashabbuskorlik va mustaqillikning yuqori darajasi."

    return jsonify({"total_score": total_score, "result": result})
