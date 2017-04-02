import json

class Util:
  CONFIGURATION_DIR = './config/'


  @staticmethod
  def load_application_configuration():
    return Util.load_json('application.json')

  @staticmethod
  def load_json(file):
    with open(Util.CONFIGURATION_DIR + file) as data_file:
      data = json.load(data_file)
    return data
