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
                              Test.day >= ot_day, Test.day <= do_day, Test.answer_id == answer_id).order_by(
        Test.id).all()
    return jsonify({
        "msg": True,
        "tests_percentage": round((len(tests) / len(all_test) * 100)),
        "tests_num": len(tests),
        "all_test": len(all_test)
    })


@app.route('/platform')
def platform():
    all_test = Test.query.order_by(Test.id).all()
    return render_template("components/list/list.html", all_test=all_test)
