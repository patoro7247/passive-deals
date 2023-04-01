from flask import Flask, request, jsonify, session
from flask_cors import CORS
from flask_login import LoginManager, UserMixin, login_user, login_required, current_user

from datetime import datetime
from flask_session.__init__ import Session
from werkzeug.security import generate_password_hash, check_password_hash
import psycopg2



app = Flask(__name__)
app.config.from_object(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.secret_key = b'6391f285a554caca6939100ee2a2d9689c3076dad72d88a415d9958bd5bb9977'



Session(app)

CORS(app)


login_manager = LoginManager()
login_manager.init_app(app)



@app.route("/")
def hello_world():
    return "<p>Sugma!</p>"

conn = psycopg2.connect(
    host="137.184.126.62",
    port=5432,
    database="dealwatcher",
    user="patoro",
    password="1234"
)
cur = conn.cursor()
cur.execute("SELECT * FROM account")
print(cur.fetchone())


class User(UserMixin):
    def __init__(self, email, password_hash):
        self.id = None
        self.email = email
        self.password_hash = password_hash

    def set_id(self, user_id):
        self.id = user_id

    def get_id(self):
        return str(self.id)

    def get_password(self):
        return self.password_hash
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@app.route("/api/register", methods=['POST'])
def register():
    
    
    session['logged_in'] = True
    data = request.get_json()
    print(data)

    userEmail = data.get('email')
    userPasswordHash = generate_password_hash(data.get('password'))

    newUser = User(email=userEmail, password_hash=userPasswordHash)
    
    cur = conn.cursor()
    cur.execute("INSERT INTO account (email, password) VALUES (%s, %s) RETURNING user_id", (userEmail, userPasswordHash))
    user_id = cur.fetchone()[0]

    newUser.set_id(user_id)


    conn.commit()
    

    #print(cur.fetchone())


    session['email'] = data.get('email')
    session['password'] = data.get('password')



    if session.get('logged_in'):
        print(session.get('email'))
        print(session.get('password'))


    else:
        print('ur not logged in')

    return jsonify({'status': 'success', 'message': 'Form submitted!'})


@app.route("/api/login", methods=['POST'])
def submit():

    
    #session['logged_in'] = True
    data = request.get_json()
    userEmail = data.get('username')
    user_password_hash = generate_password_hash(data.get('password'))


    session['username'] = data.get('username')
    session['password'] = data.get('password')

    #query db for password_hash
    cur = conn.cursor()
    cur.execute("SELECT password FROM account WHERE email = %s", (userEmail,))
    row = cur.fetchone()
    print(row[0])

    if ( check_password_hash( user_password_hash, real_password_hash) ):
        user = User


    if session.get('logged_in'):
        print(session.get('username'))
        print(session.get('password'))


    else:
        print('ur not logged in')

    return jsonify({'status': 'success', 'message': 'Form submitted!'})


@login_manager.user_loader
def load_user(user_id):
    return User.get(int(user_id))
    #returns None if ID isn't valid, after
    #which will be removed from the session



