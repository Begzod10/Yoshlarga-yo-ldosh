from app import app, render_template, request, redirect


@app.route('/about')
def about():
    return render_template('components/about/about.html')


@app.route('/home')
def home():
    return render_template('components/home/home.html')


@app.route('/brave')
def brave():
    return render_template('components/brave/brave.html')


@app.route('/control_self')
def control_self():
    return render_template('components/controlSelf/controlSelf.html')


@app.route('/goal')
def goal():
    return render_template('components/goal/goal.html')


@app.route('/independence')
def independence():
    return render_template("components/independence/independence.html")


@app.route('/initiative')
def initiative():
    return render_template("components/Initiative/Initiative.html")


@app.route('/level')
def level():
    return render_template("components/level/htrml.html")


@app.route('/login')
def login():
    return render_template("components/login/login.html")


@app.route('/prinsipic')
def prinsipic():
    return render_template("components/prinsipic/prinsipic.html")
