from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class Course(Enum):
    InfoBSc = "InfoBSc"
    InfoMSc = "InfoMSc"
    InfoDiplom = "InfoDiplom"
    InfoMinorSubject = "InfoMinorSubject"
    InfoPostGraduate = "InfoPostGraduate"
class Status(Enum):
    pending = "pending"
    inprocess = "inprocess"
    completed = "completed"
    cancelled = "cancelled"
class AuxiliaryKind(Enum):
    ProgrammingLanguage = "ProgrammingLanguage"
    Tool = "Tool"
    Method = "Method"


############################################
# Definition of Classes
############################################

class Person:

    pass
class fopramodel_Professor(Person):

    pass
class fopramodel_Person(ABC):

    def __init__(self, forename: str, lastname: str, fopramodel_Person: "fopramodel_FoPraManagementSystem" = None):
        self.forename = forename
        self.lastname = lastname
        self.fopramodel_Person = fopramodel_Person
        
    @property
    def lastname(self) -> str:
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname

    @property
    def forename(self) -> str:
        return self.__forename

    @forename.setter
    def forename(self, forename: str):
        self.__forename = forename

    @property
    def fopramodel_Person(self):
        return self.__fopramodel_Person

    @fopramodel_Person.setter
    def fopramodel_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fopramodel_Person__fopramodel_Person", None)
        self.__fopramodel_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fopramodel_FoPraManagementSystem11"):
                opp_val = getattr(old_value, "fopramodel_FoPraManagementSystem11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fopramodel_FoPraManagementSystem11"):
                opp_val = getattr(value, "fopramodel_FoPraManagementSystem11", None)
                if opp_val is None:
                    setattr(value, "fopramodel_FoPraManagementSystem11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fopramodel_FoPraManagementSystem:

    pass
class fopramodel_Auxiliary:

    def __init__(self, description: str, kind: str, Auxiliary: "fopramodel_FoPra" = None, fopramodel_Auxiliary: "fopramodel_FoPraManagementSystem" = None, auxiliaries: set["fopramodel_FoPra"] = None):
        self.description = description
        self.kind = kind
        self.Auxiliary = Auxiliary
        self.fopramodel_Auxiliary = fopramodel_Auxiliary
        self.auxiliaries = auxiliaries if auxiliaries is not None else set()
        
    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def fopramodel_Auxiliary(self):
        return self.__fopramodel_Auxiliary

    @fopramodel_Auxiliary.setter
    def fopramodel_Auxiliary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fopramodel_Auxiliary__fopramodel_Auxiliary", None)
        self.__fopramodel_Auxiliary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fopramodel_FoPraManagementSystem13"):
                opp_val = getattr(old_value, "fopramodel_FoPraManagementSystem13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fopramodel_FoPraManagementSystem13"):
                opp_val = getattr(value, "fopramodel_FoPraManagementSystem13", None)
                if opp_val is None:
                    setattr(value, "fopramodel_FoPraManagementSystem13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def auxiliaries(self):
        return self.__auxiliaries

    @auxiliaries.setter
    def auxiliaries(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fopramodel_Auxiliary__auxiliaries", None)
        self.__auxiliaries = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FoPra31"):
                    opp_val = getattr(item, "FoPra31", None)
                    
                    if opp_val == self:
                        setattr(item, "FoPra31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FoPra31"):
                    opp_val = getattr(item, "FoPra31", None)
                    
                    setattr(item, "FoPra31", self)
                    

    @property
    def Auxiliary(self):
        return self.__Auxiliary

    @Auxiliary.setter
    def Auxiliary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fopramodel_Auxiliary__Auxiliary", None)
        self.__Auxiliary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fopras8"):
                opp_val = getattr(old_value, "fopras8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fopras8"):
                opp_val = getattr(value, "fopras8", None)
                if opp_val is None:
                    setattr(value, "fopras8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fopramodel_ExternalAdvisor(Person):

    def __init__(self, information: str, ExternalAdvisor: "fopramodel_FoPra" = None, advisor: set["fopramodel_FoPra"] = None):
        self.information = information
        self.ExternalAdvisor = ExternalAdvisor
        self.advisor = advisor if advisor is not None else set()
        
    @property
    def information(self) -> str:
        return self.__information

    @information.setter
    def information(self, information: str):
        self.__information = information

    @property
    def ExternalAdvisor(self):
        return self.__ExternalAdvisor

    @ExternalAdvisor.setter
    def ExternalAdvisor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fopramodel_ExternalAdvisor__ExternalAdvisor", None)
        self.__ExternalAdvisor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fopras6"):
                opp_val = getattr(old_value, "fopras6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fopras6"):
                opp_val = getattr(value, "fopras6", None)
                if opp_val is None:
                    setattr(value, "fopras6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def advisor(self):
        return self.__advisor

    @advisor.setter
    def advisor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fopramodel_ExternalAdvisor__advisor", None)
        self.__advisor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FoPra29"):
                    opp_val = getattr(item, "FoPra29", None)
                    
                    if opp_val == self:
                        setattr(item, "FoPra29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FoPra29"):
                    opp_val = getattr(item, "FoPra29", None)
                    
                    setattr(item, "FoPra29", self)
                    

class fopramodel_Associate(Person):

    pass
class fopramodel_ResearchGroup:

    def __init__(self, name: str, ResearchGroup: "fopramodel_FoPra" = None, ResearchGroup16: "fopramodel_Professor" = None, rg: set["fopramodel_FoPra"] = None, rg20: "fopramodel_Professor" = None, rg22: set["fopramodel_Associate"] = None, ResearchGroup25: "fopramodel_Associate" = None):
        self.name = name
        self.ResearchGroup = ResearchGroup
        self.ResearchGroup16 = ResearchGroup16
        self.rg = rg if rg is not None else set()
        self.rg20 = rg20
        self.rg22 = rg22 if rg22 is not None else set()
        self.ResearchGroup25 = ResearchGroup25
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ResearchGroup(self):
        return self.__ResearchGroup

    @ResearchGroup.setter
    def ResearchGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fopramodel_ResearchGroup__ResearchGroup", None)
        self.__ResearchGroup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fopras2"):
                opp_val = getattr(old_value, "fopras2", None)
                if opp_val == self:
                    setattr(old_value, "fopras2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fopras2"):
                opp_val = getattr(value, "fopras2", None)
                setattr(value, "fopras2", self)

    @property
    def rg22(self):
        return self.__rg22

    @rg22.setter
    def rg22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fopramodel_ResearchGroup__rg22", None)
        self.__rg22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Associate23"):
                    opp_val = getattr(item, "Associate23", None)
                    
                    if opp_val == self:
                        setattr(item, "Associate23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Associate23"):
                    opp_val = getattr(item, "Associate23", None)
                    
                    setattr(item, "Associate23", self)
                    

    @property
    def ResearchGroup16(self):
        return self.__ResearchGroup16

    @ResearchGroup16.setter
    def ResearchGroup16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fopramodel_ResearchGroup__ResearchGroup16", None)
        self.__ResearchGroup16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "professor"):
                opp_val = getattr(old_value, "professor", None)
                if opp_val == self:
                    setattr(old_value, "professor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "professor"):
                opp_val = getattr(value, "professor", None)
                setattr(value, "professor", self)

    @property
    def ResearchGroup25(self):
        return self.__ResearchGroup25

    @ResearchGroup25.setter
    def ResearchGroup25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fopramodel_ResearchGroup__ResearchGroup25", None)
        self.__ResearchGroup25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "associate"):
                opp_val = getattr(old_value, "associate", None)
                if opp_val == self:
                    setattr(old_value, "associate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "associate"):
                opp_val = getattr(value, "associate", None)
                setattr(value, "associate", self)

    @property
    def rg(self):
        return self.__rg

    @rg.setter
    def rg(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fopramodel_ResearchGroup__rg", None)
        self.__rg = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FoPra18"):
                    opp_val = getattr(item, "FoPra18", None)
                    
                    if opp_val == self:
                        setattr(item, "FoPra18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FoPra18"):
                    opp_val = getattr(item, "FoPra18", None)
                    
                    setattr(item, "FoPra18", self)
                    

    @property
    def rg20(self):
        return self.__rg20

    @rg20.setter
    def rg20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fopramodel_ResearchGroup__rg20", None)
        self.__rg20 = value
        
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

class fopramodel_Student(Person):

    def __init__(self, matrikel: str, course: str, Student: "fopramodel_FoPra" = None, students: set["fopramodel_FoPra"] = None):
        self.matrikel = matrikel
        self.course = course
        self.Student = Student
        self.students = students if students is not None else set()
        
    @property
    def course(self) -> str:
        return self.__course

    @course.setter
    def course(self, course: str):
        self.__course = course

    @property
    def matrikel(self) -> str:
        return self.__matrikel

    @matrikel.setter
    def matrikel(self, matrikel: str):
        self.__matrikel = matrikel

    @property
    def Student(self):
        return self.__Student

    @Student.setter
    def Student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fopramodel_Student__Student", None)
        self.__Student = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fopras"):
                opp_val = getattr(old_value, "fopras", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fopras"):
                opp_val = getattr(value, "fopras", None)
                if opp_val is None:
                    setattr(value, "fopras", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def students(self):
        return self.__students

    @students.setter
    def students(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fopramodel_Student__students", None)
        self.__students = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "FoPra"):
                    opp_val = getattr(item, "FoPra", None)
                    
                    if opp_val == self:
                        setattr(item, "FoPra", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "FoPra"):
                    opp_val = getattr(item, "FoPra", None)
                    
                    setattr(item, "FoPra", self)
                    

class fopramodel_FoPra:

    def __init__(self, title: str, description: str, status: str, maxNumberOfStudents: int, start: date, end: date, fopras: set["fopramodel_Student"] = None, fopras2: "fopramodel_ResearchGroup" = None, fopras4: "fopramodel_Associate" = None, fopras6: set["fopramodel_ExternalAdvisor"] = None, fopras8: set["fopramodel_Auxiliary"] = None, fopramodel_FoPra: "fopramodel_FoPraManagementSystem" = None, FoPra: "fopramodel_Student" = None, FoPra18: "fopramodel_ResearchGroup" = None, FoPra27: "fopramodel_Associate" = None, FoPra29: "fopramodel_ExternalAdvisor" = None, FoPra31: "fopramodel_Auxiliary" = None):
        self.title = title
        self.description = description
        self.status = status
        self.maxNumberOfStudents = maxNumberOfStudents
        self.start = start
        self.end = end
        self.fopras = fopras if fopras is not None else set()
        self.fopras2 = fopras2
        self.fopras4 = fopras4
        self.fopras6 = fopras6 if fopras6 is not None else set()
        self.fopras8 = fopras8 if fopras8 is not None else set()
        self.fopramodel_FoPra = fopramodel_FoPra
        self.FoPra = FoPra
        self.FoPra18 = FoPra18
        self.FoPra27 = FoPra27
        self.FoPra29 = FoPra29
        self.FoPra31 = FoPra31
        
    @property
    def maxNumberOfStudents(self) -> int:
        return self.__maxNumberOfStudents

    @maxNumberOfStudents.setter
    def maxNumberOfStudents(self, maxNumberOfStudents: int):
        self.__maxNumberOfStudents = maxNumberOfStudents

    @property
    def start(self) -> date:
        return self.__start

    @start.setter
    def start(self, start: date):
        self.__start = start

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def end(self) -> date:
        return self.__end

    @end.setter
    def end(self, end: date):
        self.__end = end

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def fopras2(self):
        return self.__fopras2

    @fopras2.setter
    def fopras2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fopramodel_FoPra__fopras2", None)
        self.__fopras2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ResearchGroup"):
                opp_val = getattr(old_value, "ResearchGroup", None)
                if opp_val == self:
                    setattr(old_value, "ResearchGroup", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ResearchGroup"):
                opp_val = getattr(value, "ResearchGroup", None)
                setattr(value, "ResearchGroup", self)

    @property
    def FoPra29(self):
        return self.__FoPra29

    @FoPra29.setter
    def FoPra29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fopramodel_FoPra__FoPra29", None)
        self.__FoPra29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "advisor"):
                opp_val = getattr(old_value, "advisor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "advisor"):
                opp_val = getattr(value, "advisor", None)
                if opp_val is None:
                    setattr(value, "advisor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fopras(self):
        return self.__fopras

    @fopras.setter
    def fopras(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fopramodel_FoPra__fopras", None)
        self.__fopras = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Student"):
                    opp_val = getattr(item, "Student", None)
                    
                    if opp_val == self:
                        setattr(item, "Student", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Student"):
                    opp_val = getattr(item, "Student", None)
                    
                    setattr(item, "Student", self)
                    

    @property
    def FoPra(self):
        return self.__FoPra

    @FoPra.setter
    def FoPra(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fopramodel_FoPra__FoPra", None)
        self.__FoPra = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "students"):
                opp_val = getattr(old_value, "students", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "students"):
                opp_val = getattr(value, "students", None)
                if opp_val is None:
                    setattr(value, "students", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def FoPra18(self):
        return self.__FoPra18

    @FoPra18.setter
    def FoPra18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fopramodel_FoPra__FoPra18", None)
        self.__FoPra18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rg"):
                opp_val = getattr(old_value, "rg", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rg"):
                opp_val = getattr(value, "rg", None)
                if opp_val is None:
                    setattr(value, "rg", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def FoPra31(self):
        return self.__FoPra31

    @FoPra31.setter
    def FoPra31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fopramodel_FoPra__FoPra31", None)
        self.__FoPra31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "auxiliaries"):
                opp_val = getattr(old_value, "auxiliaries", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "auxiliaries"):
                opp_val = getattr(value, "auxiliaries", None)
                if opp_val is None:
                    setattr(value, "auxiliaries", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fopras8(self):
        return self.__fopras8

    @fopras8.setter
    def fopras8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fopramodel_FoPra__fopras8", None)
        self.__fopras8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Auxiliary"):
                    opp_val = getattr(item, "Auxiliary", None)
                    
                    if opp_val == self:
                        setattr(item, "Auxiliary", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Auxiliary"):
                    opp_val = getattr(item, "Auxiliary", None)
                    
                    setattr(item, "Auxiliary", self)
                    

    @property
    def FoPra27(self):
        return self.__FoPra27

    @FoPra27.setter
    def FoPra27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fopramodel_FoPra__FoPra27", None)
        self.__FoPra27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "supervisor"):
                opp_val = getattr(old_value, "supervisor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "supervisor"):
                opp_val = getattr(value, "supervisor", None)
                if opp_val is None:
                    setattr(value, "supervisor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fopramodel_FoPra(self):
        return self.__fopramodel_FoPra

    @fopramodel_FoPra.setter
    def fopramodel_FoPra(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fopramodel_FoPra__fopramodel_FoPra", None)
        self.__fopramodel_FoPra = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fopramodel_FoPraManagementSystem"):
                opp_val = getattr(old_value, "fopramodel_FoPraManagementSystem", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fopramodel_FoPraManagementSystem"):
                opp_val = getattr(value, "fopramodel_FoPraManagementSystem", None)
                if opp_val is None:
                    setattr(value, "fopramodel_FoPraManagementSystem", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fopras6(self):
        return self.__fopras6

    @fopras6.setter
    def fopras6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fopramodel_FoPra__fopras6", None)
        self.__fopras6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ExternalAdvisor"):
                    opp_val = getattr(item, "ExternalAdvisor", None)
                    
                    if opp_val == self:
                        setattr(item, "ExternalAdvisor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ExternalAdvisor"):
                    opp_val = getattr(item, "ExternalAdvisor", None)
                    
                    setattr(item, "ExternalAdvisor", self)
                    

    @property
    def fopras4(self):
        return self.__fopras4

    @fopras4.setter
    def fopras4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fopramodel_FoPra__fopras4", None)
        self.__fopras4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Associate"):
                opp_val = getattr(old_value, "Associate", None)
                if opp_val == self:
                    setattr(old_value, "Associate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Associate"):
                opp_val = getattr(value, "Associate", None)
                setattr(value, "Associate", self)
