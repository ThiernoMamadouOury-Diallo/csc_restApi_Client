import yaml
import logging
import os

class Configuration(object):

    configuration_data = []
    configuration_file = ""

    @staticmethod
    def initialization():
        Configuration.configuration_file = os.getcwd() + "/configuration.yml"
        logging.info(Configuration.configuration_file)
        Configuration.configuration_data = None

        f = open(Configuration.configuration_file, 'r')
        Configuration.configuration_data = yaml.load(f.read())
        f.close()

    @staticmethod
    def get_database_url():
        return Configuration.configuration_data['database']['url']

    @staticmethod
    def get_database_port():
        return Configuration.configuration_data['database']['port']

    @staticmethod
    def get_database_username():
        return Configuration.configuration_data['database']['username']

    @staticmethod
    def get_database_password():
        return Configuration.configuration_data['database']['password']

    @staticmethod
    def get_database_name():
        return Configuration.configuration_data['database']['name']
