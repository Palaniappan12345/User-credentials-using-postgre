

from database import db

class MyUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    city = db.Column(db.String(50))
    state = db.Column(db.String(23))

class City(db.Model):
    __tablename__ = 'city'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    state = db.Column(db.String(50))
    country = db.Column(db.String(30))
    citycode = db.Column(db.String(10))

    def __init__(self, name, state, country):
        self.name = name
        self.state = state
        self.country = country

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4) 

# class login(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(100), unique=True)
#     password = db.Column(db.String(100))


class One(db.Model):
    __tablename__ = 'one'

    id = db.Column(db.Integer, primary_key=True)
    two = db.Column(db.String(100), unique=True)
    three = db.Column(db.String(100), unique=True)

    def __init__(self, two, three):
        self.two = two
        self.three = three

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4) 

class Name(db.Model):
    __tablename__ = 'name'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    email = db.Column(db.String(50))
    contact_number = db.Column(db.String(30))
    

    def __init__(self, name, email, contact_number):
        self.name = name
        self.email = email 
        self.contact_number = contact_number

    def as_dict(self):
       return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4) 