import configparser

configParser = configparser.RawConfigParser()
configFilePath = "config.ini"
configParser.read(configFilePath)


def cfg(section, key, casting=str):
    return casting(configParser.get(section, key))
