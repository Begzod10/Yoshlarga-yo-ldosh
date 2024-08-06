let test_name = document.querySelector('#test_name'), test_ball = document.querySelector('#test_ball'),
    men_check = document.querySelector('#men_check'), women_check = document.querySelector('#women_check');

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
            console.log(response)
            response['answer_list'].forEach(item => {
                test_ball.innerHTML += `<option value="${item.id}">${item.name}</option>`
            })
        })
})