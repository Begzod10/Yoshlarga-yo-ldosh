import datetime

from app import app, render_template, request, jsonify
from backend.models.models import Test, TestInfo, TestAnswerOptions, User, and_
from backend.functions.infos import questions_initiative, questions_purpose, questions_patience, questions_persistence, \
    test_info, questions_2, answer_options


@app.route('/test_filter', methods=['POST'])
def test_filter():
    ot = request.form.get('ot')
    do = request.form.get('do')
    ot_day = request.form.get('ot_day')
    do_day = request.form.get('do_day')
    answer_id = request.form.get('answer_id')
    ot_day = datetime.datetime.strptime(ot_day, "%Y-%m-%d")
    do_day = datetime.datetime.strptime(do_day, "%Y-%m-%d")
    test_info_get = TestInfo.query.filter(TestInfo.id == request.form['test_info_id']).first()
    users = User.query.filter(and_(User.age >= int(ot), User.age <= int(do))).all()
    all_test = Test.query.filter(Test.test_info_id == test_info_get.id).order_by(Test.id).all()
    tests = Test.query.filter(Test.test_info_id == test_info_get.id,
                              Test.user_id.in_([user_id.id for user_id in users]),
                              Test.day >= ot_day, Test.day <= do_day, Test.answer_id == answer_id).order_by(Test.id).all()
    return jsonify({
        "msg": True,
        "tests_percentage": round((len(tests) / len(all_test) * 100)),
        "tests_num": len(tests),
        "all_test": len(all_test)
    })


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
    for answer in answers:
        score += int(answer)
    test_options = TestAnswerOptions.query.filter(TestAnswerOptions.test_info_id == test_info.id).order_by(
        TestAnswerOptions.id).all()
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
    test = Test(test_info_id=test_info.id, answer_id=test_option.id, user_id=user.id)
    test.add()
    return jsonify(score=score, result=test_option.desc)
