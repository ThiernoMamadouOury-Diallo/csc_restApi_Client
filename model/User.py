from json import JSONEncoder


class User(object):
    def __init__(self, id, reg_date, login, firstname, lastname, birthdate, phone_number, city, address, postalcode, email):
        self.id = id
        self.reg_date = reg_date
        self.login = login
        self.firstname = firstname
        self.lastname = lastname
        self.birthdate = birthdate
        self.phone_number = phone_number
        self.city = city
        self.address = address
        self.postalcode = postalcode
        self.email = email

class UserEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return o.__dict__
        else:
            return JSONEncoder.default(self, o)