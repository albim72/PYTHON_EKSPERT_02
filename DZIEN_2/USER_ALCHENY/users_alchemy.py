import mysql.connector
import sqlalchemy

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import  declarative_base


engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:abc123@localhost:3306/dbtestowa',echo=False)

#definiowanie i tworzenie tabel
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(length=50))
    fullname = sqlalchemy.Column(sqlalchemy.String(length=50))
    nickname = sqlalchemy.Column(sqlalchemy.String(length=50))

    def __repr__(self):
        return f"<User(name = {self.name}, fullname = {self.fullname}, nickname = {self.nickname})>"

Base.metadata.create_all(engine)

Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()

p_user = User(name="Marcin", fullname = "Marcin Albiniak",nickname="marc")
session.add(p_user)

s_user = User(name="Nadia", fullname = "Nadia Kowal",nickname="kowala")
session.add(s_user)

session.commit()
print("______wszystkie rekordy________")
for s in session.query(User).all():
    print(s.fullname)

print("__________filtrowanie__________")
for s in session.query(User).filter(User.nickname=="marc"):
    print(s.fullname)
