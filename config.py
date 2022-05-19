from dotenv import load_dotenv
import os

load_dotenv()


class Config:
  
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:Access@localhost/tours'
    SECRET_KEY = 'twendeTOURS'
    SQLALCHEMY_TRACK_MODIFICATIONS = False




class ProdConfig(Config):
  pass




class DevConfig(Config):
  DEBUG=True



config_options = {
  'production':ProdConfig,
  'development':DevConfig
}