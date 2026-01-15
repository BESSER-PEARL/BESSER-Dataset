from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class university_Address:

    pass
class university_Person(ABC):

    def __init__(self, name: str, university_Person: set["university_Address"] = None):
        self.name = name
        self.university_Person = university_Person if university_Person is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def university_Person(self):
        return self.__university_Person

    @university_Person.setter
    def university_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Person__university_Person", None)
        self.__university_Person = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "university_Address"):
                    opp_val = getattr(item, "university_Address", None)
                    
                    if opp_val == self:
                        setattr(item, "university_Address", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "university_Address"):
                    opp_val = getattr(item, "university_Address", None)
                    
                    setattr(item, "university_Address", self)
                    

class Person:

    pass
class university_Assistant(Person):

    pass
class university_Professor(Person):

    pass
class university_Staff:

    def __init__(self, staff: str, university_Staff: set["university_Professor"] = None, university_Staff3: set["university_Assistant"] = None):
        self.staff = staff
        self.university_Staff = university_Staff if university_Staff is not None else set()
        self.university_Staff3 = university_Staff3 if university_Staff3 is not None else set()
        
    @property
    def staff(self) -> str:
        return self.__staff

    @staff.setter
    def staff(self, staff: str):
        self.__staff = staff

    @property
    def university_Staff3(self):
        return self.__university_Staff3

    @university_Staff3.setter
    def university_Staff3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Staff__university_Staff3", None)
        self.__university_Staff3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "university_Assistant"):
                    opp_val = getattr(item, "university_Assistant", None)
                    
                    if opp_val == self:
                        setattr(item, "university_Assistant", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "university_Assistant"):
                    opp_val = getattr(item, "university_Assistant", None)
                    
                    setattr(item, "university_Assistant", self)
                    

    @property
    def university_Staff(self):
        return self.__university_Staff

    @university_Staff.setter
    def university_Staff(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Staff__university_Staff", None)
        self.__university_Staff = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "university_Professor"):
                    opp_val = getattr(item, "university_Professor", None)
                    
                    if opp_val == self:
                        setattr(item, "university_Professor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "university_Professor"):
                    opp_val = getattr(item, "university_Professor", None)
                    
                    setattr(item, "university_Professor", self)
                    

class university_Course:

    def __init__(self, id: str, name: str, etcs: int, university_Course: "university_CourseCatalog" = None):
        self.id = id
        self.name = name
        self.etcs = etcs
        self.university_Course = university_Course
        
    @property
    def etcs(self) -> int:
        return self.__etcs

    @etcs.setter
    def etcs(self, etcs: int):
        self.__etcs = etcs

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def university_Course(self):
        return self.__university_Course

    @university_Course.setter
    def university_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Course__university_Course", None)
        self.__university_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "university_CourseCatalog"):
                opp_val = getattr(old_value, "university_CourseCatalog", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "university_CourseCatalog"):
                opp_val = getattr(value, "university_CourseCatalog", None)
                if opp_val is None:
                    setattr(value, "university_CourseCatalog", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class university_CourseCatalog:

    pass