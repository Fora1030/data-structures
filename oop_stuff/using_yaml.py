import yaml

data = open('oop_stuff/using_yaml.yaml', 'r')
raw_data_schema = yaml.load(data, Loader=yaml.FullLoader)
print(raw_data_schema)