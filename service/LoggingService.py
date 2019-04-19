import psycopg2

from configuration.configuration import Configuration
from model.User import User


class LoggingService(object):

    def __init__(self):
        self.connection = psycopg2.connect(host=Configuration.get_database_url(),
                                           user=Configuration.get_database_username(),
                                           password=Configuration.get_database_password(),
                                           dbname=Configuration.get_database_name())

    def getUser(self, login, password):
        cur = self.connection.cursor()
        cur.execute(
            "select * from account where login = %s and password = %s", (login, password))
        if(cur.rowcount != 0):
            rows = cur.fetchall()
            user = User(rows[0][0], rows[0][1].strftime("%Y-%m-%d %H:%M:%S"), rows[0][2], rows[0][3], rows[0][4], rows[0][5].strftime("%Y-%m-%d %H:%M:%S"), rows[0][6], rows[0][7], rows[0][8], rows[0][9], rows[0][10])
            return user
        return None