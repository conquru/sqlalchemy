from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    # app.run()
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    # lst_names = [['Scott', 'Ridley', 21, 'captain', 'research engineer', 'module_1', 'scott_chief@mars.org'], ['a', 'aa', 13, 'office worker', 'a', 'aa', 'a@mars.org'], ['b', 'bb', 13, 'office worker', 'b', 'bb', 'b@mbrs.org'], ['c', 'cc', 13, 'office worker', 'c', 'cc', 'c@mcrs.org']]
    # for i in lst_names:
    #     user = User()
    #     user.surname = i[0]
    #     user.name = i[1]
    #     user.age = i[2]
    #     user.position = i[3]
    #     user.speciality = i[4]
    #     user.address = i[5]
    #     user.email = i[6]
    #     user.hashed_password = "cap"
    #     db_sess.add(user)
    # db_sess.commit()
    user = db_sess.query(User).filter(User.id == 1).first()
    job = Jobs(team_leader=user.id, job='deployment of residential modules 1 and 2', work_size=15, collaborators='2,3', is_finished=False)
    db_sess.add(job)
    db_sess.commit()


if __name__ == '__main__':
    main()