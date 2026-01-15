from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ResponsibilityRole(Enum):
    ASSISTANT = "ASSISTANT"
    LECTURER = "LECTURER"
    COORDINATOR = "COORDINATOR"


############################################
# Definition of Classes
############################################

class tdt4250__bDXQcCdxEeKsSJflfBDxuw:

    pass
class tdt4250_Root:

    pass
class tdt4250_Person:

    def __init__(self, ID: int, name: str):
        self.ID = ID
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ID(self) -> int:
        return self.__ID

    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

class tdt4250_Assignment:

    def __init__(self, name: str, content: str, mandatory: bool, ID: int, tdt4250_Assignment: set["tdt4250__bDSX8CdxEeKsSJflfBDxuw"] = None):
        self.name = name
        self.content = content
        self.mandatory = mandatory
        self.ID = ID
        self.tdt4250_Assignment = tdt4250_Assignment if tdt4250_Assignment is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def mandatory(self) -> bool:
        return self.__mandatory

    @mandatory.setter
    def mandatory(self, mandatory: bool):
        self.__mandatory = mandatory

    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def ID(self) -> int:
        return self.__ID

    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def tdt4250_Assignment(self):
        return self.__tdt4250_Assignment

    @tdt4250_Assignment.setter
    def tdt4250_Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250_Assignment__tdt4250_Assignment", None)
        self.__tdt4250_Assignment = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tdt4250__bDSX8CdxEeKsSJflfBDxuw"):
                    opp_val = getattr(item, "tdt4250__bDSX8CdxEeKsSJflfBDxuw", None)
                    
                    if opp_val == self:
                        setattr(item, "tdt4250__bDSX8CdxEeKsSJflfBDxuw", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tdt4250__bDSX8CdxEeKsSJflfBDxuw"):
                    opp_val = getattr(item, "tdt4250__bDSX8CdxEeKsSJflfBDxuw", None)
                    
                    setattr(item, "tdt4250__bDSX8CdxEeKsSJflfBDxuw", self)
                    

class tdt4250__bDIm8SdxEeKsSJflfBDxuw:

    pass
class _bDXQcCdxEeKsSJflfBDxuw:

    pass
class tdt4250_Teacher(_bDXQcCdxEeKsSJflfBDxuw):

    def __init__(self, role: str, tdt4250_Teacher: set["tdt4250__bDIm8SdxEeKsSJflfBDxuw"] = None):
        self.role = role
        self.tdt4250_Teacher = tdt4250_Teacher if tdt4250_Teacher is not None else set()
        
    @property
    def role(self) -> str:
        return self.__role

    @role.setter
    def role(self, role: str):
        self.__role = role

    @property
    def tdt4250_Teacher(self):
        return self.__tdt4250_Teacher

    @tdt4250_Teacher.setter
    def tdt4250_Teacher(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250_Teacher__tdt4250_Teacher", None)
        self.__tdt4250_Teacher = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tdt4250__bDIm8SdxEeKsSJflfBDxuw11"):
                    opp_val = getattr(item, "tdt4250__bDIm8SdxEeKsSJflfBDxuw11", None)
                    
                    if opp_val == self:
                        setattr(item, "tdt4250__bDIm8SdxEeKsSJflfBDxuw11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tdt4250__bDIm8SdxEeKsSJflfBDxuw11"):
                    opp_val = getattr(item, "tdt4250__bDIm8SdxEeKsSJflfBDxuw11", None)
                    
                    setattr(item, "tdt4250__bDIm8SdxEeKsSJflfBDxuw11", self)
                    

class tdt4250_Student(_bDXQcCdxEeKsSJflfBDxuw):

    pass
class tdt4250_Answer:

    def __init__(self, content: str):
        self.content = content
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

class tdt4250__bDSX8CdxEeKsSJflfBDxuw:

    pass
class tdt4250__bDYekCdxEeKsSJflfBDxuw:

    pass
class tdt4250__bDTmECdxEeKsSJflfBDxuw:

    pass
class tdt4250__bDNfcCdxEeKsSJflfBDxuw:

    pass
class tdt4250_Course:

    def __init__(self, ID: int, credit: int, name: str, tdt4250_Course: set["tdt4250__bDNfcCdxEeKsSJflfBDxuw"] = None, tdt4250_Course2: set["tdt4250__bDTmECdxEeKsSJflfBDxuw"] = None, tdt4250_Course4: set["tdt4250__bDYekCdxEeKsSJflfBDxuw"] = None):
        self.ID = ID
        self.credit = credit
        self.name = name
        self.tdt4250_Course = tdt4250_Course if tdt4250_Course is not None else set()
        self.tdt4250_Course2 = tdt4250_Course2 if tdt4250_Course2 is not None else set()
        self.tdt4250_Course4 = tdt4250_Course4 if tdt4250_Course4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def credit(self) -> int:
        return self.__credit

    @credit.setter
    def credit(self, credit: int):
        self.__credit = credit

    @property
    def ID(self) -> int:
        return self.__ID

    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def tdt4250_Course(self):
        return self.__tdt4250_Course

    @tdt4250_Course.setter
    def tdt4250_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250_Course__tdt4250_Course", None)
        self.__tdt4250_Course = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tdt4250__bDNfcCdxEeKsSJflfBDxuw"):
                    opp_val = getattr(item, "tdt4250__bDNfcCdxEeKsSJflfBDxuw", None)
                    
                    if opp_val == self:
                        setattr(item, "tdt4250__bDNfcCdxEeKsSJflfBDxuw", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tdt4250__bDNfcCdxEeKsSJflfBDxuw"):
                    opp_val = getattr(item, "tdt4250__bDNfcCdxEeKsSJflfBDxuw", None)
                    
                    setattr(item, "tdt4250__bDNfcCdxEeKsSJflfBDxuw", self)
                    

    @property
    def tdt4250_Course4(self):
        return self.__tdt4250_Course4

    @tdt4250_Course4.setter
    def tdt4250_Course4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250_Course__tdt4250_Course4", None)
        self.__tdt4250_Course4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tdt4250__bDYekCdxEeKsSJflfBDxuw"):
                    opp_val = getattr(item, "tdt4250__bDYekCdxEeKsSJflfBDxuw", None)
                    
                    if opp_val == self:
                        setattr(item, "tdt4250__bDYekCdxEeKsSJflfBDxuw", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tdt4250__bDYekCdxEeKsSJflfBDxuw"):
                    opp_val = getattr(item, "tdt4250__bDYekCdxEeKsSJflfBDxuw", None)
                    
                    setattr(item, "tdt4250__bDYekCdxEeKsSJflfBDxuw", self)
                    

    @property
    def tdt4250_Course2(self):
        return self.__tdt4250_Course2

    @tdt4250_Course2.setter
    def tdt4250_Course2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250_Course__tdt4250_Course2", None)
        self.__tdt4250_Course2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tdt4250__bDTmECdxEeKsSJflfBDxuw"):
                    opp_val = getattr(item, "tdt4250__bDTmECdxEeKsSJflfBDxuw", None)
                    
                    if opp_val == self:
                        setattr(item, "tdt4250__bDTmECdxEeKsSJflfBDxuw", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tdt4250__bDTmECdxEeKsSJflfBDxuw"):
                    opp_val = getattr(item, "tdt4250__bDTmECdxEeKsSJflfBDxuw", None)
                    
                    setattr(item, "tdt4250__bDTmECdxEeKsSJflfBDxuw", self)
                    
