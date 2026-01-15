from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class StaffMemberType(Enum):
    ResearchStudent = "ResearchStudent"
    Other = "Other"
    Academic = "Academic"
    Research = "Research"
    Technical = "Technical"
    Admin = "Admin"
    Honary = "Honary"


############################################
# Definition of Classes
############################################

class university_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class university_PrimitiveType:

    def __init__(self, a: str, b: int, c: str, bigIntList: str, d: bool, e: str, f: float, g: str, h: str, i: float, j: str, k: str, l: str, m: str, n: str, o: str, p: str):
        self.a = a
        self.b = b
        self.c = c
        self.bigIntList = bigIntList
        self.d = d
        self.e = e
        self.f = f
        self.g = g
        self.h = h
        self.i = i
        self.j = j
        self.k = k
        self.l = l
        self.m = m
        self.n = n
        self.o = o
        self.p = p
        
    @property
    def h(self) -> str:
        return self.__h

    @h.setter
    def h(self, h: str):
        self.__h = h

    @property
    def a(self) -> str:
        return self.__a

    @a.setter
    def a(self, a: str):
        self.__a = a

    @property
    def k(self) -> str:
        return self.__k

    @k.setter
    def k(self, k: str):
        self.__k = k

    @property
    def e(self) -> str:
        return self.__e

    @e.setter
    def e(self, e: str):
        self.__e = e

    @property
    def c(self) -> str:
        return self.__c

    @c.setter
    def c(self, c: str):
        self.__c = c

    @property
    def i(self) -> float:
        return self.__i

    @i.setter
    def i(self, i: float):
        self.__i = i

    @property
    def j(self) -> str:
        return self.__j

    @j.setter
    def j(self, j: str):
        self.__j = j

    @property
    def m(self) -> str:
        return self.__m

    @m.setter
    def m(self, m: str):
        self.__m = m

    @property
    def l(self) -> str:
        return self.__l

    @l.setter
    def l(self, l: str):
        self.__l = l

    @property
    def b(self) -> int:
        return self.__b

    @b.setter
    def b(self, b: int):
        self.__b = b

    @property
    def f(self) -> float:
        return self.__f

    @f.setter
    def f(self, f: float):
        self.__f = f

    @property
    def o(self) -> str:
        return self.__o

    @o.setter
    def o(self, o: str):
        self.__o = o

    @property
    def d(self) -> bool:
        return self.__d

    @d.setter
    def d(self, d: bool):
        self.__d = d

    @property
    def g(self) -> str:
        return self.__g

    @g.setter
    def g(self, g: str):
        self.__g = g

    @property
    def n(self) -> str:
        return self.__n

    @n.setter
    def n(self, n: str):
        self.__n = n

    @property
    def bigIntList(self) -> str:
        return self.__bigIntList

    @bigIntList.setter
    def bigIntList(self, bigIntList: str):
        self.__bigIntList = bigIntList

    @property
    def p(self) -> str:
        return self.__p

    @p.setter
    def p(self, p: str):
        self.__p = p

class NamedElement:

    pass
class university_Library(NamedElement):

    pass
class university_Department(NamedElement):

    pass
class university_University(NamedElement):

    pass
