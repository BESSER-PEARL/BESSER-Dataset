from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Motivation(Enum):
    HIGH_INTEREST = "HIGH_INTEREST"
    AVERAGE_INTEREST = "AVERAGE_INTEREST"
    LOW_INTEREST = "LOW_INTEREST"
class DayOfWeek(Enum):
    Monday = "Monday"
    Tuesday = "Tuesday"
    Wednesday = "Wednesday"
    Thursday = "Thursday"
    Friday = "Friday"
class SalaryRank(Enum):
    W1 = "W1"
    W2 = "W2"
    W3 = "W3"
class Building(Enum):
    H = "H"
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"


############################################
# Definition of Classes
############################################

class Student:

    pass
class universityextended_connection_Visits:

    def __init__(self, motivation: str, Course38: "Course" = None, Student: "Student" = None):
        self.motivation = motivation
        self.Course38 = Course38
        self.Student = Student
        
    @property
    def motivation(self) -> str:
        return self.__motivation

    @motivation.setter
    def motivation(self, motivation: str):
        self.__motivation = motivation

    @property
    def Course38(self):
        return self.__Course38

    @Course38.setter
    def Course38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_universityextended_connection_Visits__Course38", None)
        self.__Course38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "administration39"):
                opp_val = getattr(old_value, "administration39", None)
                if opp_val == self:
                    setattr(old_value, "administration39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "administration39"):
                opp_val = getattr(value, "administration39", None)
                setattr(value, "administration39", self)

    @property
    def Student(self):
        return self.__Student

    @Student.setter
    def Student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_universityextended_connection_Visits__Student", None)
        self.__Student = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "people41"):
                opp_val = getattr(old_value, "people41", None)
                if opp_val == self:
                    setattr(old_value, "people41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "people41"):
                opp_val = getattr(value, "people41", None)
                setattr(value, "people41", self)

class universityextended_administration_Event:

    def __init__(self, title: str, universityextended_administration_Event: "Time" = None, universityextended_administration_Event35: "Room" = None):
        self.title = title
        self.universityextended_administration_Event = universityextended_administration_Event
        self.universityextended_administration_Event35 = universityextended_administration_Event35
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def universityextended_administration_Event(self):
        return self.__universityextended_administration_Event

    @universityextended_administration_Event.setter
    def universityextended_administration_Event(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_universityextended_administration_Event__universityextended_administration_Event", None)
        self.__universityextended_administration_Event = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Time33"):
                opp_val = getattr(old_value, "Time33", None)
                if opp_val == self:
                    setattr(old_value, "Time33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Time33"):
                opp_val = getattr(value, "Time33", None)
                setattr(value, "Time33", self)

    @property
    def universityextended_administration_Event35(self):
        return self.__universityextended_administration_Event35

    @universityextended_administration_Event35.setter
    def universityextended_administration_Event35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_universityextended_administration_Event__universityextended_administration_Event35", None)
        self.__universityextended_administration_Event35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Room36"):
                opp_val = getattr(old_value, "Room36", None)
                if opp_val == self:
                    setattr(old_value, "Room36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Room36"):
                opp_val = getattr(value, "Room36", None)
                setattr(value, "Room36", self)

class universityextended_administration_Time:

    def __init__(self, day: str, startHour: int, endHour: int):
        self.day = day
        self.startHour = startHour
        self.endHour = endHour
        
    @property
    def startHour(self) -> int:
        return self.__startHour

    @startHour.setter
    def startHour(self, startHour: int):
        self.__startHour = startHour

    @property
    def day(self) -> str:
        return self.__day

    @day.setter
    def day(self, day: str):
        self.__day = day

    @property
    def endHour(self) -> int:
        return self.__endHour

    @endHour.setter
    def endHour(self, endHour: int):
        self.__endHour = endHour

class Assistant:

    pass
class Professor:

    pass
class Event:

    pass
class universityextended_administration_Tutorial(Event):

    pass
class universityextended_administration_Lecture(Event):

    def __init__(self, captions: str, Course24: "Course" = None, Professor: "Professor" = None):
        self.captions = captions
        self.Course24 = Course24
        self.Professor = Professor
        
    @property
    def captions(self) -> str:
        return self.__captions

    @captions.setter
    def captions(self, captions: str):
        self.__captions = captions

    @property
    def Professor(self):
        return self.__Professor

    @Professor.setter
    def Professor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_universityextended_administration_Lecture__Professor", None)
        self.__Professor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "people"):
                opp_val = getattr(old_value, "people", None)
                if opp_val == self:
                    setattr(old_value, "people", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "people"):
                opp_val = getattr(value, "people", None)
                setattr(value, "people", self)

    @property
    def Course24(self):
        return self.__Course24

    @Course24.setter
    def Course24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_universityextended_administration_Lecture__Course24", None)
        self.__Course24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "administration25"):
                opp_val = getattr(old_value, "administration25", None)
                if opp_val == self:
                    setattr(old_value, "administration25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "administration25"):
                opp_val = getattr(value, "administration25", None)
                setattr(value, "administration25", self)

class universityextended_administration_Course:

    def __init__(self, title: str, startOfCourse: date, endOfCourse: date, Lecture15: "Lecture" = None, Tutorial18: "Tutorial" = None, Visits21: set["Visits"] = None):
        self.title = title
        self.startOfCourse = startOfCourse
        self.endOfCourse = endOfCourse
        self.Lecture15 = Lecture15
        self.Tutorial18 = Tutorial18
        self.Visits21 = Visits21 if Visits21 is not None else set()
        
    @property
    def endOfCourse(self) -> date:
        return self.__endOfCourse

    @endOfCourse.setter
    def endOfCourse(self, endOfCourse: date):
        self.__endOfCourse = endOfCourse

    @property
    def startOfCourse(self) -> date:
        return self.__startOfCourse

    @startOfCourse.setter
    def startOfCourse(self, startOfCourse: date):
        self.__startOfCourse = startOfCourse

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def Visits21(self):
        return self.__Visits21

    @Visits21.setter
    def Visits21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_universityextended_administration_Course__Visits21", None)
        self.__Visits21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "connection22"):
                    opp_val = getattr(item, "connection22", None)
                    
                    if opp_val == self:
                        setattr(item, "connection22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "connection22"):
                    opp_val = getattr(item, "connection22", None)
                    
                    setattr(item, "connection22", self)
                    

    @property
    def Tutorial18(self):
        return self.__Tutorial18

    @Tutorial18.setter
    def Tutorial18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_universityextended_administration_Course__Tutorial18", None)
        self.__Tutorial18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "administration19"):
                opp_val = getattr(old_value, "administration19", None)
                if opp_val == self:
                    setattr(old_value, "administration19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "administration19"):
                opp_val = getattr(value, "administration19", None)
                setattr(value, "administration19", self)

    @property
    def Lecture15(self):
        return self.__Lecture15

    @Lecture15.setter
    def Lecture15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_universityextended_administration_Course__Lecture15", None)
        self.__Lecture15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "administration16"):
                opp_val = getattr(old_value, "administration16", None)
                if opp_val == self:
                    setattr(old_value, "administration16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "administration16"):
                opp_val = getattr(value, "administration16", None)
                setattr(value, "administration16", self)

class Tutorial:

    pass
class universityextended_administration_Room:

    def __init__(self, building: str, floor: int, roomnumber: int):
        self.building = building
        self.floor = floor
        self.roomnumber = roomnumber
        
    @property
    def floor(self) -> int:
        return self.__floor

    @floor.setter
    def floor(self, floor: int):
        self.__floor = floor

    @property
    def roomnumber(self) -> int:
        return self.__roomnumber

    @roomnumber.setter
    def roomnumber(self, roomnumber: int):
        self.__roomnumber = roomnumber

    @property
    def building(self) -> str:
        return self.__building

    @building.setter
    def building(self, building: str):
        self.__building = building

class universityextended_people_Person:

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class Room:

    pass
class Time:

    pass
class Course:

    pass
class Visits:

    pass
class Person:

    pass
class universityextended_people_Student(Person):

    def __init__(self, matriculationnumber: str, Visits10: set["Visits"] = None, Person: "universityextended_University"):
        self.matriculationnumber = matriculationnumber
        self.Visits10 = Visits10 if Visits10 is not None else set()
        
    @property
    def matriculationnumber(self) -> str:
        return self.__matriculationnumber

    @matriculationnumber.setter
    def matriculationnumber(self, matriculationnumber: str):
        self.__matriculationnumber = matriculationnumber

    @property
    def Visits10(self):
        return self.__Visits10

    @Visits10.setter
    def Visits10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_universityextended_people_Student__Visits10", None)
        self.__Visits10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "connection"):
                    opp_val = getattr(item, "connection", None)
                    
                    if opp_val == self:
                        setattr(item, "connection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "connection"):
                    opp_val = getattr(item, "connection", None)
                    
                    setattr(item, "connection", self)
                    

class universityextended_people_Assistant(Person):

    def __init__(self, isDoctoralCandidate: bool, Tutorial: set["Tutorial"] = None, Person: "universityextended_University"):
        self.isDoctoralCandidate = isDoctoralCandidate
        self.Tutorial = Tutorial if Tutorial is not None else set()
        
    @property
    def isDoctoralCandidate(self) -> bool:
        return self.__isDoctoralCandidate

    @isDoctoralCandidate.setter
    def isDoctoralCandidate(self, isDoctoralCandidate: bool):
        self.__isDoctoralCandidate = isDoctoralCandidate

    @property
    def Tutorial(self):
        return self.__Tutorial

    @Tutorial.setter
    def Tutorial(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_universityextended_people_Assistant__Tutorial", None)
        self.__Tutorial = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "administration13"):
                    opp_val = getattr(item, "administration13", None)
                    
                    if opp_val == self:
                        setattr(item, "administration13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "administration13"):
                    opp_val = getattr(item, "administration13", None)
                    
                    setattr(item, "administration13", self)
                    

class universityextended_University:

    pass
class Lecture:

    pass
class universityextended_people_Professor(Person):

    def __init__(self, rank: str, Lecture: set["Lecture"] = None, Person: "universityextended_University"):
        self.rank = rank
        self.Lecture = Lecture if Lecture is not None else set()
        
    @property
    def rank(self) -> str:
        return self.__rank

    @rank.setter
    def rank(self, rank: str):
        self.__rank = rank

    @property
    def Lecture(self):
        return self.__Lecture

    @Lecture.setter
    def Lecture(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_universityextended_people_Professor__Lecture", None)
        self.__Lecture = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "administration"):
                    opp_val = getattr(item, "administration", None)
                    
                    if opp_val == self:
                        setattr(item, "administration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "administration"):
                    opp_val = getattr(item, "administration", None)
                    
                    setattr(item, "administration", self)
                    
