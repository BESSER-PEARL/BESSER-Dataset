from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Attitude(Enum):
    cool = "cool"
    disgraceful = "disgraceful"
    serious = "serious"


############################################
# Definition of Classes
############################################

class Participant:

    pass
class makingOf_conference_Person:

    pass
class conference_makingOf_Participant:

    def __init__(self, age: int, attitude: str, conference_makingOf_Participant: "makingOf_conference_Person" = None):
        self.age = age
        self.attitude = attitude
        self.conference_makingOf_Participant = conference_makingOf_Participant
        
        pass
    @property
    def attitude(self):
        return self.__attitude

    @attitude.setter
    def attitude(self, attitude: str):
        self.__attitude = attitude


    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age: int):
        self.__age = age


    @property
    def conference_makingOf_Participant(self):
        return self.__conference_makingOf_Participant

    @conference_makingOf_Participant.setter
    def conference_makingOf_Participant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_makingOf_Participant__conference_makingOf_Participant", None)
        self.__conference_makingOf_Participant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "makingOf_conference_Person"):
                opp_val = getattr(old_value, "makingOf_conference_Person", None)
                if opp_val == self:
                    setattr(old_value, "makingOf_conference_Person", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "makingOf_conference_Person"):
                opp_val = getattr(value, "makingOf_conference_Person", None)
                setattr(value, "makingOf_conference_Person", self)

