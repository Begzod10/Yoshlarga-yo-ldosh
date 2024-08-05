from flask import Flask, jsonify, request, render_template
from backend.models.models import TestInfo, TestAnswerOptions, Test, desc, db_setup, and_, User
from backend.functions.infos import *
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('backend.models.config')
db = db_setup(app)
migrate = Migrate(app, db)





from backend.test_functions.test2 import *

if __name__ == '__main__':
    app.run()
