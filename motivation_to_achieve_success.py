from app import *

questions = [
    "Ikkita ishdan birini zudlik bilan bajarish yoki ularni tanlash kerak boʻlsa yaxshisi tezda unga kirishib bajarib qoʻya qolgan afzal.",
    "Berilgan topshiriqni  100% yaxshi bajara olmayotganligimni  sezsam juda qaygʻuraman.",
    "Ishlayotgan vaqtimda shunday berilib ketamanki goʻyoki hamma narsa shunga bogʻliqday.",
    "Muammoli vaziyat paydo boʻlganda men qaror chiqarishga shoshilmayman.",
    "Ikki kun surunkali ishsiz qolsam halovatimni yoʻqotaman.",
    "Baʼzi kunlari mening muvaffaqiyatlarim oʻrtachadan past boʻladi.",
    "Men oʻzimga boshqalarga qaraganda ancha talabchanman.",
    "Men boshqalardan koʻra saxovatli mehribonroq odamman.",
    "Qiyin topshiriqni bajarishdan bosh tortgan  paytlarimda odatda men oʻzimni koyiyman chunki bilaman oʻzim agar oʻsha ishga kirishganimda bajargan boʻlardim.",
    "Ishlash davomida men tez-tez dam olib turishga ehtiyoj sezaman.",
    "Tirishqoqlik va tinmaslik — mendagi asosiy sifat emas.",
    "Mening mehnatdagi yutuqlarim doim xam bir xil emas.",
    "Men bevosita oʻzim bajarayotgan ish emas balki boshqa ishlar koʻproq yoqadi.",
    "Maqtovdan koʻra tanqid meni koʻproq ishlashga majbur qiladi.",
    "Meni hamkasblarim ishchan deb hisoblashlarini yaxshi bilaman.",
    "Ishdagi qiyinchiliklar mening qarorlarimni yanada qatiylashtiradi.",
    "Mening nafsoniyatimga tegish juda ham oson.",
    "Boshqalar mening ilhomsiz tashabbussiz ishlayotganimni sezishadi.",
    "Biror ishni bajarayotganimda men boshqalarning koʻmagiga tayanmayman.",
    "Men baʼzan hozir qilishim mumkin boʻlgan ishni keyinga qoldiraman.",
    "Odam faqat oʻziga ishonishi kerak.",
    "Hayotda puldan ham muhim boʻlgan narsa deyarli yoʻq.",
    "Muhim biror topshiriqni bajarish kerak boʻlganda men doimo boshqa barcha tashvishlarni unutaman.",
    "Men koʻpchilikka qaraganda unchalik izzattalab emasman.",
    "Taʼtil oxirida men odatda yaqinda ishga chiqishimni oʻylab quvonaman.",
    "Menga ish yoqsa uni men boshqalarga nisbatan malakaliroq bajaraman.",
    "Men ishga kirishib ketadigan insonlar bilan til topishim osonroq boʻladi.",
    "Ishim yoʻq paytlarda men oʻzimni behalovat his qilaman.",
    "Men  boshqalarga  nisbatan  masʼuliyatli  ishlarni  tez-tez  bajarishga toʻgʻri keladi.",
    "Qaror chiqarish masʼuliyati menga yuklansa yaxshiroq bajarishga intilaman.",
    "Mening doʻstlarim meni baʼzan dangasa deb hisoblashadi.",
    "Maʼlum maʼnoda mening yutuqlarimda hamkasablarimning ulushi bor.",
    "Rahbarning fikrini qaytarishdan foyda yoʻq.",
    "Baʼzan qanday ish bajarish kerakligini ham bilmaysan.",
    "Ishim yurishmay qolgan paytlarimda men betoqat boʻlib bezovtalanaman.",
    "Men odatda oʻz yutuqlarimga kam eʼtibor beraman.",
    "Boshqalar bilan ishlayotgan paytlarimda mening yutuqlarim boshqalarnikidan koʻproq va sezilarliroq boʻladi.",
    "Oʻz boʻynimga olgan koʻpgina ishlarni men oxiriga yetkaza olmayman.",
    "Men ishi juda koʻp boʻlmagan odamlarga havas qilaman.",
    "Men hokimiyatga intilgan va amalparastlarga havas qilmayman.",
    "Men oʻz yoʻlimning toʻgʻriligiga shubha qilmasam uni amalga oshirish yoʻlida hech narsadan toymayman."
]

answers = {
    "yes": [2, 3, 4, 5, 7, 8, 9, 10, 14, 15, 16, 17, 21, 22, 25, 26, 27, 28, 29, 30, 32, 37, 41],
    "no": [6, 13, 18, 20, 24, 31, 36, 38, 39]
}


def calculate_score(responses):
    score = 0
    for i, response in enumerate(responses, start=1):
        if (response == "yes" and i in answers["yes"]) or (response == "no" and i in answers["no"]):
            score += 1
    return score


@app.route("/motivation_to_achieve_success", methods=["GET", "POST"])
def motivation_to_achieve_success():
    if request.method == "POST":
        responses = [request.form.get(f"q{i}") for i in range(1, len(questions) + 1)]
        score = calculate_score(responses)
        return render_template("motivation_to_achieve_success/result.html", score=score)
    return render_template("motivation_to_achieve_success/index.html", questions=questions)