class conference_makingOf_Task:

    def __init__(self, name: str, conference_makingOf_Task: set["Participant"] = None):
        self.name = name
        self.conference_makingOf_Task = conference_makingOf_Task if conference_makingOf_Task is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def conference_makingOf_Task(self):
        return self.__conference_makingOf_Task

    @conference_makingOf_Task.setter
    def conference_makingOf_Task(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_makingOf_Task__conference_makingOf_Task", None)
        self.__conference_makingOf_Task = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Participant35"):
                    opp_val = getattr(item, "Participant35", None)
                    
                    if opp_val == self:
                        setattr(item, "Participant35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Participant35"):
                    opp_val = getattr(item, "Participant35", None)
                    
                    setattr(item, "Participant35", self)
                    

class Day:

    pass
class conference_makingOf_Story:

    def __init__(self, name: str, conference_makingOf_Story: set["Day"] = None):
        self.name = name
        self.conference_makingOf_Story = conference_makingOf_Story if conference_makingOf_Story is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def conference_makingOf_Story(self):
        return self.__conference_makingOf_Story

    @conference_makingOf_Story.setter
    def conference_makingOf_Story(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_makingOf_Story__conference_makingOf_Story", None)
        self.__conference_makingOf_Story = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Day33"):
                    opp_val = getattr(item, "Day33", None)
                    
                    if opp_val == self:
                        setattr(item, "Day33", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Day33"):
                    opp_val = getattr(item, "Day33", None)
                    
                    setattr(item, "Day33", self)
                    

class conference_Subject:

    def __init__(self, description: str, isDone: bool, conference_Subject: "conference_Talk" = None):
        self.description = description
        self.isDone = isDone
        self.conference_Subject = conference_Subject
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def isDone(self):
        return self.__isDone

    @isDone.setter
    def isDone(self, isDone: bool):
        self.__isDone = isDone


    @property
    def conference_Subject(self):
        return self.__conference_Subject

    @conference_Subject.setter
    def conference_Subject(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Subject__conference_Subject", None)
        self.__conference_Subject = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conference_Talk"):
                opp_val = getattr(old_value, "conference_Talk", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conference_Talk"):
                opp_val = getattr(value, "conference_Talk", None)
                if opp_val is None:
                    setattr(value, "conference_Talk", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Task:

    pass
class conference_makingOf_Day:

    def __init__(self, name: str, conference_makingOf_Day: set["Task"] = None, conference_makingOf_Day31: set["Participant"] = None, conference_makingOf_Day28: set["Task"] = None):
        self.name = name
        self.conference_makingOf_Day = conference_makingOf_Day if conference_makingOf_Day is not None else set()
        self.conference_makingOf_Day31 = conference_makingOf_Day31 if conference_makingOf_Day31 is not None else set()
        self.conference_makingOf_Day28 = conference_makingOf_Day28 if conference_makingOf_Day28 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def conference_makingOf_Day28(self):
        return self.__conference_makingOf_Day28

    @conference_makingOf_Day28.setter
    def conference_makingOf_Day28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_makingOf_Day__conference_makingOf_Day28", None)
        self.__conference_makingOf_Day28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Task29"):
                    opp_val = getattr(item, "Task29", None)
                    
                    if opp_val == self:
                        setattr(item, "Task29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Task29"):
                    opp_val = getattr(item, "Task29", None)
                    
                    setattr(item, "Task29", self)
                    

    @property
    def conference_makingOf_Day(self):
        return self.__conference_makingOf_Day

    @conference_makingOf_Day.setter
    def conference_makingOf_Day(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_makingOf_Day__conference_makingOf_Day", None)
        self.__conference_makingOf_Day = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Task"):
                    opp_val = getattr(item, "Task", None)
                    
                    if opp_val == self:
                        setattr(item, "Task", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Task"):
                    opp_val = getattr(item, "Task", None)
                    
                    setattr(item, "Task", self)
                    

    @property
    def conference_makingOf_Day31(self):
        return self.__conference_makingOf_Day31

    @conference_makingOf_Day31.setter
    def conference_makingOf_Day31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_makingOf_Day__conference_makingOf_Day31", None)
        self.__conference_makingOf_Day31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Participant"):
                    opp_val = getattr(item, "Participant", None)
                    
                    if opp_val == self:
                        setattr(item, "Participant", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Participant"):
                    opp_val = getattr(item, "Participant", None)
                    
                    setattr(item, "Participant", self)
                    

class Story:

    pass
class conference_Talk:

    def __init__(self, time: str, name: str, abstract: str, duration: int, talks: set["conference_Person"] = None, conference_Talk: set["conference_Subject"] = None, conference_Talk10: set["Story"] = None, talks12: "conference_Day" = None, talks14: "conference_Location" = None, Talk: "conference_Person" = None, conference_Talk19: "conference_Track" = None, Talk23: "conference_Day" = None, Talk25: "conference_Location" = None):
        self.time = time
        self.name = name
        self.abstract = abstract
        self.duration = duration
        self.talks = talks if talks is not None else set()
        self.conference_Talk = conference_Talk if conference_Talk is not None else set()
        self.conference_Talk10 = conference_Talk10 if conference_Talk10 is not None else set()
        self.talks12 = talks12
        self.talks14 = talks14
        self.Talk = Talk
        self.conference_Talk19 = conference_Talk19
        self.Talk23 = Talk23
        self.Talk25 = Talk25
        
        pass
    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration


    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self, time: str):
        self.__time = time


    @property
    def abstract(self):
        return self.__abstract

    @abstract.setter
    def abstract(self, abstract: str):
        self.__abstract = abstract


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def talks(self):
        return self.__talks

    @talks.setter
    def talks(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Talk__talks", None)
        self.__talks = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person"):
                    opp_val = getattr(item, "Person", None)
                    
                    if opp_val == self:
                        setattr(item, "Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person"):
                    opp_val = getattr(item, "Person", None)
                    
                    setattr(item, "Person", self)
                    

    @property
    def talks14(self):
        return self.__talks14

    @talks14.setter
    def talks14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Talk__talks14", None)
        self.__talks14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Location"):
                opp_val = getattr(old_value, "Location", None)
                if opp_val == self:
                    setattr(old_value, "Location", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Location"):
                opp_val = getattr(value, "Location", None)
                setattr(value, "Location", self)

    @property
    def talks12(self):
        return self.__talks12

    @talks12.setter
    def talks12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Talk__talks12", None)
        self.__talks12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Day"):
                opp_val = getattr(old_value, "Day", None)
                if opp_val == self:
                    setattr(old_value, "Day", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Day"):
                opp_val = getattr(value, "Day", None)
                setattr(value, "Day", self)

    @property
    def Talk23(self):
        return self.__Talk23

    @Talk23.setter
    def Talk23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Talk__Talk23", None)
        self.__Talk23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "day"):
                opp_val = getattr(old_value, "day", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "day"):
                opp_val = getattr(value, "day", None)
                if opp_val is None:
                    setattr(value, "day", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def conference_Talk10(self):
        return self.__conference_Talk10

    @conference_Talk10.setter
    def conference_Talk10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Talk__conference_Talk10", None)
        self.__conference_Talk10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Story"):
                    opp_val = getattr(item, "Story", None)
                    
                    if opp_val == self:
                        setattr(item, "Story", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Story"):
                    opp_val = getattr(item, "Story", None)
                    
                    setattr(item, "Story", self)
                    

    @property
    def conference_Talk19(self):
        return self.__conference_Talk19

    @conference_Talk19.setter
    def conference_Talk19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Talk__conference_Talk19", None)
        self.__conference_Talk19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "conference_Track18"):
                opp_val = getattr(old_value, "conference_Track18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "conference_Track18"):
                opp_val = getattr(value, "conference_Track18", None)
                if opp_val is None:
                    setattr(value, "conference_Track18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Talk25(self):
        return self.__Talk25

    @Talk25.setter
    def Talk25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Talk__Talk25", None)
        self.__Talk25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "location"):
                opp_val = getattr(old_value, "location", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "location"):
                opp_val = getattr(value, "location", None)
                if opp_val is None:
                    setattr(value, "location", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Talk(self):
        return self.__Talk

    @Talk.setter
    def Talk(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Talk__Talk", None)
        self.__Talk = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "speakers"):
                opp_val = getattr(old_value, "speakers", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "speakers"):
                opp_val = getattr(value, "speakers", None)
                if opp_val is None:
                    setattr(value, "speakers", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def conference_Talk(self):
        return self.__conference_Talk

    @conference_Talk.setter
    def conference_Talk(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Talk__conference_Talk", None)
        self.__conference_Talk = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "conference_Subject"):
                    opp_val = getattr(item, "conference_Subject", None)
                    
                    if opp_val == self:
                        setattr(item, "conference_Subject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "conference_Subject"):
                    opp_val = getattr(item, "conference_Subject", None)
                    
                    setattr(item, "conference_Subject", self)
                    

class conference_Location:

    def __init__(self, name: str, conference_Location: "conference_Conference" = None, Location: "conference_Talk" = None, location: set["conference_Talk"] = None):
        self.name = name
        self.conference_Location = conference_Location
        self.Location = Location
        self.location = location if location is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Location__location", None)
        self.__location = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Talk25"):
                    opp_val = getattr(item, "Talk25", None)
                    
                    if opp_val == self:
                        setattr(item, "Talk25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Talk25"):
                    opp_val = getattr(item, "Talk25", None)
                    
                    setattr(item, "Talk25", self)
                    

    @property
    def Location(self):
        return self.__Location

    @Location.setter
    def Location(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Location__Location", None)
        self.__Location = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "talks14"):
                opp_val = getattr(old_value, "talks14", None)
                if opp_val == self:
                    setattr(old_value, "talks14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "talks14"):
                opp_val = getattr(value, "talks14", None)
                setattr(value, "talks14", self)

    @property
    def conference_Location(self):
        return self.__conference_Location

    @conference_Location.setter
    def conference_Location(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Location__conference_Location", None)
        self.__conference_Location = value
        
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

class conference_Day:

    def __init__(self, name: str, conference_Day: "conference_Conference" = None, Day: "conference_Talk" = None, day: set["conference_Talk"] = None):
        self.name = name
        self.conference_Day = conference_Day
        self.Day = Day
        self.day = day if day is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def Day(self):
        return self.__Day

    @Day.setter
    def Day(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Day__Day", None)
        self.__Day = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "talks12"):
                opp_val = getattr(old_value, "talks12", None)
                if opp_val == self:
                    setattr(old_value, "talks12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "talks12"):
                opp_val = getattr(value, "talks12", None)
                setattr(value, "talks12", self)

    @property
    def conference_Day(self):
        return self.__conference_Day

    @conference_Day.setter
    def conference_Day(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Day__conference_Day", None)
        self.__conference_Day = value
        
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
    def day(self):
        return self.__day

    @day.setter
    def day(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Day__day", None)
        self.__day = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Talk23"):
                    opp_val = getattr(item, "Talk23", None)
                    
                    if opp_val == self:
                        setattr(item, "Talk23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Talk23"):
                    opp_val = getattr(item, "Talk23", None)
                    
                    setattr(item, "Talk23", self)
                    

class conference_Person:

    def __init__(self, name: str, organisation: str, conference_Person: "conference_Conference" = None, Person: "conference_Talk" = None, speakers: set["conference_Talk"] = None, animators: set["conference_Track"] = None, Person21: "conference_Track" = None):
        self.name = name
        self.organisation = organisation
        self.conference_Person = conference_Person
        self.Person = Person
        self.speakers = speakers if speakers is not None else set()
        self.animators = animators if animators is not None else set()
        self.Person21 = Person21
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def organisation(self):
        return self.__organisation

    @organisation.setter
    def organisation(self, organisation: str):
        self.__organisation = organisation


    @property
    def speakers(self):
        return self.__speakers

    @speakers.setter
    def speakers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Person__speakers", None)
        self.__speakers = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Talk"):
                    opp_val = getattr(item, "Talk", None)
                    
                    if opp_val == self:
                        setattr(item, "Talk", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Talk"):
                    opp_val = getattr(item, "Talk", None)
                    
                    setattr(item, "Talk", self)
                    

    @property
    def animators(self):
        return self.__animators

    @animators.setter
    def animators(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Person__animators", None)
        self.__animators = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Track"):
                    opp_val = getattr(item, "Track", None)
                    
                    if opp_val == self:
                        setattr(item, "Track", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Track"):
                    opp_val = getattr(item, "Track", None)
                    
                    setattr(item, "Track", self)
                    

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
    def Person21(self):
        return self.__Person21

    @Person21.setter
    def Person21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Person__Person21", None)
        self.__Person21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tracks"):
                opp_val = getattr(old_value, "tracks", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tracks"):
                opp_val = getattr(value, "tracks", None)
                if opp_val is None:
                    setattr(value, "tracks", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Person(self):
        return self.__Person

    @Person.setter
    def Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Person__Person", None)
        self.__Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "talks"):
                opp_val = getattr(old_value, "talks", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "talks"):
                opp_val = getattr(value, "talks", None)
                if opp_val is None:
                    setattr(value, "talks", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class conference_Track:

    def __init__(self, name: str, conference_Track: "conference_Conference" = None, Track: "conference_Person" = None, conference_Track18: set["conference_Talk"] = None, tracks: set["conference_Person"] = None):
        self.name = name
        self.conference_Track = conference_Track
        self.Track = Track
        self.conference_Track18 = conference_Track18 if conference_Track18 is not None else set()
        self.tracks = tracks if tracks is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def conference_Track(self):
        return self.__conference_Track

    @conference_Track.setter
    def conference_Track(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Track__conference_Track", None)
        self.__conference_Track = value
        
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
    def Track(self):
        return self.__Track

    @Track.setter
    def Track(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Track__Track", None)
        self.__Track = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "animators"):
                opp_val = getattr(old_value, "animators", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "animators"):
                opp_val = getattr(value, "animators", None)
                if opp_val is None:
                    setattr(value, "animators", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tracks(self):
        return self.__tracks

    @tracks.setter
    def tracks(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Track__tracks", None)
        self.__tracks = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person21"):
                    opp_val = getattr(item, "Person21", None)
                    
                    if opp_val == self:
                        setattr(item, "Person21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person21"):
                    opp_val = getattr(item, "Person21", None)
                    
                    setattr(item, "Person21", self)
                    

    @property
    def conference_Track18(self):
        return self.__conference_Track18

    @conference_Track18.setter
    def conference_Track18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_conference_Track__conference_Track18", None)
        self.__conference_Track18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "conference_Talk19"):
                    opp_val = getattr(item, "conference_Talk19", None)
                    
                    if opp_val == self:
                        setattr(item, "conference_Talk19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "conference_Talk19"):
                    opp_val = getattr(item, "conference_Talk19", None)
                    
                    setattr(item, "conference_Talk19", self)
                    

class conference_Conference:

    def __init__(self, name: str, conference_Conference: set["conference_Track"] = None, conference_Conference2: set["conference_Person"] = None, conference_Conference4: set["conference_Day"] = None, conference_Conference6: set["conference_Location"] = None):
        self.name = name
        self.conference_Conference = conference_Conference if conference_Conference is not None else set()
        self.conference_Conference2 = conference_Conference2 if conference_Conference2 is not None else set()
        self.conference_Conference4 = conference_Conference4 if conference_Conference4 is not None else set()
        self.conference_Conference6 = conference_Conference6 if conference_Conference6 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


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
                if hasattr(item, "conference_Track"):
                    opp_val = getattr(item, "conference_Track", None)
                    
                    if opp_val == self:
                        setattr(item, "conference_Track", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "conference_Track"):
                    opp_val = getattr(item, "conference_Track", None)
                    
                    setattr(item, "conference_Track", self)
                    

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
                if hasattr(item, "conference_Day"):
                    opp_val = getattr(item, "conference_Day", None)
                    
                    if opp_val == self:
                        setattr(item, "conference_Day", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "conference_Day"):
                    opp_val = getattr(item, "conference_Day", None)
                    
                    setattr(item, "conference_Day", self)
                    

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
                if hasattr(item, "conference_Location"):
                    opp_val = getattr(item, "conference_Location", None)
                    
                    if opp_val == self:
                        setattr(item, "conference_Location", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "conference_Location"):
                    opp_val = getattr(item, "conference_Location", None)
                    
                    setattr(item, "conference_Location", self)
                    
