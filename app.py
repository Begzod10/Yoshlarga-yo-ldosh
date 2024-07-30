from flask import Flask, render_template, request, jsonify

from backend.functions.infos import *
from backend.functions.infos2 import *
from backend.models.models import *

app = Flask(__name__)
app.config.from_object('backend.models.config')
db = db_setup(app)
migrate = Migrate(app, db)


@app.route('/', defaults={"test_id": 0})
@app.route('/<int:test_id>')
def index(test_id):
    if test_id == 0:
        test_id = TestInfo.query.order_by(TestInfo.id).first().id
    for info in test_info:
        test_info_add = TestInfo.query.filter(TestInfo.name == info['name']).first()
        if not test_info_add:
            test_info_add = TestInfo(name=info['name'], desc=info['desc'])
            test_info_add.add()
        for test_options in info['variants']:
            if isinstance(test_options['name'], str):
                for test_options1 in test_options['variants']:
                    test_options_add1 = TestAnswerOptions.query.filter(TestAnswerOptions.desc == test_options1['desc'],
                                                                       TestAnswerOptions.test_info_id == test_info_add.id).first()
                    if not test_options_add1:
                        test_options_add1 = TestAnswerOptions(name=test_options1['name'], test_info_id=test_info_add.id,
                                                              desc=test_options1['desc'])
                    test_options_add1.add()

            else:
                test_options_add = TestAnswerOptions.query.filter(TestAnswerOptions.name == test_options['name'],
                                                                  TestAnswerOptions.test_info_id == test_info_add.id).first()
                if not test_options_add:
                    test_options_add = TestAnswerOptions(name=test_options['name'], test_info_id=test_info_add.id,
                                                         desc=test_options['desc'])

                test_options_add.add()
    test = TestInfo.query.filter(TestInfo.id == test_id).first()
    if test.name == 'Maqsadga intiluvchanlik':
        questions = questions_purpose
    elif test.name == 'Qat’iyatlilikni baholash testi':
        questions = questions_persistence
    elif test.name == 'Siz qanchalik sabrlisiz':
        questions = questions_patience
    elif test.name == 'Siz qanchalik tashabbuskor va mustaqilsiz':
        questions = questions_initiative
    elif test.name == 'SHAXS EMOTSIONAL INTELLEKTINING SIFATLARINING PSIXOLOGIK TASHXISI':
        questions = questions_emotion
    else:
        questions = []
    return render_template('index.html', questions=questions, selected_test=test,
                           tests=[{'id': test.id, 'name': test.name} for test in
                                  TestInfo.query.order_by(TestInfo.id).all()]
                           )


