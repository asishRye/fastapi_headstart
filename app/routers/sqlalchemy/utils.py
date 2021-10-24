from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import Column
from sqlalchemy.sql.sqltypes import Integer, String

engine = create_engine(
    'postgresql://postgres:mysecretpassword@localhost:5432/mydb', echo=False)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))
    # another_field = Column(String(50))


# Base.metadata.create_all(engine)


def get_records(id: int):
    try:
        db_results = session.query(Student).filter(Student.id == id).first()
        return db_results
    except Exception as error:
        print("Error occured", error)


def write_records(obj=None):
    try:
        student1 = Student(name=obj["name"], age=obj["age"],
                           grade=obj["grade"], id=obj["id"])
        session.add(student1)
        session.commit()
        print("Records are written", obj)
    except Exception as error:
        print("Error occured", error)
