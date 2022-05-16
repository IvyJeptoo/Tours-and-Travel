from dotenv import load_dotenv
import os

load_dotenv()


class Config:
  pass



class ProdConfig(Config):
  pass




class DevConfig(Config):
  DEBUG=True



config_options = {
  'production':ProdConfig,
  'development':DevConfig
}