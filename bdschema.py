# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 21:37:45 2019

@author: Rahul
"""
from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Application(Base):
    __tablename__ = "application"    
    id = Column('id',Integer,primary_key=True)
    company = Column('company',String)
    jobid = Column('jobid',String)
    role = Column('role',String)
    location = Column('location',String)

engine = create_engine('sqlite:///applications.db',echo=True)
if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)

#Session =sessionmaker(bind=engine)
#session =Session()
#
#user = User()
#user.id=0
#user.username='Rahul'
#
#session.add(user)
#session.commit()
#users = session.query(User).all()

#for user in users:
#    print('Username: ',user.username,'& ID: ',user.id )

#session.close()
    