import os
import yaml

fp_config = os.getcwd() + "/tools/upgrade.yml"


def __import_config():
    with open(fp_config) as f:
        config = yaml.safe_load(f)
    return config


config = __import_config()