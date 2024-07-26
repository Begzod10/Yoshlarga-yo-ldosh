from flask import Flask, render_template, request, jsonify
from backend.models.models import *
from backend.functions.infos import *

app = Flask(__name__)
app.config.from_object('backend.models.config')
db = db_setup(app)
migrate = Migrate(app, db)


@app.route('/', defaults={"test_id": 1})
@app.route('/<int:test_id>')
def index(test_id):
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
    for test_option in test_options:
        if test_info.name == 'Maqsadga intiluvchanlik':
            if 6 >= score > 0:
                option = test_option
            elif 7 <= score <= 11:
                option = test_option
            else:
                option = test_option
        elif test_info.name == 'Qat’iyatlilikni baholash testi':
            if 6 >= score > 0:
                option = test_option
            elif 7 <= score <= 11:
                option = test_option
            else:
                option = test_option
        elif test_info.name == 'Siz qanchalik sabrlisiz':
            if 4 >= score > 0:
                option = test_option
            elif 4 <= score <= 14:
                option = test_option
            else:
                option = test_option

    test = Test(test_info_id=test_info.id, answer_id=option.id, user_id=user.id)
    test.add()
    return jsonify(score=score, result=option.desc)


if __name__ == '__main__':
    app.run()
