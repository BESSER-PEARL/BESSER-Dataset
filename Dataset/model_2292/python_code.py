from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Building(Enum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"
    H = "H"
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


############################################
# Definition of Classes
############################################

class universityextended_administration_Event:

    def __init__(self, title: str, universityextended_administration_Event: "Time" = None, universityextended_administration_Event31: "Room" = None):
        self.title = title
        self.universityextended_administration_Event = universityextended_administration_Event
        self.universityextended_administration_Event31 = universityextended_administration_Event31
        
        pass
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def universityextended_administration_Event31(self):
        return self.__universityextended_administration_Event31

    @universityextended_administration_Event31.setter
    def universityextended_administration_Event31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_universityextended_administration_Event__universityextended_administration_Event31", None)
        self.__universityextended_administration_Event31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Room32"):
                opp_val = getattr(old_value, "Room32", None)
                if opp_val == self:
                    setattr(old_value, "Room32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Room32"):
                opp_val = getattr(value, "Room32", None)
                setattr(value, "Room32", self)

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
            if hasattr(old_value, "Time29"):
                opp_val = getattr(old_value, "Time29", None)
                if opp_val == self:
                    setattr(old_value, "Time29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Time29"):
                opp_val = getattr(value, "Time29", None)
                setattr(value, "Time29", self)

class universityextended_administration_Time:

    def __init__(self, day: str, startHour: int, endHour: int):
        self.day = day
        self.startHour = startHour
        self.endHour = endHour
        
        pass
    @property
    def endHour(self):
        return self.__endHour

    @endHour.setter
    def endHour(self, endHour: int):
        self.__endHour = endHour


    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day: str):
        self.__day = day


    @property
    def startHour(self):
        return self.__startHour

    @startHour.setter
    def startHour(self, startHour: int):
        self.__startHour = startHour


class universityextended_administration_Room:

    def __init__(self, building: str, floor: int, roomnumber: int):
        self.building = building
        self.floor = floor
        self.roomnumber = roomnumber
        
        pass
    @property
    def building(self):
        return self.__building

    @building.setter
    def building(self, building: str):
        self.__building = building


    @property
    def floor(self):
        return self.__floor

    @floor.setter
    def floor(self, floor: int):
        self.__floor = floor


    @property
    def roomnumber(self):
        return self.__roomnumber

    @roomnumber.setter
    def roomnumber(self, roomnumber: int):
        self.__roomnumber = roomnumber


class Assistant:

    pass
class Professor:

    pass
class Event:

    pass
class universityextended_administration_Tutorial(Event):

    pass
