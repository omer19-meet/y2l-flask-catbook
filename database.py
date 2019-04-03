from models import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///cats.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()

def create_cat(name, votes):
    cat_object = Cat(name=name, votes=votes)
    session.add(cat_object)
    session.commit()

def get_all_cats():
    cats = session.query(Cat).all()
    return cats

def get_cat_by_id(their_id):
	cat = session.query(Cat).filter_by(id=their_id).first()
	return cat

def count_votes(id):
	cat = session.query(Cat).filter_by(id=id).first()
	# session.commit()
	cat.votes += 1
	session.commit()																																																																		
	# return cat.votes
# the goa;l of the function is 
# 1) get the cat from the db
# 2) increase the votes by 1
# 3) save it to t

# create_cat("Mizti", 0)
# create_cat("Miyahoooo", 0)

    
# def add_vote():
	