# Event Haven

# Introduction
Event Hub is a versatile and user-friendly command-line interface (CLI) tool designed to simplify event management. Whether you're organizing a small gathering, a corporate conference, or anything in between, Event Hub will streamline your event planning process. With Event Hub, you can effortlessly create, manage, and track events, participants, speakers and venues, all from the convenience of your terminal. 

# Table of contents
1. Getting started
   * Prerequisites
   * Installation
2. Features
3. Usage
4. Commands
5. License
6. Author

# Getting Started
   # Prerequisites
  Before you start, ensure that you meet the following prerequisites:
   * Python 3.6 or higher
   * Git 

  # Installation
 1. Clone the repository to your local machine.
 2. Navigate to the project directory.
 3. Set up a virtual environment and install the required dependencies: 

    `pipenv install`.
4. Activate  the virtual environment: 

   `pipenv shell`.

# Features
Event Hub offers an array of features designed to simplify the event management tasks:

* Create Events: Rapidly create new events by providing essential details like name, date, description, and capacity.

* Register Participants: Easily register participants for events, associating them with specific occurrences.

* Add Speakers: Seamlessly assign speakers to events, streamlining event agenda management.

* Add Venues: Associate venues with events for efficient tracking of event locations.

* List Participants: Instantly view a list of registered participants for any event in the database.

* List Events: Display events in chronological order, sorted by date.

# Usage
To get started, execute the `cli.py` script: 

    python lib/cli.py

This command launches the CLI interface, providing access to a wide range of commands tailored to facilitate event creation, management, and tracking.

# Commands
Here is a list of available commands and their use cases:
 - Create Event
          
       python lib/cli.py create-event

 This command guides you through the process of creating a new event. Input the event's name, date, description, and capacity.

 - Register Participant

       python lib/cli.py register-participant

Use this command to register a participant for an event. Specify the event name and the participant's name.

- Add Speaker

      python lib/cli.py add-speaker

Add a speaker to an event by entering the event name and the speaker's name.

- Add Venue

      python lib/cli.py add-venue

Associate a venue with an event. Input the event name and venue name to link them.

- List Participants

      python lib/cli.py list-participants

View a list of registered participants for a specific event by providing the event's name.

- List Events

      python lib/cli.py list-events

Display a chronological list of events, ordered by their respective dates.

# License
This project is licensed under the MIT License. 

# Author
Joseph Thairu

joejoement@gmail.com