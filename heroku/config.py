from os.path import abspath, dirname, join

_cwd = dirname(abspath(__file__))

SECRET_KEY = 'flask-session-insecure-secret-key'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + join(_cwd, 'flask-tracking.db')
SQLALCHEMY_ECHO = True
WTF_CSRF_SECRET_KEY = 'this-is-not-random-but-it-should-be'

#app = Flask(__name__)
#app.config.from_object(__name__)