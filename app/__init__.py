from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config_options
# from flask_uploads import UploadSet,configure_uploads,IMAGES

bootstrap = Bootstrap()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

db = SQLAlchemy()

def create_app(config_name):


  app = Flask(__name__)


  app.config.from_object(config_options[config_name])
  
  # app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
  app.config['SECRET_KEY']= 'twendeTOURS'


   #initialise extesions
  bootstrap.init_app(app)
  db.init_app(app)

  #register blueprints
  from app.main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  from app.auth import auth as auth_blueprint

  app.register_blueprint(auth_blueprint)


 



  return app