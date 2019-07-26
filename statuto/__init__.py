# -*- coding: utf-8 -*-

from backports import configparser
from bs4 import BeautifulSoup
import json
import yaml

import os

__version__ = "0.0.1"
__all__ = ['load']


class Loader(object):
    # TODO: load from other sources like, remote http, ssh, stream
    def getFileContent(self, file_path):
        content = None
        if not os.path.isfile(file_path):
            raise Exception("{} not found".format(file_path))
        with open(file_path) as _input:
            content =_input.read()
        return content


def load(file_path,type_file):
    # TODO: Make all the params and return always a dict or custum dict like object
    ConfigObj = None
    loaderObj = Loader()
    content = loaderObj.getFileContent(file_path)
    if type_file == "json":
        ConfigObj = json.loads(content)
    elif type_file == "yaml":
        ConfigObj = yaml.load(content,  Loader=yaml.FullLoader)
    elif type_file == "ini":
        ConfigObj = configparser.ConfigParser()
        ConfigObj.read(configFile)
    elif type_file == "xml":
        ConfigObj = BeautifulSoup(content,"html.parser")
    else:
        raise Exception("Not valid format")
    return ConfigObj




from backports import configparser

class Configuration:
    '''docstring for Configuration Class.

    Some description about Configuration class.'''
    DATABASE = {}
    ROUTES = {}
    MAIL = {}
    WEB = {}
  
    conf = None
    required = set(['ROUTES', 'DATABASE', 'WEB', 'TOKENS', 'TRANSLATIONS', 'SECURITY', 'CORS', 'BUCKET', 'ENCRYPTION'])
    __mappedKeys = {
        "CORS":[{
            "key":"allowed",
            "mapping": lambda _key : _key.split(",")
        }]
    }
    def __init__(self, configFile='config.ini'):
        '''Description of function __init__.

        Parameters
        ---------- 
        self : `type`
                Description of self

        Returns
        -------
        type
            Description of return type'''        
        Config = configparser.ConfigParser()
        Config.read(configFile)
        self.conf = Config
        self.__loadConfig()

    def __loadConfig(self):
        sections = list(self.required.difference(set(self.conf.sections())))
        if not sections:
            for section in self.conf.sections():
                if section in self.__mappedKeys:
                    for item in self.__mappedKeys[section]:
                        _key = item["key"]
                        if self.conf.has_option(section,_key):
                            setattr(self, section.upper(), item["mapping"](self.conf.get(section,_key)))
                    continue
                setattr(self,section,dict(self.conf.items(section)))
        else:
            raise AttributeError('Some sections are missing from config file', *sections)

