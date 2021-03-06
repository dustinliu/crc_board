import os

#default setting
class default:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = True

# for local development
class dev(default):
    BASE_URL = 'http://localhost:5000'
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(default.BASE_DIR, 'crc_board.db')

# production setting
class prod(default):
    BASE_URL = "https://crc-board.herokuapp.com"
