from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

class UsersInfo(db.Model):
    __tablename__ = 'Users_info'

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    photo = db.Column(db.String(200), nullable=False)

@app.route('/user/<id_user>', methods=["GET"])
def get_user(id_user):
    try:
        user = session.query(UsersInfo).filter(UsersInfo.id == int(id_user)).first()

        if user:
            return jsonify({
                "id": user.id,
                "name": user.name,
                "age": user.age,
                "photo": user.photo})

        else:
            raise ValueError("500 INTERNAL SERVER ERROR")
    except Exception as e:
        return str(e), 500
    finally:
        session.close()

@app.route('/user', methods=['GET'])
def get_users():
    try:
        users = session.query(UsersInfo).all()

        if users:

            users_json = [
                {
                    "id": user.id,
                    "name": user.name,
                    "age": user.age,
                    "photo": user.photo
                }
                for user in users
            ]

            return users_json

        else:
            raise ValueError("500 INTERNAL SERVER ERROR")
    except Exception as e:
        return str(e), 500
    finally:
        session.close()


if __name__ == '__main__':
    app.run(debug=True)
