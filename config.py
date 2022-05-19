from dotenv import load_dotenv
import os

load_dotenv()


class Config:
  
  SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URL')
  SECRET_KEY=os.getenv('SECRET_KEY')
  SQLALCHEMY_TRACK_MODIFICATIONS=False




class ProdConfig(Config):
  pass




class DevConfig(Config):
  DEBUG=True



config_options = {
  'production':ProdConfig,
  'development':DevConfig
}