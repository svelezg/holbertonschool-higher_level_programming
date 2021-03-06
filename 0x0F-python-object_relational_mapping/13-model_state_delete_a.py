#!/usr/bin/python3
"""changes the name of a State object from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State

from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm.exc import MultipleResultsFound
from sqlalchemy import insert
from sqlalchemy import MetaData

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1],
                                                    sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # create session
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    query = session.query(State).filter(State.name.ilike('%a%'))
    query.delete(synchronize_session='fetch')

    session.commit()
