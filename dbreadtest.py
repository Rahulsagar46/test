# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 16:13:02 2019

@author: Rahul
"""


#from bdschema import Application,engine
#from sqlalchemy.orm import sessionmaker
#
##engine = create_engine('sqlite:///applications.db',echo=True)
#
#Session =sessionmaker(bind=engine)
#session =Session()
#
##applications = session.query(Application).all()
##for application in applications:
##    session.delete(application)
##    session.commit()
#
##applications1 = session.query(Application).all()
##
##for application in applications1:
##    print('Company: ',application.company)
#
#session.close()


import re

text = "The rain in Spain"

x = re.findall("Spain\Z",text)

print(x)