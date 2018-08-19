from datetime import datetime

import django;

django.setup()
from feedservice.db.feed_models.models import Question as questions
from feedservice.db.feed_models.models import Topic
from flask import jsonify, request
from flask_restful import Resource

class Question(Resource):
    def get(self, topic_id=None):
        if topic_id:
            question = questions.objects.get(topic_id=topic_id)
            data = {'string': question.string, 'username': question.username, 'views': question.views}
            return jsonify({'User': data})

    def post(self):
        data=request.get_json()
        new_topic=Topic.objects.get(topic_id='Education')
        new_question=questions(topic=new_topic,string=data['string'],username=data['username'],views=data['views'])
        new_question.save()

    def put(self, token):
        pass

    def delete(self):
        pass
