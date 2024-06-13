from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from models import Event, Participant, Speaker, Venue

# Define the database connection
engine = create_engine('sqlite:///event_hub.db', echo=True)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()
session.query(Event).delete() 
session.query(Participant).delete()
session.query(Speaker).delete()
session.query(Venue).delete()

fake = Faker()

# Seed events
for _ in range(10):  
    event = Event(
        name=fake.catch_phrase(),
        date=fake.date_between(start_date='-30d', end_date='+30d'),
        description=fake.text(),
        capacity=fake.random_int(min=50, max=500)
    )
    session.add(event)

# Seed participants
for _ in range(10):  
    participant = Participant(
        name=fake.name(),
        event_id=fake.random_element(elements=session.query(Event).all()).id
    )
    session.add(participant)

# Seed speakers
for _ in range(10):  
    speaker = Speaker(
        name=fake.name()
    )
    session.add(speaker)

# Seed venues
for _ in range(5): 
    venue = Venue(
        name=fake.company()
    )
    session.add(venue)

session.commit()

print("Seed data has been successfully added to the database.")
