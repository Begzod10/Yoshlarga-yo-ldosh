let test_name = document.querySelector('#test_name'), test_ball = document.querySelector('#test_ball'),
    men_check = document.querySelector('#men_check input'), women_check = document.querySelector('#women_check input'),
    table_body = document.querySelector('.table_body'), filter_btn = document.querySelector('.filter_btn'),
    ot_input = document.querySelector('#ot_input'), do_input = document.querySelector('#do_input'),
    ot_date = document.querySelector('#ot_date'), do_date = document.querySelector('#do_date');


test_name.addEventListener('change', function () {
    fetch('/get_test_balls', {
        method: "POST", body: JSON.stringify({
            "test_id": test_name.value
        }), headers: {
            "Content-Type": "application/json"
        }
    })
        .then(function (response) {
            return response.json()
        })
        .then(function (response) {
            test_ball.innerHTML = ''
            test_ball.innerHTML += `<option value="">Hammasi</option>`
            response['answer_list'].forEach(item => {
                test_ball.innerHTML += `<option value="${item.id}">${item.name}</option>`
            })

        })
})
filter_btn.addEventListener('click', function () {
    let test_ball = document.querySelector('#test_ball');
    console.log(test_ball.value)
    fetch('/test_filter', {
        method: "POST", headers: {
            "Content-Type": "application/json"
        }, body: JSON.stringify({
            ot_age_input: ot_input.value,
            do_age_input: do_input.value,
            test_name: test_name.value,
            men_check: men_check.checked,
            women_check: women_check.checked,
            test_ball: test_ball.value,
            ot_date: ot_date.value,
            do_date: do_date.value
        })
    })
        .then(function (response) {
            return response.json()
        })
        .then(function (response) {
            table_body.innerHTML = ''
            response['test_info_list'].forEach((item, index) => {
                table_body.innerHTML += `<tr>
                    <td>${index + 1}</td>
                    <td>${item.age}</td>
                    <td>${item.gender}</td>
                    <td>${item.value}</td>
                    <td>${item.date}</td>
                </tr>`
            })
        })
})