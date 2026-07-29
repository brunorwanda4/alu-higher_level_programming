#!/usr/bin/python3
"""Lists all State objects and their City objects, using one query"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).options(
        joinedload(State.cities)).order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
        for city in sorted(state.cities, key=lambda c: c.id):
            print("\t{}: {}".format(city.id, city.name))

    session.close()
