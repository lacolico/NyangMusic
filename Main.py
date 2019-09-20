from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

# Flask 인스턴스 생성
app = Flask(__name__)
api = Api(app)

# 기능 정의
TODOS = {
    'search': {'id': 'search'},
    'download': {'id': 'download'},
    'chart': {'id': 'chart'},
}

# 예외 처리
def todoExistException(todo_id):
    sp = todo_id.split('?')
    if sp[0] not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))
    else:
        return sp

parser = reqparse.RequestParser()
parser.add_argument('id')

# 기능 리스트
# Get, POST 정의
class NyangMusic(Resource):
    def get(self):
        return TODOS

# Get, Delete, Put 정의
class NyangMusicTodo(Resource):
    def get(self, todo_id):
        sp = todoExistException(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        sp = todoExistException(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201

# URL Router에 맵핑한다.(Rest URL정의)
api.add_resource(NyangMusic, '/nyangmusic')
api.add_resource(NyangMusicTodo, '/nyangmusic/<string:todo_id>')

# 서버 실행
if __name__ == '__main__':
    app.run(debug=True)





