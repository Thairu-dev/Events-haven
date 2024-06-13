import click
from datetime import datetime
from models import Base, Event, Participant, Speaker, Venue
from utils import create_session, create_db_engine

engine = create_db_engine()
Base.metadata.create_all(engine)

# Initialize an empty list to store registered participants
participants_list = []

# Initialize an empty dictionary to store events
events_dict = {}

@click.group()
def cli():
    pass

def validate_date(ctx, param, value):
    try:
        return datetime.strptime(value, '%Y-%m-%d').date()
    except ValueError:
        raise click.BadParameter('Date format should be YYYY-MM-DD')
    
def validate_non_empty(ctx, param, value):
    if not value:
        raise click.BadParameter(f"{param.human_readable_name} cannot be empty.")
    return value

# Create new event
@cli.command()
@click.option('--name', prompt='Event Name', help='Name of the event', default='', callback=validate_non_empty)
@click.option('--date', prompt='Event Date (YYYY-MM-DD)', callback=validate_date, help='Date of the event')
@click.option('--description', prompt='Event Description', help='Description of the event', callback=validate_non_empty, default='')
@click.option('--capacity', prompt='Event Capacity', type=int, help='Maximum capacity of the event', callback=validate_non_empty, default=0)

def create_event(name, date, description, capacity):
    """Create a new event."""

# Create a session using create_session from utils.py
    session = create_session(engine)   

    event = Event(name=name, date=date, description=description, capacity=capacity)
    session.add(event)
    session.commit()

    click.echo(f'Event "{name}" created successfully.')

# Register a participant for an event
@cli.command()
@click.option('--event-name', prompt='Event Name', help='Name of the event', callback=validate_non_empty, default='')
@click.option('--participant-name', prompt='Participant Name', help='Name of the participant',callback=validate_non_empty, default='')
def register_participant(event_name, participant_name):
    """Register a participant for an event."""
  
    session = create_session(engine)    

    # Find the event by name
    event = session.query(Event).filter_by(name=event_name).first()    

    if event:
        participant = Participant(name=participant_name, event=event)
        session.add(participant)
        session.commit()
        
        # Add the participant to the list
        participants_list.append(participant_name)

        click.echo(f'Participant "{participant_name}" registered for the event "{event_name}".')
    else:
        click.echo(f'Event with name "{event_name}" not found.')


# Add speaker to an event
@cli.command()
@click.option('--event-name', prompt='Event Name', help='Name of the event', callback=validate_non_empty, default='')
@click.option('--speaker-name', prompt='Speaker Name', help='Name of the speaker', callback=validate_non_empty, default='')
def add_speaker(event_name, speaker_name):
    """Add a speaker to an event."""
   
    session = create_session(engine)

     # Find the event by name
    event = session.query(Event).filter_by(name=event_name).first()

    if event:
        speaker = Speaker(name=speaker_name)
        event.speakers.append(speaker)
        session.commit()

        click.echo(f'Speaker "{speaker_name}" added to the event "{event_name}".')
    else:
        click.echo(f'Event with name "{event_name}" not found.')


# Add a venue to an event
@cli.command()
@click.option('--event-name', prompt='Event Name', help='Name of the event', callback=validate_non_empty, default='')
@click.option('--venue-name', prompt='Venue Name', help='Name of the venue', callback=validate_non_empty, default='')
def add_venue(event_name, venue_name):
    """Add a venue to an event."""
   
    session = create_session(engine)  

     # Find the event by name
    event = session.query(Event).filter_by(name=event_name).first()

    if event:
        venue = Venue(name=venue_name)
        event.venues.append(venue)
        session.commit()  

        click.echo(f'Venue "{venue_name}" added to the event "{event_name}".')
    else:
        click.echo(f'Event with name "{event_name}" not found.')  


# Displays List of registered participants
@cli.command()
@click.option('--event-name', prompt='Event Name', help='Name of the event', callback=validate_non_empty, default='')
def list_participants(event_name):
    """List all registered participants for an event."""
    
    session = create_session(engine) 

    # Find the event by name
    event = session.query(Event).filter_by(name=event_name).first()   

    if event:
        participants = event.participants
        if participants:
            click.echo(f'List of Registered Participants for "{event_name}":')
            for participant in participants:
                click.echo(participant.name)
        else:
            click.echo(f'No participants registered for "{event_name}".')
    else:
        click.echo(f'Event with name "{event_name}" not found.')
 

# Displays list of events in chronological order based on date
@cli.command()
def list_events():
    """List events in chronological order based on date."""
    
    session = create_session(engine)  

    # Query all events and sort them by date
    events = session.query(Event).order_by(Event.date).all()

    if events:
        for event in events:
            events_dict[event.name] = {
                "Name": event.name,
                "Date": event.date.strftime('%Y-%m-%d')
            }
        
        click.echo("List of Events in Chronological Order:")

        for event_name in sorted(events_dict.keys(), key=lambda x: events_dict[x]['Date']):
            event_details = events_dict[event_name]
            click.echo(f"Event Name: {event_details['Name']}, Date: {event_details['Date']}")
    else:
        click.echo("No events found in the database.")

if __name__ == '__main__':
    cli()        