class universityextended_administration_Lecture(Event):

    def __init__(self, captions: str, lecture: "Course" = None, lectures: "Professor" = None):
        self.captions = captions
        self.lecture = lecture
        self.lectures = lectures
        
        pass
    @property
    def captions(self):
        return self.__captions

    @captions.setter
    def captions(self, captions: str):
        self.__captions = captions


    @property
    def lecture(self):
        return self.__lecture

    @lecture.setter
    def lecture(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_universityextended_administration_Lecture__lecture", None)
        self.__lecture = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Course22"):
                opp_val = getattr(old_value, "Course22", None)
                if opp_val == self:
                    setattr(old_value, "Course22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Course22"):
                opp_val = getattr(value, "Course22", None)
                setattr(value, "Course22", self)

    @property
    def lectures(self):
        return self.__lectures

    @lectures.setter
    def lectures(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_universityextended_administration_Lecture__lectures", None)
        self.__lectures = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Professor"):
                opp_val = getattr(old_value, "Professor", None)
                if opp_val == self:
                    setattr(old_value, "Professor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Professor"):
                opp_val = getattr(value, "Professor", None)
                setattr(value, "Professor", self)

class Student:

    pass
class universityextended_connection_Visits:

    def __init__(self, motivation: str, visitor: "Course" = None, courseVisit: "Student" = None):
        self.motivation = motivation
        self.visitor = visitor
        self.courseVisit = courseVisit
        
        pass
    @property
    def motivation(self):
        return self.__motivation

    @motivation.setter
    def motivation(self, motivation: str):
        self.__motivation = motivation


    @property
    def courseVisit(self):
        return self.__courseVisit

    @courseVisit.setter
    def courseVisit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_universityextended_connection_Visits__courseVisit", None)
        self.__courseVisit = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Student"):
                opp_val = getattr(old_value, "Student", None)
                if opp_val == self:
                    setattr(old_value, "Student", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Student"):
                opp_val = getattr(value, "Student", None)
                setattr(value, "Student", self)

    @property
    def visitor(self):
        return self.__visitor

    @visitor.setter
    def visitor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_universityextended_connection_Visits__visitor", None)
        self.__visitor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Course34"):
                opp_val = getattr(old_value, "Course34", None)
                if opp_val == self:
                    setattr(old_value, "Course34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Course34"):
                opp_val = getattr(value, "Course34", None)
                setattr(value, "Course34", self)

class universityextended_people_Person:

    def __init__(self, name: str):
        self.name = name
        
        pass
    @property
    def name(self):
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

    def __init__(self, matriculationnumber: str, student: set["Visits"] = None, Person: "universityextended_University" = None):
        self.matriculationnumber = matriculationnumber
        self.student = student if student is not None else set()
        
        pass
    @property
    def matriculationnumber(self):
        return self.__matriculationnumber

    @matriculationnumber.setter
    def matriculationnumber(self, matriculationnumber: str):
        self.__matriculationnumber = matriculationnumber


    @property
    def student(self):
        return self.__student

    @student.setter
    def student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_universityextended_people_Student__student", None)
        self.__student = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Visits10"):
                    opp_val = getattr(item, "Visits10", None)
                    
                    if opp_val == self:
                        setattr(item, "Visits10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Visits10"):
                    opp_val = getattr(item, "Visits10", None)
                    
                    setattr(item, "Visits10", self)
                    

class universityextended_people_Professor(Person):

    def __init__(self, rank: str, lecturer: set["Lecture"] = None, Person: "universityextended_University" = None):
        self.rank = rank
        self.lecturer = lecturer if lecturer is not None else set()
        
        pass
    @property
    def rank(self):
        return self.__rank

    @rank.setter
    def rank(self, rank: str):
        self.__rank = rank


    @property
    def lecturer(self):
        return self.__lecturer

    @lecturer.setter
    def lecturer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_universityextended_people_Professor__lecturer", None)
        self.__lecturer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Lecture"):
                    opp_val = getattr(item, "Lecture", None)
                    
                    if opp_val == self:
                        setattr(item, "Lecture", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Lecture"):
                    opp_val = getattr(item, "Lecture", None)
                    
                    setattr(item, "Lecture", self)
                    

class universityextended_University:

    pass
class universityextended_administration_Course:

    def __init__(self, title: str, startOfCourse: date, endOfCourse: date, course: "Lecture" = None, course16: "Tutorial" = None, course19: set["Visits"] = None):
        self.title = title
        self.startOfCourse = startOfCourse
        self.endOfCourse = endOfCourse
        self.course = course
        self.course16 = course16
        self.course19 = course19 if course19 is not None else set()
        
        pass
    @property
    def startOfCourse(self):
        return self.__startOfCourse

    @startOfCourse.setter
    def startOfCourse(self, startOfCourse: date):
        self.__startOfCourse = startOfCourse


    @property
    def endOfCourse(self):
        return self.__endOfCourse

    @endOfCourse.setter
    def endOfCourse(self, endOfCourse: date):
        self.__endOfCourse = endOfCourse


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def course16(self):
        return self.__course16

    @course16.setter
    def course16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_universityextended_administration_Course__course16", None)
        self.__course16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Tutorial17"):
                opp_val = getattr(old_value, "Tutorial17", None)
                if opp_val == self:
                    setattr(old_value, "Tutorial17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Tutorial17"):
                opp_val = getattr(value, "Tutorial17", None)
                setattr(value, "Tutorial17", self)

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_universityextended_administration_Course__course", None)
        self.__course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Lecture14"):
                opp_val = getattr(old_value, "Lecture14", None)
                if opp_val == self:
                    setattr(old_value, "Lecture14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Lecture14"):
                opp_val = getattr(value, "Lecture14", None)
                setattr(value, "Lecture14", self)

    @property
    def course19(self):
        return self.__course19

    @course19.setter
    def course19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_universityextended_administration_Course__course19", None)
        self.__course19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Visits20"):
                    opp_val = getattr(item, "Visits20", None)
                    
                    if opp_val == self:
                        setattr(item, "Visits20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Visits20"):
                    opp_val = getattr(item, "Visits20", None)
                    
                    setattr(item, "Visits20", self)
                    

class Tutorial:

    pass
class universityextended_people_Assistant(Person):

    def __init__(self, isDoctoralCandidate: bool, tutor: set["Tutorial"] = None, Person: "universityextended_University" = None):
        self.isDoctoralCandidate = isDoctoralCandidate
        self.tutor = tutor if tutor is not None else set()
        
        pass
    @property
    def isDoctoralCandidate(self):
        return self.__isDoctoralCandidate

    @isDoctoralCandidate.setter
    def isDoctoralCandidate(self, isDoctoralCandidate: bool):
        self.__isDoctoralCandidate = isDoctoralCandidate


    @property
    def tutor(self):
        return self.__tutor

    @tutor.setter
    def tutor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_universityextended_people_Assistant__tutor", None)
        self.__tutor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Tutorial"):
                    opp_val = getattr(item, "Tutorial", None)
                    
                    if opp_val == self:
                        setattr(item, "Tutorial", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Tutorial"):
                    opp_val = getattr(item, "Tutorial", None)
                    
                    setattr(item, "Tutorial", self)
                    

class Lecture:

    pass