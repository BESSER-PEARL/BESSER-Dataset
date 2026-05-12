from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class TALK_TYPE(Enum):
    WORKSHOP = "WORKSHOP"
    DEMONSTRATION = "DEMONSTRATION"
    CONFERENCE = "CONFERENCE"
class GENDER(Enum):
    UNKNOWN = "UNKNOWN"
    MALE = "MALE"
    FEMALE = "FEMALE"


############################################
# Definition of Classes
############################################

class conference_Room:

    def __init__(self, name: str, capacity: int, conference_Room: "conference_Site" = None):
        self.name = name
        self.capacity = capacity
        self.conference_Room = conference_Room
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: int):
        self.__capacity = capacity


    @property
    def conference_Room(self):
        return self.__conference_Room

    @conference_Room.setter
    def conference_Room(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Room__conference_Room", None)
        self.__conference_Room = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conference_Site20"):
                opp_val = getattr(old_value, "conference_Site20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conference_Site20"):
                opp_val = getattr(value, "conference_Site20", None)
                if opp_val is None:
                    setattr(value, "conference_Site20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class conference_Person:

    def __init__(self, firstname: str, lastname: str, age: int, eclipseCommiter: bool, gender: str, isRegistered: bool, conference_Person: "conference_Conference" = None, conference_Person8: set["conference_Talk"] = None, conference_Person15: "conference_Talk" = None, conference_Person18: "conference_Talk" = None):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.eclipseCommiter = eclipseCommiter
        self.gender = gender
        self.isRegistered = isRegistered
        self.conference_Person = conference_Person
        self.conference_Person8 = conference_Person8 if conference_Person8 is not None else set()
        self.conference_Person15 = conference_Person15
        self.conference_Person18 = conference_Person18
        
        pass
    @property
    def isRegistered(self):
        return self.__isRegistered

    @isRegistered.setter
    def isRegistered(self, isRegistered: bool):
        self.__isRegistered = isRegistered


    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender


    @property
    def eclipseCommiter(self):
        return self.__eclipseCommiter

    @eclipseCommiter.setter
    def eclipseCommiter(self, eclipseCommiter: bool):
        self.__eclipseCommiter = eclipseCommiter


    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname


    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname


    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age


    @property
    def conference_Person(self):
        return self.__conference_Person

    @conference_Person.setter
    def conference_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Person__conference_Person", None)
        self.__conference_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conference_Conference"):
                opp_val = getattr(old_value, "conference_Conference", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conference_Conference"):
                opp_val = getattr(value, "conference_Conference", None)
                if opp_val is None:
                    setattr(value, "conference_Conference", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def conference_Person15(self):
        return self.__conference_Person15

    @conference_Person15.setter
    def conference_Person15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Person__conference_Person15", None)
        self.__conference_Person15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conference_Talk14"):
                opp_val = getattr(old_value, "conference_Talk14", None)
                if opp_val == self:
                    setattr(old_value, "conference_Talk14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conference_Talk14"):
                opp_val = getattr(value, "conference_Talk14", None)
                setattr(value, "conference_Talk14", self)

    @property
    def conference_Person8(self):
        return self.__conference_Person8

    @conference_Person8.setter
    def conference_Person8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Person__conference_Person8", None)
        self.__conference_Person8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "conference_Talk9"):
                    opp_val = getattr(item, "conference_Talk9", None)
                    
                    if opp_val == self:
                        setattr(item, "conference_Talk9", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "conference_Talk9"):
                    opp_val = getattr(item, "conference_Talk9", None)
                    
                    setattr(item, "conference_Talk9", self)
                    

    @property
    def conference_Person18(self):
        return self.__conference_Person18

    @conference_Person18.setter
    def conference_Person18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Person__conference_Person18", None)
        self.__conference_Person18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conference_Talk17"):
                opp_val = getattr(old_value, "conference_Talk17", None)
                if opp_val == self:
                    setattr(old_value, "conference_Talk17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conference_Talk17"):
                opp_val = getattr(value, "conference_Talk17", None)
                setattr(value, "conference_Talk17", self)

class conference_Conference:

    def __init__(self, name: str, overview: str, place: str, conference_Conference2: set["conference_Talk"] = None, conference_Conference4: set["conference_Topic"] = None, conference_Conference6: set["conference_Site"] = None, conference_Conference: set["conference_Person"] = None):
        self.name = name
        self.overview = overview
        self.place = place
        self.conference_Conference2 = conference_Conference2 if conference_Conference2 is not None else set()
        self.conference_Conference4 = conference_Conference4 if conference_Conference4 is not None else set()
        self.conference_Conference6 = conference_Conference6 if conference_Conference6 is not None else set()
        self.conference_Conference = conference_Conference if conference_Conference is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def overview(self):
        return self.__overview

    @overview.setter
    def overview(self, overview: str):
        self.__overview = overview


    @property
    def place(self):
        return self.__place

    @place.setter
    def place(self, place: str):
        self.__place = place


    @property
    def conference_Conference2(self):
        return self.__conference_Conference2

    @conference_Conference2.setter
    def conference_Conference2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Conference__conference_Conference2", None)
        self.__conference_Conference2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "conference_Talk"):
                    opp_val = getattr(item, "conference_Talk", None)
                    
                    if opp_val == self:
                        setattr(item, "conference_Talk", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "conference_Talk"):
                    opp_val = getattr(item, "conference_Talk", None)
                    
                    setattr(item, "conference_Talk", self)
                    

    @property
    def conference_Conference6(self):
        return self.__conference_Conference6

    @conference_Conference6.setter
    def conference_Conference6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Conference__conference_Conference6", None)
        self.__conference_Conference6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "conference_Site"):
                    opp_val = getattr(item, "conference_Site", None)
                    
                    if opp_val == self:
                        setattr(item, "conference_Site", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "conference_Site"):
                    opp_val = getattr(item, "conference_Site", None)
                    
                    setattr(item, "conference_Site", self)
                    

    @property
    def conference_Conference(self):
        return self.__conference_Conference

    @conference_Conference.setter
    def conference_Conference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Conference__conference_Conference", None)
        self.__conference_Conference = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "conference_Person"):
                    opp_val = getattr(item, "conference_Person", None)
                    
                    if opp_val == self:
                        setattr(item, "conference_Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "conference_Person"):
                    opp_val = getattr(item, "conference_Person", None)
                    
                    setattr(item, "conference_Person", self)
                    

    @property
    def conference_Conference4(self):
        return self.__conference_Conference4

    @conference_Conference4.setter
    def conference_Conference4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Conference__conference_Conference4", None)
        self.__conference_Conference4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "conference_Topic"):
                    opp_val = getattr(item, "conference_Topic", None)
                    
                    if opp_val == self:
                        setattr(item, "conference_Topic", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "conference_Topic"):
                    opp_val = getattr(item, "conference_Topic", None)
                    
                    setattr(item, "conference_Topic", self)
                    

