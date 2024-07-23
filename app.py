from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

questions = [
    "Kelajakdagi maqsadimni belgilab oldim va unga erishishga hozirlik ko'ryapman",
    "Qanchalik uzoq bo'lishidan qat'i nazar, men ko'zlangan maqsad sari intilaman",
    "Agar biror narsa uzoq muddatli maqsadni amalga oshirishga xalaqit bersa, men odatda uzoq maqsadga erishish istagini yo'qotaman",
    "Muvaffaqiyatsizliklar bo'lsa ham, men o'z maqsadimga erishisha olishimga ishonchim komil",
    "Men o'z oldimga juda uzoq maqsadlar qo'ymaslikka harakat qilaman, chunki bugungi kun bilan yashash osonroq deb o'ylayman",
    "Men bir necha bor o'zimni rivojlantirishga harakat qildim, lekin hech narsa chiqmadi",
    "Muvaffaqiyatsizliklar meni maqsadga erishish yo’lidan chetlatadi va men biron bir muhim narsaga erishish niyatidan voz kechaman.",
    "Agar men o’z oldimga o'zim uchun muhim bo'lgan maqsadni qo'ygan bo'lsam, unda meni to'xtatish qiyin.",
    "Mag'lubiyat meni yanada yangi kuch bilan harakat qilishga undaydi",
    "Men haftalikni ishlarimni rejalashtirishga ko'p marta urinib ko'rdim, lekin rejani noto’g’ri tashkil qilganim uchun hech qachon rejalashtirganimni amalga oshira olmadim.",
    "Qiyinchiliklar paydo bo'lganda, men boshlagan ishimni davom ettirishga arziydimi yoki yo'qligiga shubha qila boshlayman.",
    "Menga ko'pincha ishlarni oxirigacha bajarish qiyin, ayniqsa bunga haftalar yoki oylar kerak bo'lganda.",
    "Mening yaqinlarim meni biror narsaga qaramlikka moyil deb o'ylashadi",
    "Mavjud qiyinchiliklarga qaramay, maqsadlarimga erishganimda katta mamnuniyat his qilaman.",
    "Ko'pincha men boshlagan narsalarni yarim yo'lda tashlab qo’yaman va ularga qiziqishimni yo'qotaman.",
    "Men kutish va chidashni bilaman, shuning uchun uzoq maqsadlar meni qo'rqitmaydi.",
    "To'siqlar meni faqat harakatga undaydi va qarorlarimni kuchliroq qiladi.",
    "Muvaffaqiyatga erishishga bo’lgan shubha emas, balki dangasalik ko’pincha meni maqsadlarimga erishishdan voz kechishga majbur qiladi."
]

positive_indices = {0, 1, 3, 7, 8, 12, 13, 15, 16}
negative_indices = {2, 4, 5, 6, 9, 10, 11, 14, 17}


@app.route('/')
def index():
    return render_template('index.html', questions=questions)


@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    answers = data['answers']

    score = 0

    for i, answer in enumerate(answers):
        if answer == '+':
            if i in positive_indices:
                score += 1
        elif answer == '-':
            if i in negative_indices:
                score += 1

    if score <= 6:
        result = "Sizda maqsadga intiluvchanlikning past darajasi aniqlandi. Sizning yumshoq ko’ngilligingiz va ko’pincha boshqalarga yon berishingiz bunga sabab bo’lishi mumkin. Biroq shuni esda tutinki, qat’iyatlilik, maqsadga intiluvchanlik xislatlarini o’zingizda shakllantira olsangiz o’qishda, ishda muvaffaqiyatlarga erisha olasiz. "
    elif 7 <= score <= 11:
        result = "Sizda maqsadga intiluvchanlikning o’rta darajasi. Biroq bu sizning qo’lingizdan ko’p narsa kelmaydi degani emas. Aksincha o’qishga, ishga, maqsadingizga nisbatan me’yorda yondashish sizni boshqalardan ajratib turadi."
    else:
        result = "Sizda maqsadga intiluvchanlikning yuqori darajasi. Siz barcha boshlagan ishlaringizda oldingizga qo’ygan maqsadingizga intilishda tinimsiz mehnat qilasiz.  "

    return jsonify(score=score, result=result)


if __name__ == '__main__':
    app.run()
