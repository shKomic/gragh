import yaml
import numpy

def read_yml():
    with open('test.yaml', 'rt') as fp:
        text = fp.read()
    data = yaml.safe_load(text)
    return data

