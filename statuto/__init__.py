# -*- coding: utf-8 -*-

from backports import configparser
# from bs4 import BeautifulSoup
import xmltodict
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

class Config(object):

    def __init__(self):
        pass

class Configurator(object):
    required = set()
    def __init__(self, configFile, _format, required=[], keysMapping={}):
        self.configFile = configFile
        self.format = _format
        self.configObj = None
        self.loaderObj = Loader()
        self.required = set(required)
        self.__mappedKeys = keysMapping

    def getConfigDict(self):
        if self.format == "json":
            self.configObj = self.__parseJson()
        elif self.format == "yaml":
            self.configObj = self.__parseYaml()
        elif self.format == "ini":
            self.configObj = self.__parseIni()
        elif self.format == "xml":
            self.configObj = self.__parseXml()
        else:
            raise Exception("Not valid format")
        return self.configObj

    def getConfigObj(self):
        configObj = Config()
        self.getConfigDict()
        for k,v in self.configObj.items():
            setattr(configObj,k,v)
        return configObj

    def __parseIni(self):
        conf = configparser.ConfigParser()
        conf.read(self.configFile)
        return self.__processIni(conf)

    def __parseJson(self):
        content = self.loaderObj.getFileContent(self.configFile)
        conf = json.loads(content)
        return conf

    def __parseXml(self):
        content = self.loaderObj.getFileContent(self.configFile)
        conf = xmltodict.parse(content)
        return conf

    def __parseYaml(self):
        content = self.loaderObj.getFileContent(self.configFile)
        conf = yaml.load(content,  Loader=yaml.FullLoader)
        return conf

    def __processIni(self, conf):
        result = {}
        validating_sections = list(self.required.difference(set(conf.sections())))
        if not validating_sections:
            for section in conf.sections():
                # print "Section : ",section
                result[section] = dict(conf.items(section))
                if section in self.__mappedKeys:
                    for item in self.__mappedKeys[section]:
                        _key = item["key"]
                        if conf.has_option(section,_key):
                            result[section][_key] = item["mapping"](conf.get(section,_key))
                            # setattr(result, section.upper(), item["mapping"](conf.get(section,_key)))
                    continue
                
                # setattr(result,section,dict(conf.items(section)))
        else:
            raise AttributeError('Some sections are missing', *sections)
        return result


def load(file_path,type_file, mapping, asDict=True):
    # TODO: Make all the params and return always a dict or custum dict like object
    configuration = Configurator(file_path,type_file,keysMapping=mapping)
    if asDict:
        return configuration.getConfigDict()
    return configuration.getConfigObj()