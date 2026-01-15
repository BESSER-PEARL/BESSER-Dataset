from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class SemesterKind(Enum):
    AUTUMN = "AUTUMN"
    SPRING = "SPRING"


############################################
# Definition of Classes
############################################

class model_CourseInstance:

    pass
class model_CourseAllocation:

    def __init__(self, factor: str, explicitFactor: str, CourseAllocation: "model_Person" = None, CourseAllocation16: "model_CourseInstance" = None, allocations: "model_Person" = None, model_CourseAllocation: "model_Role" = None, allocations21: "model_CourseInstance" = None):
        self.factor = factor
        self.explicitFactor = explicitFactor
        self.CourseAllocation = CourseAllocation
        self.CourseAllocation16 = CourseAllocation16
        self.allocations = allocations
        self.model_CourseAllocation = model_CourseAllocation
        self.allocations21 = allocations21
        
    @property
    def explicitFactor(self) -> str:
        return self.__explicitFactor

    @explicitFactor.setter
    def explicitFactor(self, explicitFactor: str):
        self.__explicitFactor = explicitFactor

    @property
    def factor(self) -> str:
        return self.__factor

    @factor.setter
    def factor(self, factor: str):
        self.__factor = factor

    @property
    def model_CourseAllocation(self):
        return self.__model_CourseAllocation

    @model_CourseAllocation.setter
    def model_CourseAllocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_CourseAllocation__model_CourseAllocation", None)
        self.__model_CourseAllocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Role19"):
                opp_val = getattr(old_value, "model_Role19", None)
                if opp_val == self:
                    setattr(old_value, "model_Role19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Role19"):
                opp_val = getattr(value, "model_Role19", None)
                setattr(value, "model_Role19", self)

    @property
    def allocations21(self):
        return self.__allocations21

    @allocations21.setter
    def allocations21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_CourseAllocation__allocations21", None)
        self.__allocations21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CourseInstance22"):
                opp_val = getattr(old_value, "CourseInstance22", None)
                if opp_val == self:
                    setattr(old_value, "CourseInstance22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CourseInstance22"):
                opp_val = getattr(value, "CourseInstance22", None)
                setattr(value, "CourseInstance22", self)

    @property
    def CourseAllocation(self):
        return self.__CourseAllocation

    @CourseAllocation.setter
    def CourseAllocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_CourseAllocation__CourseAllocation", None)
        self.__CourseAllocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "person"):
                opp_val = getattr(old_value, "person", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "person"):
                opp_val = getattr(value, "person", None)
                if opp_val is None:
                    setattr(value, "person", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CourseAllocation16(self):
        return self.__CourseAllocation16

    @CourseAllocation16.setter
    def CourseAllocation16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_CourseAllocation__CourseAllocation16", None)
        self.__CourseAllocation16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course"):
                opp_val = getattr(old_value, "course", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course"):
                opp_val = getattr(value, "course", None)
                if opp_val is None:
                    setattr(value, "course", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def allocations(self):
        return self.__allocations

    @allocations.setter
    def allocations(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_CourseAllocation__allocations", None)
        self.__allocations = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Person"):
                opp_val = getattr(old_value, "Person", None)
                if opp_val == self:
                    setattr(old_value, "Person", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Person"):
                opp_val = getattr(value, "Person", None)
                setattr(value, "Person", self)

class model_Semester:

    def __init__(self, year: str, kind: str, model_Semester: "model_Department" = None, semester: set["model_CourseInstance"] = None, Semester: "model_CourseInstance" = None):
        self.year = year
        self.kind = kind
        self.model_Semester = model_Semester
        self.semester = semester if semester is not None else set()
        self.Semester = Semester
        
    @property
    def year(self) -> str:
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year

    @property
    def kind(self) -> str:
        return self.__kind

    @kind.setter
    def kind(self, kind: str):
        self.__kind = kind

    @property
    def Semester(self):
        return self.__Semester

    @Semester.setter
    def Semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Semester__Semester", None)
        self.__Semester = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courses"):
                opp_val = getattr(old_value, "courses", None)
                if opp_val == self:
                    setattr(old_value, "courses", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courses"):
                opp_val = getattr(value, "courses", None)
                setattr(value, "courses", self)

    @property
    def semester(self):
        return self.__semester

    @semester.setter
    def semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Semester__semester", None)
        self.__semester = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CourseInstance"):
                    opp_val = getattr(item, "CourseInstance", None)
                    
                    if opp_val == self:
                        setattr(item, "CourseInstance", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CourseInstance"):
                    opp_val = getattr(item, "CourseInstance", None)
                    
                    setattr(item, "CourseInstance", self)
                    

    @property
    def model_Semester(self):
        return self.__model_Semester

    @model_Semester.setter
    def model_Semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Semester__model_Semester", None)
        self.__model_Semester = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Department6"):
                opp_val = getattr(old_value, "model_Department6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Department6"):
                opp_val = getattr(value, "model_Department6", None)
                if opp_val is None:
                    setattr(value, "model_Department6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class model_Role:

    def __init__(self, name: str, factor: str, model_Role: "model_Department" = None, model_Role10: "model_Course" = None, model_Role19: "model_CourseAllocation" = None):
        self.name = name
        self.factor = factor
        self.model_Role = model_Role
        self.model_Role10 = model_Role10
        self.model_Role19 = model_Role19
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def factor(self) -> str:
        return self.__factor

    @factor.setter
    def factor(self, factor: str):
        self.__factor = factor

    @property
    def model_Role10(self):
        return self.__model_Role10

    @model_Role10.setter
    def model_Role10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Role__model_Role10", None)
        self.__model_Role10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Course9"):
                opp_val = getattr(old_value, "model_Course9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Course9"):
                opp_val = getattr(value, "model_Course9", None)
                if opp_val is None:
                    setattr(value, "model_Course9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Role(self):
        return self.__model_Role

    @model_Role.setter
    def model_Role(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Role__model_Role", None)
        self.__model_Role = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Department4"):
                opp_val = getattr(old_value, "model_Department4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Department4"):
                opp_val = getattr(value, "model_Department4", None)
                if opp_val is None:
                    setattr(value, "model_Department4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Role19(self):
        return self.__model_Role19

    @model_Role19.setter
    def model_Role19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Role__model_Role19", None)
        self.__model_Role19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_CourseAllocation"):
                opp_val = getattr(old_value, "model_CourseAllocation", None)
                if opp_val == self:
                    setattr(old_value, "model_CourseAllocation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_CourseAllocation"):
                opp_val = getattr(value, "model_CourseAllocation", None)
                setattr(value, "model_CourseAllocation", self)

class model_Course:

    def __init__(self, name: str, fullName: str, model_Course: "model_Department" = None, model_Course9: set["model_Role"] = None, model_Course13: "model_CourseInstance" = None):
        self.name = name
        self.fullName = fullName
        self.model_Course = model_Course
        self.model_Course9 = model_Course9 if model_Course9 is not None else set()
        self.model_Course13 = model_Course13
        
    @property
    def fullName(self) -> str:
        return self.__fullName

    @fullName.setter
    def fullName(self, fullName: str):
        self.__fullName = fullName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_Course13(self):
        return self.__model_Course13

    @model_Course13.setter
    def model_Course13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Course__model_Course13", None)
        self.__model_Course13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_CourseInstance"):
                opp_val = getattr(old_value, "model_CourseInstance", None)
                if opp_val == self:
                    setattr(old_value, "model_CourseInstance", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_CourseInstance"):
                opp_val = getattr(value, "model_CourseInstance", None)
                setattr(value, "model_CourseInstance", self)

    @property
    def model_Course(self):
        return self.__model_Course

    @model_Course.setter
    def model_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Course__model_Course", None)
        self.__model_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Department2"):
                opp_val = getattr(old_value, "model_Department2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Department2"):
                opp_val = getattr(value, "model_Department2", None)
                if opp_val is None:
                    setattr(value, "model_Department2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def model_Course9(self):
        return self.__model_Course9

    @model_Course9.setter
    def model_Course9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Course__model_Course9", None)
        self.__model_Course9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Role10"):
                    opp_val = getattr(item, "model_Role10", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Role10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Role10"):
                    opp_val = getattr(item, "model_Role10", None)
                    
                    setattr(item, "model_Role10", self)
                    

class model_Person:

    def __init__(self, name: str, userName: str, email: str, faceUrl: str, employmentFactor: str, model_Person: "model_Department" = None, person: set["model_CourseAllocation"] = None, Person: "model_CourseAllocation" = None):
        self.name = name
        self.userName = userName
        self.email = email
        self.faceUrl = faceUrl
        self.employmentFactor = employmentFactor
        self.model_Person = model_Person
        self.person = person if person is not None else set()
        self.Person = Person
        
    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def faceUrl(self) -> str:
        return self.__faceUrl

    @faceUrl.setter
    def faceUrl(self, faceUrl: str):
        self.__faceUrl = faceUrl

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def userName(self) -> str:
        return self.__userName

    @userName.setter
    def userName(self, userName: str):
        self.__userName = userName

    @property
    def employmentFactor(self) -> str:
        return self.__employmentFactor

    @employmentFactor.setter
    def employmentFactor(self, employmentFactor: str):
        self.__employmentFactor = employmentFactor

    @property
    def model_Person(self):
        return self.__model_Person

    @model_Person.setter
    def model_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Person__model_Person", None)
        self.__model_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "model_Department"):
                opp_val = getattr(old_value, "model_Department", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "model_Department"):
                opp_val = getattr(value, "model_Department", None)
                if opp_val is None:
                    setattr(value, "model_Department", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def person(self):
        return self.__person

    @person.setter
    def person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Person__person", None)
        self.__person = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CourseAllocation"):
                    opp_val = getattr(item, "CourseAllocation", None)
                    
                    if opp_val == self:
                        setattr(item, "CourseAllocation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CourseAllocation"):
                    opp_val = getattr(item, "CourseAllocation", None)
                    
                    setattr(item, "CourseAllocation", self)
                    

    @property
    def Person(self):
        return self.__Person

    @Person.setter
    def Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Person__Person", None)
        self.__Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "allocations"):
                opp_val = getattr(old_value, "allocations", None)
                if opp_val == self:
                    setattr(old_value, "allocations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "allocations"):
                opp_val = getattr(value, "allocations", None)
                setattr(value, "allocations", self)

class model_Department:

    def __init__(self, name: str, model_Department: set["model_Person"] = None, model_Department2: set["model_Course"] = None, model_Department4: set["model_Role"] = None, model_Department6: set["model_Semester"] = None):
        self.name = name
        self.model_Department = model_Department if model_Department is not None else set()
        self.model_Department2 = model_Department2 if model_Department2 is not None else set()
        self.model_Department4 = model_Department4 if model_Department4 is not None else set()
        self.model_Department6 = model_Department6 if model_Department6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def model_Department6(self):
        return self.__model_Department6

    @model_Department6.setter
    def model_Department6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Department__model_Department6", None)
        self.__model_Department6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Semester"):
                    opp_val = getattr(item, "model_Semester", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Semester", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Semester"):
                    opp_val = getattr(item, "model_Semester", None)
                    
                    setattr(item, "model_Semester", self)
                    

    @property
    def model_Department4(self):
        return self.__model_Department4

    @model_Department4.setter
    def model_Department4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Department__model_Department4", None)
        self.__model_Department4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Role"):
                    opp_val = getattr(item, "model_Role", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Role", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Role"):
                    opp_val = getattr(item, "model_Role", None)
                    
                    setattr(item, "model_Role", self)
                    

    @property
    def model_Department2(self):
        return self.__model_Department2

    @model_Department2.setter
    def model_Department2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Department__model_Department2", None)
        self.__model_Department2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Course"):
                    opp_val = getattr(item, "model_Course", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Course", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Course"):
                    opp_val = getattr(item, "model_Course", None)
                    
                    setattr(item, "model_Course", self)
                    

    @property
    def model_Department(self):
        return self.__model_Department

    @model_Department.setter
    def model_Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_model_Department__model_Department", None)
        self.__model_Department = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "model_Person"):
                    opp_val = getattr(item, "model_Person", None)
                    
                    if opp_val == self:
                        setattr(item, "model_Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "model_Person"):
                    opp_val = getattr(item, "model_Person", None)
                    
                    setattr(item, "model_Person", self)
                    
