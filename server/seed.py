#!/usr/bin/env python3
# server/seed.py

from app import app
from models import Earthquake, db

with app.app_context():
    # Delete all rows in the "earthquakes" table
    Earthquake.query.delete()

    # Add several Earthquake instances to the "earthquakes" table

    earthquake_1 = Earthquake(magnitude=9.5, location="Chile", year=1960)

    db.session.add(earthquake_1)

    db.session.add(Earthquake(magnitude=9.2, location="Alaska", year=1964))
    db.session.add(Earthquake(magnitude=8.6, location="Alaska", year=1946))
    db.session.add(Earthquake(magnitude=8.5, location="Banda Sea", year=1934))
    db.session.add(Earthquake(magnitude=8.4, location="Chile", year=1922))

    # Commit the transaction
    db.session.commit()
