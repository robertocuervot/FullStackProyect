from sqlalchemy import Column, Integer, String, String

from declarative_base import Base

class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    position = Column(String)
    skills = Column(String)