@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    answers = data['answers']
    age = data['age']
    gender = data['gender']
    test = data['test']
    test_info = TestInfo.query.filter(TestInfo.id == test).first()
    user = User(age=age, gender=gender)
    user.add()
    score = 0
    question_count = 0
    for answer in answers:
        question_count += 1
        score += int(answer)

    test_option = None

    if test_info.name == 'Maqsadga intiluvchanlik':
        if 6 >= score > 0:
            test_option = TestAnswerOptions.query.filter(
                and_(TestAnswerOptions.name <= 6, TestAnswerOptions.name > 0),
                TestAnswerOptions.test_info_id == test_info.id).first()
        elif 7 <= score <= 11:
            test_option = TestAnswerOptions.query.filter(
                and_(TestAnswerOptions.name <= 11, TestAnswerOptions.name > 7),
                TestAnswerOptions.test_info_id == test_info.id).first()
        elif 11 <= score <= 18:
            test_option = TestAnswerOptions.query.filter(
                and_(TestAnswerOptions.name <= 18, TestAnswerOptions.name > 11),
                TestAnswerOptions.test_info_id == test_info.id).first()
    elif test_info.name == 'Qat’iyatlilikni baholash testi':
        if 6 >= score > 0:
            test_option = TestAnswerOptions.query.filter(
                and_(TestAnswerOptions.name <= 6, TestAnswerOptions.name > 0),
                TestAnswerOptions.test_info_id == test_info.id).first()
        elif 7 <= score <= 11:
            test_option = TestAnswerOptions.query.filter(
                and_(TestAnswerOptions.name <= 11, TestAnswerOptions.name > 7),
                TestAnswerOptions.test_info_id == test_info.id).first()
        elif 11 <= score <= 18:
            test_option = TestAnswerOptions.query.filter(
                and_(TestAnswerOptions.name <= 18, TestAnswerOptions.name > 11),
                TestAnswerOptions.test_info_id == test_info.id).first()
    elif test_info.name == 'Siz qanchalik sabrlisiz':
        if 4 >= score > 0:
            test_option = TestAnswerOptions.query.filter(
                and_(TestAnswerOptions.name <= 4, TestAnswerOptions.name > 0),
                TestAnswerOptions.test_info_id == test_info.id).first()
        elif 4 <= score <= 14:
            test_option = TestAnswerOptions.query.filter(
                and_(TestAnswerOptions.name <= 14, TestAnswerOptions.name > 4),
                TestAnswerOptions.test_info_id == test_info.id).first()
        elif 14 <= score <= 18:
            test_option = TestAnswerOptions.query.filter(
                and_(TestAnswerOptions.name <= 18, TestAnswerOptions.name > 14),
                TestAnswerOptions.test_info_id == test_info.id).first()
    elif test_info.name == 'Siz qanchalik tashabbuskor va mustaqilsiz':
        score += 20
        if 19 >= score > 0:
            test_option = TestAnswerOptions.query.filter(
                and_(TestAnswerOptions.name <= 19, TestAnswerOptions.name > 0),
                TestAnswerOptions.test_info_id == test_info.id).first()
        elif 19 <= score <= 30:
            test_option = TestAnswerOptions.query.filter(
                and_(TestAnswerOptions.name <= 30, TestAnswerOptions.name > 19),
                TestAnswerOptions.test_info_id == test_info.id).first()
        elif 30 <= score:
            test_option = TestAnswerOptions.query.filter(
                and_(TestAnswerOptions.name > 30),
                TestAnswerOptions.test_info_id == test_info.id).first()

    def get_test_option(score, desc, test_info_id):
        return TestAnswerOptions.query.filter(
            and_(
                TestAnswerOptions.test_info_id == test_info_id,
                TestAnswerOptions.desc == desc
            )
        ).first()

    def calculate_score(answers, start_index, end_index):
        return sum(int(answer) for answer in answers[start_index:end_index])

    results = []
    if test_info.name == 'SHAXS EMOTSIONAL INTELLEKTINING SIFATLARINING PSIXOLOGIK TASHXISI':

        for i in range(0, len(answers), 10):
            segment_score = calculate_score(answers, i, i + 10)


            desc = ""

            if i == 0:
                if 1 <= segment_score <= 7:
                    desc = "Sizda xavotirlanish darajasi past chiqdi. Xavotirlilik past bo’lganda siz oldinga dadil qadam tashlay olasiz va qiyinchiliklardan qo’rqmaysiz. Omadsizlikka duch kelishingiz mumkinligidan xavotirga tushmaysiz;"
                elif 8 <= segment_score <= 14:
                    desc = "Sizda xavotirlanishning o’rta darajasi aniqlandi. Siz ba’zan biror bir faoliyatni amalga oshirayotganda uning yakuni haqida xavotirga tushasiz. Bu esa sizning faoliyatingiz unumdorligini pasayishiga olib kelishi mumkin;"
                elif 15 <= segment_score <= 20:
                    desc = "Sizda xavotirlanishning yuqori darajasi mavjud. Xavotirlik darajasi yuqori bo’lsa, sizning shaxsiy va mehnat faoliyatingizda bir qancha qiyinchiliklar yuzaga kelishi mumkin. Doimiy xavotir ostida yashash esa doimiy stressga, shaxslararo munosabatlarning buzilishiga olib kelishi mumkin."
                test_option = get_test_option(test_info_id=test_info.id, score=segment_score, desc=desc)
                if test_option:
                    results.append(test_option.desc)


            elif i == 10:
                if 1 <= segment_score <= 7:
                    desc = "Sizda xavotirlanishning yuqori darajasi mavjud. Xavotirlik darajasi yuqori bo’lsa, sizning shaxsiy va mehnat faoliyatingizda bir qancha qiyinchiliklar yuzaga kelishi mumkin. Doimiy xavotir ostida yashash esa doimiy stressga, shaxslararo munosabatlarning buzilishiga olib kelishi mumkin."
                elif 8 <= segment_score <= 14:
                    desc = "Sizda umidsizlikning o’rta darajasi aniqlandi. Siz biror bir faoliyatni amalga oshirayotganda uning yakuni siz kutgan natijani bermasligi mumkinligidan ba’zan umidsizlikka tushasiz. Bu esa o’z o’zidan xavotirlik, tashvish hissini yuzaga keltirishi mumkin."
                elif 15 <= segment_score <= 20:
                    desc = "Sizda umidsizlikning yuqori darajasi mavjud. Umidsizlik darajasi yuqori bo’lsa, siz o'zingizni past baholaysiz, qiyinchiliklardan qochasiz, muvaffaqiyatsizliklardan qo'rqasiz va umidsizlikka tushasiz."
                test_option = get_test_option(test_info_id=test_info.id, score=segment_score, desc=desc)
                if test_option:
                    results.append(test_option.desc)

            elif i == 20:
                if 1 <= segment_score <= 7:
                    desc = "Sizda agressiyaning darajasi past ekanligi aniqlandi. Agar agressiya (tajavuzkorlik) darajasi past bo’lsa siz insonlar bilan muloqotga kirishishda, o’zingizni boshqarishda hech qanday qiyinchiliklarga duch kelmaysiz."
                elif 8 <= segment_score <= 14:
                    desc = "Sizda agressiyaning o’rta darajasi aniqlandi. Siz ba’zan biror bir faoliyatni amalga oshirayotganda, odamlar bilan muloqotga kirishayotganda qiyinchiliklarga duch kelasiz. Arzimasa-dek tuyilgan narsalarga tez asabiylashasiz. Bu esa sizning faoliyatingizni bir me’yorda kechishiga xalaqit berishi mumkin."
                elif 15 <= segment_score <= 20:
                    desc = "Sizda agressiyaning yuqori darajasi mavjud. Agressiya darajasi yuqori bo’lsa, siz atrofingizdagilar bilan doimiy nizolashasiz, o’z hissiyotlaringizni boshqarishga qiynalasiz. Bu esa o’zidan atrofdagilan bilan munosabatlaringizni yomonlashishiga olib keladi. Ushbu holatdan chiqish uchun o’z hissiyotlaringizni, g’azabingizni boshqarishga harakat qiling."
                test_option = get_test_option(test_info_id=test_info.id, score=segment_score, desc=desc)
                if test_option:
                    results.append(test_option.desc)
            elif i == 30:
                if 1 <= segment_score <= 7:
                    desc = "Sizda qat’iyatlilikning darajasi past. Agar qat’iyatlilik darajasi past bo’lsa siz o’z oldingizga qo’ygan maqsadlaringiz, rejalaringizga erishishda qiynalishingiz mumkin."
                elif 8 <= segment_score <= 14:
                    desc = "Sizda qat’iyatlilikning o’rta darajasi aniqlandi. Siz ba’zan biror bir faoliyatni amalga oshirayotganda, ko’plab ikkilanishlarga, qo’rquvlarga duch kelasiz. Bularning barchasi sizda qilayotgan ishingizga nisbatan qat’iyat bilan yondasholmasligingiz sabab. Agar o’z qat’iyatliligingiz ustida ishlasangiz bunday muammolarga yechim topgan bo’lasiz."
                elif 15 <= segment_score <= 20:
                    desc = "Sizda qat’iyatlilikning yuqori darajasi mavjud. Qat’iyatlilik darajasi yuqori bo’lsa, siz barcha maqsadlaringiz, o’z qarorlaringizni amalga oshirishda qiyinchiliklarga duch kelish ehtimoli keskin past bo’ladi. Bu esa sizni muvaffaqiyatga erishishingizga zamin yaratadi."
                test_option = get_test_option(test_info_id=test_info.id, score=segment_score, desc=desc)
                if test_option:
                    results.append(test_option.desc)
        return jsonify(score=score, results=results)


if __name__ == '__main__':
    app.run()