class conference_Site:

    def __init__(self, documentation: str, name: str, conference_Site: "conference_Conference" = None, conference_Site20: set["conference_Room"] = None):
        self.documentation = documentation
        self.name = name
        self.conference_Site = conference_Site
        self.conference_Site20 = conference_Site20 if conference_Site20 is not None else set()
        
        pass
    @property
    def documentation(self):
        return self.__documentation

    @documentation.setter
    def documentation(self, documentation: str):
        self.__documentation = documentation


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def conference_Site20(self):
        return self.__conference_Site20

    @conference_Site20.setter
    def conference_Site20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Site__conference_Site20", None)
        self.__conference_Site20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "conference_Room"):
                    opp_val = getattr(item, "conference_Room", None)
                    
                    if opp_val == self:
                        setattr(item, "conference_Room", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "conference_Room"):
                    opp_val = getattr(item, "conference_Room", None)
                    
                    setattr(item, "conference_Room", self)
                    

    @property
    def conference_Site(self):
        return self.__conference_Site

    @conference_Site.setter
    def conference_Site(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Site__conference_Site", None)
        self.__conference_Site = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conference_Conference6"):
                opp_val = getattr(old_value, "conference_Conference6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conference_Conference6"):
                opp_val = getattr(value, "conference_Conference6", None)
                if opp_val is None:
                    setattr(value, "conference_Conference6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class conference_Topic:

    def __init__(self, description: str, references: str, documentation: str, conference_Topic: "conference_Conference" = None, conference_Topic12: "conference_Talk" = None):
        self.description = description
        self.references = references
        self.documentation = documentation
        self.conference_Topic = conference_Topic
        self.conference_Topic12 = conference_Topic12
        
        pass
    @property
    def documentation(self):
        return self.__documentation

    @documentation.setter
    def documentation(self, documentation: str):
        self.__documentation = documentation


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def references(self):
        return self.__references

    @references.setter
    def references(self, references: str):
        self.__references = references


    @property
    def conference_Topic(self):
        return self.__conference_Topic

    @conference_Topic.setter
    def conference_Topic(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Topic__conference_Topic", None)
        self.__conference_Topic = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conference_Conference4"):
                opp_val = getattr(old_value, "conference_Conference4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conference_Conference4"):
                opp_val = getattr(value, "conference_Conference4", None)
                if opp_val is None:
                    setattr(value, "conference_Conference4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def conference_Topic12(self):
        return self.__conference_Topic12

    @conference_Topic12.setter
    def conference_Topic12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Topic__conference_Topic12", None)
        self.__conference_Topic12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conference_Talk11"):
                opp_val = getattr(old_value, "conference_Talk11", None)
                if opp_val == self:
                    setattr(old_value, "conference_Talk11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conference_Talk11"):
                opp_val = getattr(value, "conference_Talk11", None)
                setattr(value, "conference_Talk11", self)

class conference_Talk:

    def __init__(self, title: str, type: str, documentation: str, conference_Talk: "conference_Conference" = None, conference_Talk9: "conference_Person" = None, conference_Talk11: "conference_Topic" = None, conference_Talk14: "conference_Person" = None, conference_Talk17: "conference_Person" = None):
        self.title = title
        self.type = type
        self.documentation = documentation
        self.conference_Talk = conference_Talk
        self.conference_Talk9 = conference_Talk9
        self.conference_Talk11 = conference_Talk11
        self.conference_Talk14 = conference_Talk14
        self.conference_Talk17 = conference_Talk17
        
        pass
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def documentation(self):
        return self.__documentation

    @documentation.setter
    def documentation(self, documentation: str):
        self.__documentation = documentation


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def conference_Talk14(self):
        return self.__conference_Talk14

    @conference_Talk14.setter
    def conference_Talk14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Talk__conference_Talk14", None)
        self.__conference_Talk14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conference_Person15"):
                opp_val = getattr(old_value, "conference_Person15", None)
                if opp_val == self:
                    setattr(old_value, "conference_Person15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conference_Person15"):
                opp_val = getattr(value, "conference_Person15", None)
                setattr(value, "conference_Person15", self)

    @property
    def conference_Talk17(self):
        return self.__conference_Talk17

    @conference_Talk17.setter
    def conference_Talk17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Talk__conference_Talk17", None)
        self.__conference_Talk17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conference_Person18"):
                opp_val = getattr(old_value, "conference_Person18", None)
                if opp_val == self:
                    setattr(old_value, "conference_Person18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conference_Person18"):
                opp_val = getattr(value, "conference_Person18", None)
                setattr(value, "conference_Person18", self)

    @property
    def conference_Talk(self):
        return self.__conference_Talk

    @conference_Talk.setter
    def conference_Talk(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Talk__conference_Talk", None)
        self.__conference_Talk = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conference_Conference2"):
                opp_val = getattr(old_value, "conference_Conference2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conference_Conference2"):
                opp_val = getattr(value, "conference_Conference2", None)
                if opp_val is None:
                    setattr(value, "conference_Conference2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def conference_Talk9(self):
        return self.__conference_Talk9

    @conference_Talk9.setter
    def conference_Talk9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Talk__conference_Talk9", None)
        self.__conference_Talk9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conference_Person8"):
                opp_val = getattr(old_value, "conference_Person8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conference_Person8"):
                opp_val = getattr(value, "conference_Person8", None)
                if opp_val is None:
                    setattr(value, "conference_Person8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def conference_Talk11(self):
        return self.__conference_Talk11

    @conference_Talk11.setter
    def conference_Talk11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Talk__conference_Talk11", None)
        self.__conference_Talk11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conference_Topic12"):
                opp_val = getattr(old_value, "conference_Topic12", None)
                if opp_val == self:
                    setattr(old_value, "conference_Topic12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conference_Topic12"):
                opp_val = getattr(value, "conference_Topic12", None)
                setattr(value, "conference_Topic12", self)
