from flask import *
from flask_restful import *
from feedservice.service_apis.question import Question
import django

django.setup()

app = Flask(__name__)

api = Api(app, prefix='/feedservice')
api.add_resource(Question,'/question','/question/<topic_id>')
if __name__ == '__main__':
    app.run(host='localhost',port=2010,debug=True)
