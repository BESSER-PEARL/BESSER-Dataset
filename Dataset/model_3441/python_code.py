from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class scholar_Named(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class scholar_ScholarManagement:

    pass
class Named:

    pass
class scholar_Lecture(Named):

    pass
class scholar_Exam(Named):

    def __init__(self, score: float, scholar_Exam: "scholar_Student" = None, scholar_Exam5: "scholar_Lecture" = None):
        self.score = score
        self.scholar_Exam = scholar_Exam
        self.scholar_Exam5 = scholar_Exam5
        
    @property
    def score(self) -> float:
        return self.__score

    @score.setter
    def score(self, score: float):
        self.__score = score

    @property
    def scholar_Exam(self):
        return self.__scholar_Exam

    @scholar_Exam.setter
    def scholar_Exam(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scholar_Exam__scholar_Exam", None)
        self.__scholar_Exam = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scholar_Student"):
                opp_val = getattr(old_value, "scholar_Student", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scholar_Student"):
                opp_val = getattr(value, "scholar_Student", None)
                if opp_val is None:
                    setattr(value, "scholar_Student", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scholar_Exam5(self):
        return self.__scholar_Exam5

    @scholar_Exam5.setter
    def scholar_Exam5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scholar_Exam__scholar_Exam5", None)
        self.__scholar_Exam5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scholar_Lecture6"):
                opp_val = getattr(old_value, "scholar_Lecture6", None)
                if opp_val == self:
                    setattr(old_value, "scholar_Lecture6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scholar_Lecture6"):
                opp_val = getattr(value, "scholar_Lecture6", None)
                setattr(value, "scholar_Lecture6", self)

class scholar_Discipline(Named):

    pass
class scholar_Teacher(Named):

    pass
class scholar_Student(Named):

    def __init__(self, forname: str, scholar_Student: set["scholar_Exam"] = None, scholar_Student8: "scholar_ScholarManagement" = None):
        self.forname = forname
        self.scholar_Student = scholar_Student if scholar_Student is not None else set()
        self.scholar_Student8 = scholar_Student8
        
    @property
    def forname(self) -> str:
        return self.__forname

    @forname.setter
    def forname(self, forname: str):
        self.__forname = forname

    @property
    def scholar_Student8(self):
        return self.__scholar_Student8

    @scholar_Student8.setter
    def scholar_Student8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scholar_Student__scholar_Student8", None)
        self.__scholar_Student8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scholar_ScholarManagement"):
                opp_val = getattr(old_value, "scholar_ScholarManagement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scholar_ScholarManagement"):
                opp_val = getattr(value, "scholar_ScholarManagement", None)
                if opp_val is None:
                    setattr(value, "scholar_ScholarManagement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scholar_Student(self):
        return self.__scholar_Student

    @scholar_Student.setter
    def scholar_Student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scholar_Student__scholar_Student", None)
        self.__scholar_Student = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scholar_Exam"):
                    opp_val = getattr(item, "scholar_Exam", None)
                    
                    if opp_val == self:
                        setattr(item, "scholar_Exam", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scholar_Exam"):
                    opp_val = getattr(item, "scholar_Exam", None)
                    
                    setattr(item, "scholar_Exam", self)
                    
