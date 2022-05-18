from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()







def create_app(config_name):


  app = Flask(__name__)


  app.config.from_object(config_options[config_name])
  
  # app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False


   #initialise extesions
  bootstrap.init_app(app)
  db.init_app(app)

  #register blueprints
  from app.main import main as main_blueprint
  app.register_blueprint(main_blueprint)

  from app.auth import auth as auth_blueprint

  app.register_blueprint(auth_blueprint)


 



  return app