from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Table
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define database connection
engine = create_engine('sqlite:///event_hub.db', echo=True)

# Base class for all classes
Base = declarative_base()

# Many-to-Many Relationship Table (Events - Speakers)
event_speaker_association = Table(
    'event_speaker_association',
    Base.metadata,
    Column('event_id', Integer, ForeignKey('events.id')),
    Column('speaker_id', Integer, ForeignKey('speakers.id'))
)

# Many-to-Many Relationship Table (Events - Venues)
event_venue_association = Table(
    'event_venue_association',
    Base.metadata,
    Column('event_id', Integer, ForeignKey('events.id')),
    Column('venue_id', Integer, ForeignKey('venues.id'))
)

class Event(Base):
    __tablename__ = 'events'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    date = Column(Date)
    description = Column(String(255))
    capacity = Column(Integer)

    # Define the one-to-many relationship with participants
    participants = relationship('Participant', back_populates='event')

    # Define the many-to-many relationship with speakers
    speakers = relationship('Speaker', secondary=event_speaker_association, back_populates='events')

    # Define the many-to-many relationship with venues
    venues = relationship('Venue', secondary=event_venue_association, back_populates='events')

    def __repr__(self):
        return f"<Event(name='{self.name}', date='{self.date}')>"   
    

class Participant(Base):
    __tablename__ = 'participants'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))  
    
    event_id = Column(Integer, ForeignKey('events.id'))

    # Define the many-to-one relationship with events
    event = relationship('Event', back_populates='participants')

    def __repr__(self):
        return f"<Participant(name='{self.name}')>"
    
class Speaker(Base):
    __tablename__ = 'speakers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))

    # Define the many-to-many relationship with events
    events = relationship('Event', secondary=event_speaker_association, back_populates='speakers')

    def __repr__(self):
        return f"<Speaker(name='{self.name}')>"


class Venue(Base):
    __tablename__ = 'venues'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100))    

   # Define the many-to-many relationship with events
    events = relationship('Event', secondary=event_venue_association, back_populates='venues')  
        
    def __repr__(self):
        return f"<Venue(name='{self.name}')>"

# create all tables in the database
Base.metadata.create_all(engine)

# create session
Session = sessionmaker(bind=engine)
session = Session()        