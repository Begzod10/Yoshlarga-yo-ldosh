from flask import Flask, render_template, request, jsonify
from backend.models.models import *

app = Flask(__name__)
app.config.from_object('backend.models.config')
db = db_setup(app)
migrate = Migrate(app, db)


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
    test_info = [
        {
            "name": "Maqsadga intiluvchanlik",
            "variants": [
                {
                    "name": 6,
                    "desc": "6 ballgacha – sizda maqsadga intiluvchanlikning past darajasi aniqlandi. Sizning yumshoq ko’ngilligingiz va ko’pincha boshqalarga yon berishingiz bunga sabab bo’lishi mumkin. Biroq shuni esda tutinki, qat’iyatlilik, maqsadga intiluvchanlik xislatlarini o’zingizda shakllantira olsangiz o’qishda, ishda muvaffaqiyatlarga erisha olasiz."
                },
                {
                    "name": 7,
                    "desc": "7-11 ballgacha – Sizda maqsadga intiluvchanlikning o’rta darajasi. Biroq bu sizning qo’lingizdan ko’p narsa kelmaydi degani emas. Aksincha o’qishga, ishga, maqsadingizga nisbatan me’yorda yondashish sizni boshqalardan ajratib turadi."
                },
                {
                    "name": 12,
                    "desc": "Sizda maqsadga intiluvchanlikning yuqori darajasi. Siz barcha boshlagan ishlaringizda oldingizga qo’ygan maqsadingizga intilishda tinimsiz mehnat qilasiz."
                },
            ],
            "desc": "Ushbu metodika  E. P. Ilin va E. K. Feshchenko tomonidan ishlab chiqilgan. Ko'rsatmalar: Sizga bir nechta savollar taqdim etiladi. Ushbu vaziyatlarga o'zingizni qo’yib ko’ring  va ular siz uchun qanchalik mos ekanligini baholang. Agar siz ushbu fikrga rozi bo'lsangiz, '+' belgisini qo'ying, agar rozi bo'lmasangiz, '-' belgisini qo'ying."
        },
        {
            "name": "Siz qanchalik sabrlisiz",
            "desc": "",
            "variants": [
                {
                    "name": 4,
                    "desc": "Siz qatyatlisiz va o'jarsiz. Qaerda bo'lishingizdan  qat'iy nazar, siz fikringizni boshqalarga yuklamoqchi bo'lgandek ta'ssurot qoldirishingiz mumkin, ko'pincha ikkilanmasdan, maqsadingizga yordam berish uchun siz tez-tez ovozingizni ko'tarasiz. Sizning xarakteringiz sizdan boshqacha fikrlaydigan va siz aytayotgan va qiladigan ishlaringizga rozi bo'lmagan odamlar bilan normal munosabatlarni saqlashni qiyinlashtirish."
                },
                {
                    "name": 14,
                    "desc": "Siz o'z fikringizni qat'iy himoya qilishga qodirsiz. Lekin, albatta, siz ham muloqot jarayonida agar kerak bo'lsa, fikringizni o'zgartirishingiz mumkin. Sizda ba'zan haddan tashqari keskinlik, suxbatdoshga hurmatsizlik ko'rsatishingiz ham mumkin. Va bunday payda siz xaqiqatan ham zaifroq xarakterga ega bo'lgan odam bilan baxsda g'alaba qozonishingiz mumkin."
                },
                {
                    "name": 18,
                    "desc": "Sizning etiqodlaringizning qat'ijligi ajoyib noziklik, ongingizning qobiliyatiga bilan mukammal birlashtirilgan. Siz har qanday g'oyalarni qabul qilish va qarashda, birinchi ishni boshlashingiz mumkin. Siz notug'ri bo'lgan fikrlarni hurmat va hushmuomalalik bilan rad eta olasiz."
                }
            ]
        }
    ]
    for info in test_info:
        test_info_add = TestInfo.query.filter(TestInfo.name == info['name']).first()
        if not test_info_add:
            test_info_add = TestInfo(name=info['name'], desc=info['desc'])
            test_info_add.add()
        for test_options in info['variants']:
            test_options_add = TestAnswerOptions.query.filter(TestAnswerOptions.name == test_options['name'],
                                                              TestAnswerOptions.test_info_id == test_info_add.id).first()
            if not test_options_add:
                test_options_add = TestAnswerOptions(name=test_options['name'], test_info_id=test_info_add.id,
                                                     desc=test_options['desc'])
                test_options_add.add()
    return render_template('index.html', questions=questions)


@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    answers = data['answers']
    age = data['age']
    gender = data['gender']
    test_info = TestInfo.query.filter(TestInfo.name == "Maqsadga intiluvchanlik").first()

    # txt = "h3110 23 cat 444.4 rabbit 11 2 dog"
    # [int(s) for s in txt.split() if s.isdigit()]
    user = User(age=age, gender=gender)
    user.add()
    score = 0
    for i, answer in enumerate(answers):
        if answer == '+':
            if i in positive_indices:
                score += 1
        elif answer == '-':
            if i in negative_indices:
                score += 1

    if 6 >= score > 0:
        test_options = TestAnswerOptions.query.filter(
            and_(TestAnswerOptions.name <= 6, TestAnswerOptions.name > 0),
            TestAnswerOptions.test_info_id == test_info.id).first()
        result = "Sizda maqsadga intiluvchanlikning past darajasi aniqlandi. Sizning yumshoq ko’ngilligingiz va ko’pincha boshqalarga yon berishingiz bunga sabab bo’lishi mumkin. Biroq shuni esda tutinki, qat’iyatlilik, maqsadga intiluvchanlik xislatlarini o’zingizda shakllantira olsangiz o’qishda, ishda muvaffaqiyatlarga erisha olasiz. "
    elif 7 <= score <= 11:
        test_options = TestAnswerOptions.query.filter(
            and_(TestAnswerOptions.name <= 11, TestAnswerOptions.name > 6),
            TestAnswerOptions.test_info_id == test_info.id).first()
        result = "Sizda maqsadga intiluvchanlikning o’rta darajasi. Biroq bu sizning qo’lingizdan ko’p narsa kelmaydi degani emas. Aksincha o’qishga, ishga, maqsadingizga nisbatan me’yorda yondashish sizni boshqalardan ajratib turadi."
    else:
        test_options = TestAnswerOptions.query.filter(
            TestAnswerOptions.name >= 12, TestAnswerOptions.test_info_id == test_info.id).first()
        result = "Sizda maqsadga intiluvchanlikning yuqori darajasi. Siz barcha boshlagan ishlaringizda oldingizga qo’ygan maqsadingizga intilishda tinimsiz mehnat qilasiz.  "
    test = Test(test_info_id=test_info.id, answer_id=test_options.id, user_id=user.id)
    test.add()
    return jsonify(score=score, result=result)


if __name__ == '__main__':
    app.run()
