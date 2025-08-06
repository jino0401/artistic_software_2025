from flask import Flask, request, jsonify
from flask_cors import CORS
from models import db, User

app = Flask(__name__)
CORS(app)

# SQLite 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# DB 테이블 생성
with app.app_context():
    db.create_all()

# 회원가입 API
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not name or not email or not password:
        return jsonify({'error': '모든 항목을 입력하세요'}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({'error': '이미 등록된 이메일입니다'}), 409

    new_user = User(name=name, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': f'{name}님, 회원가입 완료!'}), 201


if __name__ == '__main__':

    with app.app_context():
        db.create_all()
    app.run(debug=True)
