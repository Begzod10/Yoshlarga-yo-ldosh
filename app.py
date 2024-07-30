from flask import Flask, render_template, request, jsonify
from backend.models.models import *
from backend.functions.infos import *

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
    elif test.name == 'Oʻquv faoliyat motivi':
        questions = questions_educational_activity
    elif test.name == 'Oiladagi psixologik iqlim':
        questions = questions_family
    elif test.name == "IPM / ijtimoiy – psixologik maslashganlik / so‘rovnomasi":
        questions = questions_IPM
    else:
        questions = []
    return render_template('index.html', questions=questions, selected_test=test,
                           tests=[{'id': test.id, 'name': test.name} for test in
                                  TestInfo.query.order_by(TestInfo.id).all()]
                           )


def calculate_section_scores(questions, sections):
    section_scores = {section: 0 for section in sections}
    for q in questions:
        question_number = int(q['question'])
        value = int(q['value'])
        for section, numbers in sections.items():
            if question_number in numbers:
                section_scores[section] += value
    return section_scores


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
    for answer in answers:
        score += int(answer['value'])
    results = []
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
        test = Test(test_info_id=test_info.id, answer=test_option.desc, user_id=user.id)
        test.add()
        results.append(test_option.desc)
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
        test = Test(test_info_id=test_info.id, answer=test_option.desc, user_id=user.id)
        test.add()
        results.append(test_option.desc)
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
        test = Test(test_info_id=test_info.id, answer=test_option.desc, user_id=user.id)
        test.add()
        results.append(test_option.desc)
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
        test = Test(test_info_id=test_info.id, answer=test_option.desc, user_id=user.id)
        test.add()
        results.append(test_option.desc)
    elif test_info.name == 'Oʻquv faoliyat motivi':
        if 10 >= score > 0:
            test_option = TestAnswerOptions.query.filter(
                and_(TestAnswerOptions.name <= 10, TestAnswerOptions.name > 0),
                TestAnswerOptions.test_info_id == test_info.id).first()
        elif 10 <= score <= 20:
            test_option = TestAnswerOptions.query.filter(
                and_(TestAnswerOptions.name <= 20, TestAnswerOptions.name > 10),
                TestAnswerOptions.test_info_id == test_info.id).first()
        test = Test(test_info_id=test_info.id, answer=test_option.desc, user_id=user.id)
        test.add()
        results.append(test_option.desc)
    elif test_info.name == 'Oiladagi psixologik iqlim':
        if 8 >= score > 0:
            test_option = TestAnswerOptions.query.filter(
                and_(TestAnswerOptions.name <= 8, TestAnswerOptions.name > 0),
                TestAnswerOptions.test_info_id == test_info.id).first()
        elif 8 <= score <= 15:
            test_option = TestAnswerOptions.query.filter(
                and_(TestAnswerOptions.name <= 15, TestAnswerOptions.name > 8),
                TestAnswerOptions.test_info_id == test_info.id).first()
        elif 15 <= score <= 22:
            test_option = TestAnswerOptions.query.filter(
                and_(TestAnswerOptions.name <= 22, TestAnswerOptions.name > 15),
                TestAnswerOptions.test_info_id == test_info.id).first()
        elif 22 <= score <= 35:
            test_option = TestAnswerOptions.query.filter(
                and_(TestAnswerOptions.name <= 35, TestAnswerOptions.name > 22),
                TestAnswerOptions.test_info_id == test_info.id).first()
        test = Test(test_info_id=test_info.id, answer=test_option.desc, user_id=user.id)
        test.add()
        results.append(test_option.desc)
    elif test_info.name == "IPM / ijtimoiy – psixologik maslashganlik / so‘rovnomasi":
        sections = {
            'Moslashganlik': [4, 5, 9, 12, 15, 19, 22, 23, 26, 27, 29, 33, 35, 37, 41, 44, 47, 51, 53, 55, 61, 63, 67,
                              72, 74, 75, 78, 80, 88, 91, 94, 96, 97, 98],
            'Moslashmaganlik': [2, 6, 8, 13, 16, 18, 25, 28, 32, 36, 38, 40, 42, 43, 49, 50, 54, 56, 59, 60, 62, 64, 69,
                                71, 73, 76, 77, 83, 84, 86, 90, 95, 99, 100],
            'O‘z-o‘zini qabul qilish': [33, 35, 55, 67, 72, 74, 75, 80, 88, 94, 96],
            'O‘z-o‘zini qabul qilmaslik': [7, 59, 62, 65, 90, 95, 99],
            'Boshqalarni qabul qilish': [9, 14, 22, 26, 53, 97],
            'Boshqalarni qabul qilmaslik': [2, 10, 21, 28, 40, 60, 76],
            'Hissiy qulaylik': [23, 29, 30, 41, 44, 47, 78],
            'Hissiy noqulaylik': [6, 42, 43, 49, 50, 83, 85],
            'Ichki nazorat': [4, 5, 11, 12, 19, 29, 37, 51, 63, 68, 79, 91, 98],
            'Tashqi nazorat': [13, 25, 36, 52, 57, 70, 71, 73, 77],
            'Ustuvorlik': [58, 61, 66],
            'Ergashuvchanlik': [16, 32, 38, 69, 84, 87],
            'Eskalizm': [17, 18, 54, 64, 86]
        }
        scores = calculate_section_scores(answers, sections)
        if 0 < scores['Moslashganlik'] <= 170:
            pass
    return jsonify(score=score, results=results)


if __name__ == '__main__':
    app.run()
