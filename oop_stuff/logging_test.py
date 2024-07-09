import logging.config
import sys
import logging
import yaml
with open('oop_stuff/logging_config.yaml','r') as file:
    yaml_config = file
    config_dict = yaml.safe_load(yaml_config)
# logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
logging.config.dictConfig(config_dict)

class Test:
    def __init__(self, text, test) -> None:
        self.logger = logging.getLogger("audit.example."+__class__.__qualname__)
        self.logger.info(f"{text} this is {test}")
    
def logged(class_):
    class_.logger = logging.getLogger(class_.__qualname__)
    return class_

@logged
class Test2:
    def __init__(self, text, test) -> None:
        self.logger = logging.getLogger("audit.example."+__class__.__qualname__)
        self.logger.info(f"{text} this is {test}")
        

test = Test("Texting logging functions", "test 1")
test = Test2("Texting logging functions", "test 2")