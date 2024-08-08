import datetime
import pprint

from app import app, render_template, request, jsonify, session, extract
from backend.models.models import Test, TestInfo, TestAnswerOptions, User, and_
from backend.functions.infos import questions_initiative, questions_purpose, questions_patience, questions_persistence, \
    test_info, questions_2, answer_options


@app.route('/test_filter', methods=['POST'])
def test_filter():
    ot_age_input = request.get_json()['ot_age_input']
    do_age_input = request.get_json()['do_age_input']

    men_check = request.get_json()['men_check'] if 'men_check' in request.get_json() else False
    women_check = request.get_json()['women_check'] if 'women_check' in request.get_json() else False

    ot_date = request.get_json()['ot_date']
    do_date = request.get_json()['do_date']
    test_name = request.get_json()['test_name']
    test_ball = request.get_json()['test_ball']
    test_ball = ''
    ot_day = datetime.datetime.strptime(ot_date, "%Y-%m-%d") if ot_date else None
    do_day = datetime.datetime.strptime(do_date, "%Y-%m-%d") if do_date else None

    if men_check and not women_check:
        gender = "Erkak"
    elif women_check and not men_check:
        gender = "Ayol"
    else:
        gender = ""
    print("test_id",test_name)
    if ot_age_input and do_age_input and gender:

        users = User.query.filter(
            and_(User.age >= int(ot_age_input), User.age <= int(do_age_input), User.gender == gender)).order_by(
            User.id).all()
    elif ot_age_input and do_age_input and not gender:

        users = User.query.filter(
            and_(User.age >= int(ot_age_input), User.age <= int(do_age_input))).order_by(User.id).all()
    elif gender:
        users = User.query.filter(User.gender == gender).order_by(User.id).all()
    else:

        users = User.query.order_by(User.id).all()
    print('users', users)
    test_info_get = TestInfo.query.filter(TestInfo.id == test_name).first()

    all_test = Test.query.filter(Test.test_info_id == test_info_get.id).order_by(Test.id).all()
    by_option = False

    test_answer_option = TestAnswerOptions.query.filter(TestAnswerOptions.test_info_id == test_info_get.id,
                                                        TestAnswerOptions.id == test_ball).first() if test_ball else None
    if test_answer_option:
        by_option = True
    print('ball', test_ball)
    if ot_day and do_day and test_ball and test_info_get:
        print(1, 'work')
        if by_option:
            print(1.1)
            tests = Test.query.filter(
                Test.test_info_id == test_info_get.id,
                Test.user_id.in_([user_id.id for user_id in users]),
                Test.day >= ot_day, Test.day <= do_day,
                Test.test_answer_options_id == test_ball) \
                .order_by(Test.id).all()
        else:
            print(1.2)
            tests = Test.query.filter(Test.test_info_id == test_info_get.id,
                                      Test.day >= ot_day, Test.day <= do_day,
                                      Test.user_id.in_([user_id.id for user_id in users]),
                                      Test.value == test_ball).order_by(
                Test.id).all()
    elif ot_day and do_day and test_ball and not test_info_get:
        print(2)
        if by_option:
            tests = Test.query.filter(
                Test.user_id.in_([user_id.id for user_id in users]),
                Test.day >= ot_day, Test.day <= do_day, Test.test_answer_options_id == test_ball).order_by(
                Test.id).all()
        else:
            tests = Test.query.filter(
                Test.user_id.in_([user_id.id for user_id in users]),
                Test.day >= ot_day, Test.day <= do_day, Test.value == test_ball).order_by(
                Test.id).all()
    elif ot_day and do_day and test_info_get and not test_ball:
        print(3)
        tests = Test.query.filter(Test.test_info_id == test_info_get.id,
                                  Test.user_id.in_([user_id.id for user_id in users]),
                                  Test.day >= ot_day, Test.day <= do_day).order_by(
            Test.id).all()
    elif test_info_get and not test_ball:
        print(4)

        tests = Test.query.filter(Test.test_info_id == test_info_get.id,
                                  Test.user_id.in_([user_id.id for user_id in users]),
                                 ).order_by(
            Test.id).all()

    elif test_info_get and test_ball:
        print(5)
        if by_option:
            tests = Test.query.filter(Test.test_info_id == test_info_get.id,
                                      Test.user_id.in_([user_id.id for user_id in users]),
                                      Test.test_answer_options_id == test_ball).order_by(
                Test.id).all()
        else:
            tests = Test.query.filter(Test.test_info_id == test_info_get.id,
                                      Test.user_id.in_([user_id.id for user_id in users]),
                                      Test.value == test_ball).order_by(
                Test.id).all()
    else:
        tests = Test.query.filter(
            Test.user_id.in_([user_id.id for user_id in users]),
        ).order_by(
            Test.id).all()
    test_info_list = []
    for test in tests:
        info = {
            "id": test.id,
            "gender": test.user.gender,
            "age": test.user.age,
            "value": test.value,
            "date": test.day.strftime("%Y-%m-%d")
        }
        test_info_list.append(info)
    pprint.pprint(tests)
    return jsonify({
        "msg": True,
        "test_info_list": test_info_list,
        # "tests_percentage": round((len(tests) / len(all_test) * 100)),
        "tests_num": len(tests),
        "all_test": len(all_test)
    })


@app.route('/platform')
def platform():
    all_test = Test.query.order_by(Test.id).all()
    test_infos = TestInfo.query.order_by(TestInfo.id).all()
    test_answer_options = TestAnswerOptions.query.filter(TestAnswerOptions.test_info_id == test_infos[0].id).order_by(
        TestAnswerOptions.id).all()
    return render_template("components/platform/platform.html", all_test=all_test, test_infos=test_infos,
                           test_answer_options=test_answer_options)


@app.route('/get_test_balls', methods=['POST'])
def get_test_balls():
    test_id = request.get_json()['test_id']
    test_answers = TestAnswerOptions.query.filter(TestAnswerOptions.test_info_id == test_id).order_by(
        TestAnswerOptions.name).all()
    test_info_list = []
    tests = Test.query.filter(Test.test_info_id == test_id).order_by(Test.id).all()
    for test in tests:
        info = {
            "id": test.id,
            "gender": test.user.gender,
            "age": test.user.age,
            "value": test.value,
            "date": test.day.strftime("%Y-%m-%d")
        }
        test_info_list.append(info)
    test_answers_list = []
    if test_answers:
        for test in test_answers:
            info = {
                "id": test.id,
                "name": test.name,
                "relation": True
            }
            test_answers_list.append(info)
    else:
        test_answers = Test.query.filter(Test.test_info_id == test_id).distinct(Test.value).all()
        for test in test_answers:
            info = {
                "id": test.value,
                "name": test.value,
                "relation": False
            }
            test_answers_list.append(info)
    return jsonify({
        "answer_list": test_answers_list,
        "test_info_list": test_info_list
    })
