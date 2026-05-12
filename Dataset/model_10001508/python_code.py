from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class String(Enum):
    pass

############################################
# Definition of Classes
############################################










class Event__:

    pass


class User__4:

    pass


class Date:

    pass


class User:

    def __init__(self, tickets: str, id: str, name: str, birthdate: Date, gender: str, userImage: str, friends: str, events: Event__, password: str, company: str, selfDescription: str, ticket3: set["Ticket"] = None, event5: set["Event"] = None):
        self.tickets = tickets
        self.id = id
        self.name = name
        self.birthdate = birthdate
        self.gender = gender
        self.userImage = userImage
        self.friends = friends
        self.events = events
        self.password = password
        self.company = company
        self.selfDescription = selfDescription
        self.ticket3 = ticket3 if ticket3 is not None else set()
        self.event5 = event5 if event5 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def company(self):
        return self.__company
    @company.setter
    def company(self, company: str):
        self.__company = company

    @property
    def friends(self):
        return self.__friends
    @friends.setter
    def friends(self, friends: str):
        self.__friends = friends

    @property
    def events(self):
        return self.__events
    @events.setter
    def events(self, events: Event__):
        self.__events = events

    @property
    def userImage(self):
        return self.__userImage
    @userImage.setter
    def userImage(self, userImage: str):
        self.__userImage = userImage

    @property
    def tickets(self):
        return self.__tickets
    @tickets.setter
    def tickets(self, tickets: str):
        self.__tickets = tickets

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def selfDescription(self):
        return self.__selfDescription
    @selfDescription.setter
    def selfDescription(self, selfDescription: str):
        self.__selfDescription = selfDescription

    @property
    def birthdate(self):
        return self.__birthdate
    @birthdate.setter
    def birthdate(self, birthdate: Date):
        self.__birthdate = birthdate

    @property
    def event5(self):
        return self.__event5
    @event5.setter
    def event5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__event5", None)
        self.__event5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user4"):
                    opp_val = getattr(item, "user4", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user4"):
                    opp_val = getattr(item, "user4", None)
                    
                    if opp_val is None:
                        setattr(item, "user4", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def ticket3(self):
        return self.__ticket3
    @ticket3.setter
    def ticket3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__ticket3", None)
        self.__ticket3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user2"):
                    opp_val = getattr(item, "user2", None)
                    
                    if opp_val == self:
                        setattr(item, "user2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user2"):
                    opp_val = getattr(item, "user2", None)
                    
                    setattr(item, "user2", self)
                    



class Ticket:

    def __init__(self, id: str, event: Event, event20: "Event" = None, user2: "User" = None):
        self.id = id
        self.event = event
        self.event20 = event20
        self.user2 = user2
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def event(self):
        return self.__event
    @event.setter
    def event(self, event: Event):
        self.__event = event

    @property
    def event20(self):
        return self.__event20
    @event20.setter
    def event20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ticket__event20", None)
        self.__event20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ticket1"):
                opp_val = getattr(old_value, "ticket1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ticket1"):
                opp_val = getattr(value, "ticket1", None)
                if opp_val is None:
                    setattr(value, "ticket1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def user2(self):
        return self.__user2
    @user2.setter
    def user2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ticket__user2", None)
        self.__user2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ticket3"):
                opp_val = getattr(old_value, "ticket3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ticket3"):
                opp_val = getattr(value, "ticket3", None)
                if opp_val is None:
                    setattr(value, "ticket3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Event:

    def __init__(self, type: str, time: str, participantCount: int, placeName: str, image: str, id: String, participants: str, location: str, organizator: User, discussion: str, about: str, ticket1: set["Ticket"] = None, user4: set["User"] = None):
        self.type = type
        self.time = time
        self.participantCount = participantCount
        self.placeName = placeName
        self.image = image
        self.id = id
        self.participants = participants
        self.location = location
        self.organizator = organizator
        self.discussion = discussion
        self.about = about
        self.ticket1 = ticket1 if ticket1 is not None else set()
        self.user4 = user4 if user4 is not None else set()
        
        pass
    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def organizator(self):
        return self.__organizator
    @organizator.setter
    def organizator(self, organizator: User):
        self.__organizator = organizator

    @property
    def placeName(self):
        return self.__placeName
    @placeName.setter
    def placeName(self, placeName: str):
        self.__placeName = placeName

    @property
    def about(self):
        return self.__about
    @about.setter
    def about(self, about: str):
        self.__about = about

    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time: str):
        self.__time = time

    @property
    def discussion(self):
        return self.__discussion
    @discussion.setter
    def discussion(self, discussion: str):
        self.__discussion = discussion

    @property
    def image(self):
        return self.__image
    @image.setter
    def image(self, image: str):
        self.__image = image

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: String):
        self.__id = id

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def participants(self):
        return self.__participants
    @participants.setter
    def participants(self, participants: str):
        self.__participants = participants

    @property
    def participantCount(self):
        return self.__participantCount
    @participantCount.setter
    def participantCount(self, participantCount: int):
        self.__participantCount = participantCount

    @property
    def ticket1(self):
        return self.__ticket1
    @ticket1.setter
    def ticket1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Event__ticket1", None)
        self.__ticket1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "event20"):
                    opp_val = getattr(item, "event20", None)
                    
                    if opp_val == self:
                        setattr(item, "event20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "event20"):
                    opp_val = getattr(item, "event20", None)
                    
                    setattr(item, "event20", self)
                    

    @property
    def user4(self):
        return self.__user4
    @user4.setter
    def user4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Event__user4", None)
        self.__user4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "event5"):
                    opp_val = getattr(item, "event5", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "event5"):
                    opp_val = getattr(item, "event5", None)
                    
                    if opp_val is None:
                        setattr(item, "event5", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

