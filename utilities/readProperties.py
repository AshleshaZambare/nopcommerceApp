import configparser

config = configparser.RawConfigParser()
config.read('.\\configuration\\config.ini')

class ReadConfig():
    @staticmethod
    def getApplicationURL():
        url = config.get("common info", 'baseURL')
        return url
    @staticmethod
    def getUsername():
        username = config.get("common info", 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get("common info", 'password')
        return password

    @staticmethod
    def get_file_path():
        file_path = config.get("common info", 'xl_file_path')
        return file_path

