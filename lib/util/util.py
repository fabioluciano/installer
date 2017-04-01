import json

class Util:
  CONFIGURATION_DIR = '../config/'

  def load_json(self, file):
    with open(self.CONFIGURATION_DIR + file) as data_file:
      data = json.load(data_file)
    return data