class university_Book(NamedElement):

    def __init__(self, ISBN: str, authorNames: str, university_Book: "university_Library" = None):
        self.ISBN = ISBN
        self.authorNames = authorNames
        self.university_Book = university_Book
        
    @property
    def authorNames(self) -> str:
        return self.__authorNames

    @authorNames.setter
    def authorNames(self, authorNames: str):
        self.__authorNames = authorNames

    @property
    def ISBN(self) -> str:
        return self.__ISBN

    @ISBN.setter
    def ISBN(self, ISBN: str):
        self.__ISBN = ISBN

    @property
    def university_Book(self):
        return self.__university_Book

    @university_Book.setter
    def university_Book(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Book__university_Book", None)
        self.__university_Book = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "university_Library10"):
                opp_val = getattr(old_value, "university_Library10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "university_Library10"):
                opp_val = getattr(value, "university_Library10", None)
                if opp_val is None:
                    setattr(value, "university_Library10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class university_Computer(NamedElement):

    pass
class university_Vehicle:

    def __init__(self, registrationNumber: str, university_Vehicle: "university_Student" = None, university_Vehicle18: "university_StaffMember" = None, university_Vehicle13: "university_Library" = None):
        self.registrationNumber = registrationNumber
        self.university_Vehicle = university_Vehicle
        self.university_Vehicle18 = university_Vehicle18
        self.university_Vehicle13 = university_Vehicle13
        
    @property
    def registrationNumber(self) -> str:
        return self.__registrationNumber

    @registrationNumber.setter
    def registrationNumber(self, registrationNumber: str):
        self.__registrationNumber = registrationNumber

    @property
    def university_Vehicle(self):
        return self.__university_Vehicle

    @university_Vehicle.setter
    def university_Vehicle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Vehicle__university_Vehicle", None)
        self.__university_Vehicle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "university_Student"):
                opp_val = getattr(old_value, "university_Student", None)
                if opp_val == self:
                    setattr(old_value, "university_Student", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "university_Student"):
                opp_val = getattr(value, "university_Student", None)
                setattr(value, "university_Student", self)

    @property
    def university_Vehicle18(self):
        return self.__university_Vehicle18

    @university_Vehicle18.setter
    def university_Vehicle18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Vehicle__university_Vehicle18", None)
        self.__university_Vehicle18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "university_StaffMember17"):
                opp_val = getattr(old_value, "university_StaffMember17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "university_StaffMember17"):
                opp_val = getattr(value, "university_StaffMember17", None)
                if opp_val is None:
                    setattr(value, "university_StaffMember17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def university_Vehicle13(self):
        return self.__university_Vehicle13

    @university_Vehicle13.setter
    def university_Vehicle13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Vehicle__university_Vehicle13", None)
        self.__university_Vehicle13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "university_Library12"):
                opp_val = getattr(old_value, "university_Library12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "university_Library12"):
                opp_val = getattr(value, "university_Library12", None)
                if opp_val is None:
                    setattr(value, "university_Library12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class university_Module(NamedElement):

    pass
class university_Student(NamedElement):

    def __init__(self, studentId: float, enrolledStudents: set["university_Module"] = None, university_Student: "university_Vehicle" = None, university_Student24: "university_Department" = None, Student: "university_Module" = None):
        self.studentId = studentId
        self.enrolledStudents = enrolledStudents if enrolledStudents is not None else set()
        self.university_Student = university_Student
        self.university_Student24 = university_Student24
        self.Student = Student
        
    @property
    def studentId(self) -> float:
        return self.__studentId

    @studentId.setter
    def studentId(self, studentId: float):
        self.__studentId = studentId

    @property
    def university_Student24(self):
        return self.__university_Student24

    @university_Student24.setter
    def university_Student24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Student__university_Student24", None)
        self.__university_Student24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "university_Department23"):
                opp_val = getattr(old_value, "university_Department23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "university_Department23"):
                opp_val = getattr(value, "university_Department23", None)
                if opp_val is None:
                    setattr(value, "university_Department23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def university_Student(self):
        return self.__university_Student

    @university_Student.setter
    def university_Student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Student__university_Student", None)
        self.__university_Student = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "university_Vehicle"):
                opp_val = getattr(old_value, "university_Vehicle", None)
                if opp_val == self:
                    setattr(old_value, "university_Vehicle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "university_Vehicle"):
                opp_val = getattr(value, "university_Vehicle", None)
                setattr(value, "university_Vehicle", self)

    @property
    def enrolledStudents(self):
        return self.__enrolledStudents

    @enrolledStudents.setter
    def enrolledStudents(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Student__enrolledStudents", None)
        self.__enrolledStudents = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Module"):
                    opp_val = getattr(item, "Module", None)
                    
                    if opp_val == self:
                        setattr(item, "Module", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Module"):
                    opp_val = getattr(item, "Module", None)
                    
                    setattr(item, "Module", self)
                    

    @property
    def Student(self):
        return self.__Student

    @Student.setter
    def Student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Student__Student", None)
        self.__Student = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "enrolledModules"):
                opp_val = getattr(old_value, "enrolledModules", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "enrolledModules"):
                opp_val = getattr(value, "enrolledModules", None)
                if opp_val is None:
                    setattr(value, "enrolledModules", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class university_StaffMember(NamedElement):

    def __init__(self, staffMemberType: str, university_StaffMember: "university_University" = None, moduleLecturers: set["university_Module"] = None, university_StaffMember17: set["university_Vehicle"] = None, university_StaffMember21: "university_Department" = None, StaffMember: "university_Module" = None):
        self.staffMemberType = staffMemberType
        self.university_StaffMember = university_StaffMember
        self.moduleLecturers = moduleLecturers if moduleLecturers is not None else set()
        self.university_StaffMember17 = university_StaffMember17 if university_StaffMember17 is not None else set()
        self.university_StaffMember21 = university_StaffMember21
        self.StaffMember = StaffMember
        
    @property
    def staffMemberType(self) -> str:
        return self.__staffMemberType

    @staffMemberType.setter
    def staffMemberType(self, staffMemberType: str):
        self.__staffMemberType = staffMemberType

    @property
    def university_StaffMember(self):
        return self.__university_StaffMember

    @university_StaffMember.setter
    def university_StaffMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_StaffMember__university_StaffMember", None)
        self.__university_StaffMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "university_University4"):
                opp_val = getattr(old_value, "university_University4", None)
                if opp_val == self:
                    setattr(old_value, "university_University4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "university_University4"):
                opp_val = getattr(value, "university_University4", None)
                setattr(value, "university_University4", self)

    @property
    def university_StaffMember21(self):
        return self.__university_StaffMember21

    @university_StaffMember21.setter
    def university_StaffMember21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_StaffMember__university_StaffMember21", None)
        self.__university_StaffMember21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "university_Department20"):
                opp_val = getattr(old_value, "university_Department20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "university_Department20"):
                opp_val = getattr(value, "university_Department20", None)
                if opp_val is None:
                    setattr(value, "university_Department20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def university_StaffMember17(self):
        return self.__university_StaffMember17

    @university_StaffMember17.setter
    def university_StaffMember17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_StaffMember__university_StaffMember17", None)
        self.__university_StaffMember17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "university_Vehicle18"):
                    opp_val = getattr(item, "university_Vehicle18", None)
                    
                    if opp_val == self:
                        setattr(item, "university_Vehicle18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "university_Vehicle18"):
                    opp_val = getattr(item, "university_Vehicle18", None)
                    
                    setattr(item, "university_Vehicle18", self)
                    

    @property
    def moduleLecturers(self):
        return self.__moduleLecturers

    @moduleLecturers.setter
    def moduleLecturers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_StaffMember__moduleLecturers", None)
        self.__moduleLecturers = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Module15"):
                    opp_val = getattr(item, "Module15", None)
                    
                    if opp_val == self:
                        setattr(item, "Module15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Module15"):
                    opp_val = getattr(item, "Module15", None)
                    
                    setattr(item, "Module15", self)
                    

    @property
    def StaffMember(self):
        return self.__StaffMember

    @StaffMember.setter
    def StaffMember(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_StaffMember__StaffMember", None)
        self.__StaffMember = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "taughtModules"):
                opp_val = getattr(old_value, "taughtModules", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "taughtModules"):
                opp_val = getattr(value, "taughtModules", None)
                if opp_val is None:
                    setattr(value, "taughtModules", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
