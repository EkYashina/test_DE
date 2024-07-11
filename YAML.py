
import yaml

class dict_to_file():

    def __init__(self,dicts):
        self.dicts = []

    def add_content(self,dict):
        self.dicts.append(dict)
    def create_yaml(self):
        with open(r'vc.yaml', 'w') as file:
            doc = yaml.dump(self.dicts,file)

    def read_yaml(self):
        with open(r'vc.yaml') as file:
            content = yaml.load(file, Loader = yaml.FullLoader)
            print(content)


vc_2 = dict_to_file([])
vc_2.add_content([{'job': 'Tech writer', 'name': 'Ivan Katkov', 'skill': 'Normal'},{'name': 'Ivan Katkov', 'job': 'Techwriter', 'skill': 'Normal', 'employed': True}])
vc_2.create_yaml()
vc_2.read_yaml()
