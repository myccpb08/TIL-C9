from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# flask
app = Flask(__name__)

#sqlalchemy 설정
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db_flask.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# sqlalchemy 초기화
db = SQLAlchemy(app)

# migrate 초기화
migrate = Migrate(app, db)


# table 만들기
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    memo = db.Column(db.Text)
    
    def __repr__(self):
        return f'<User {self.id}: {self.username}, {self.email}>'
    
# 정리
# [Create]
# INSERT INTO users (username, email) VALUES ('nwith', 'no.water@gmail.com')
# 위 SQLite 구문이 아래 3줄 문장과 같다
# user = User(username = 'nwith', email = 'no.water@gmail.com')
# db.session.add(user)
# db.session.commit()

# [Read]
# SELECT * FROM users;
# users = User.query.all() # 결과가 복수 / 여러 개가 리스트에 담겨 나온다

# SELECT * FROM users WHERE username ="nwith";
# users = User.query.filter_by(username='nwith').all()

# SELECT * FROM users WHERE username='nwith' LIMIT 1;
# user = User.query.filter_by(username='nwith').first()

# SELECT * FROM users WHERE id=2 LIMIT 1;
# user = User.query.get(2)
# primary key 만 get 으로 가져올 수 있음.

# SELECT * FROM users WHERE email LIKE '%water%';
# users = User.query.filter(User.email.like("%water%")).all()

# ORDER
# users = User.query.order_by(User.username).all()

# LIMIT
# users = User.query.limit(1).all()

# OFFSET
# users = User.query.offset(2).all()

# ORDER + LIMIT + OFFSET
# users = User.query.order_by(User.username).limit(1).offset(2).all()