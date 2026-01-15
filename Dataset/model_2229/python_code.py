from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Season(Enum):
    Fall = "Fall"
    Spring = "Spring"
    Summer = "Summer"


############################################
# Definition of Classes
############################################

class studyprogram_Slot:

    pass
class studyprogram_Department:

    def __init__(self, name: str, studyprogram_Department: set["studyprogram_Course"] = None, studyprogram_Department19: set["studyprogram_Program"] = None):
        self.name = name
        self.studyprogram_Department = studyprogram_Department if studyprogram_Department is not None else set()
        self.studyprogram_Department19 = studyprogram_Department19 if studyprogram_Department19 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def studyprogram_Department19(self):
        return self.__studyprogram_Department19

    @studyprogram_Department19.setter
    def studyprogram_Department19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Department__studyprogram_Department19", None)
        self.__studyprogram_Department19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studyprogram_Program20"):
                    opp_val = getattr(item, "studyprogram_Program20", None)
                    
                    if opp_val == self:
                        setattr(item, "studyprogram_Program20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studyprogram_Program20"):
                    opp_val = getattr(item, "studyprogram_Program20", None)
                    
                    setattr(item, "studyprogram_Program20", self)
                    

    @property
    def studyprogram_Department(self):
        return self.__studyprogram_Department

    @studyprogram_Department.setter
    def studyprogram_Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Department__studyprogram_Department", None)
        self.__studyprogram_Department = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studyprogram_Course17"):
                    opp_val = getattr(item, "studyprogram_Course17", None)
                    
                    if opp_val == self:
                        setattr(item, "studyprogram_Course17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studyprogram_Course17"):
                    opp_val = getattr(item, "studyprogram_Course17", None)
                    
                    setattr(item, "studyprogram_Course17", self)
                    

class studyprogram_Course:

    def __init__(self, name: str, credits: float, studyprogram_Course: "studyprogram_Slot" = None, studyprogram_Course15: "studyprogram_Slot" = None, studyprogram_Course17: "studyprogram_Department" = None):
        self.name = name
        self.credits = credits
        self.studyprogram_Course = studyprogram_Course
        self.studyprogram_Course15 = studyprogram_Course15
        self.studyprogram_Course17 = studyprogram_Course17
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def credits(self) -> float:
        return self.__credits

    @credits.setter
    def credits(self, credits: float):
        self.__credits = credits

    @property
    def studyprogram_Course(self):
        return self.__studyprogram_Course

    @studyprogram_Course.setter
    def studyprogram_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Course__studyprogram_Course", None)
        self.__studyprogram_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyprogram_Slot12"):
                opp_val = getattr(old_value, "studyprogram_Slot12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyprogram_Slot12"):
                opp_val = getattr(value, "studyprogram_Slot12", None)
                if opp_val is None:
                    setattr(value, "studyprogram_Slot12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def studyprogram_Course17(self):
        return self.__studyprogram_Course17

    @studyprogram_Course17.setter
    def studyprogram_Course17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Course__studyprogram_Course17", None)
        self.__studyprogram_Course17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyprogram_Department"):
                opp_val = getattr(old_value, "studyprogram_Department", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyprogram_Department"):
                opp_val = getattr(value, "studyprogram_Department", None)
                if opp_val is None:
                    setattr(value, "studyprogram_Department", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def studyprogram_Course15(self):
        return self.__studyprogram_Course15

    @studyprogram_Course15.setter
    def studyprogram_Course15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Course__studyprogram_Course15", None)
        self.__studyprogram_Course15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyprogram_Slot14"):
                opp_val = getattr(old_value, "studyprogram_Slot14", None)
                if opp_val == self:
                    setattr(old_value, "studyprogram_Slot14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyprogram_Slot14"):
                opp_val = getattr(value, "studyprogram_Slot14", None)
                setattr(value, "studyprogram_Slot14", self)

class studyprogram_Specialization:

    def __init__(self, name: str, studyprogram_Specialization: "studyprogram_Program" = None, studyprogram_Specialization4: set["studyprogram_Semester"] = None, studyprogram_Specialization8: "studyprogram_Specialization" = None, studyprogram_Specialization6: set["studyprogram_Specialization"] = None):
        self.name = name
        self.studyprogram_Specialization = studyprogram_Specialization
        self.studyprogram_Specialization4 = studyprogram_Specialization4 if studyprogram_Specialization4 is not None else set()
        self.studyprogram_Specialization8 = studyprogram_Specialization8
        self.studyprogram_Specialization6 = studyprogram_Specialization6 if studyprogram_Specialization6 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def studyprogram_Specialization4(self):
        return self.__studyprogram_Specialization4

    @studyprogram_Specialization4.setter
    def studyprogram_Specialization4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Specialization__studyprogram_Specialization4", None)
        self.__studyprogram_Specialization4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studyprogram_Semester5"):
                    opp_val = getattr(item, "studyprogram_Semester5", None)
                    
                    if opp_val == self:
                        setattr(item, "studyprogram_Semester5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studyprogram_Semester5"):
                    opp_val = getattr(item, "studyprogram_Semester5", None)
                    
                    setattr(item, "studyprogram_Semester5", self)
                    

    @property
    def studyprogram_Specialization8(self):
        return self.__studyprogram_Specialization8

    @studyprogram_Specialization8.setter
    def studyprogram_Specialization8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Specialization__studyprogram_Specialization8", None)
        self.__studyprogram_Specialization8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyprogram_Specialization6"):
                opp_val = getattr(old_value, "studyprogram_Specialization6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyprogram_Specialization6"):
                opp_val = getattr(value, "studyprogram_Specialization6", None)
                if opp_val is None:
                    setattr(value, "studyprogram_Specialization6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def studyprogram_Specialization(self):
        return self.__studyprogram_Specialization

    @studyprogram_Specialization.setter
    def studyprogram_Specialization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Specialization__studyprogram_Specialization", None)
        self.__studyprogram_Specialization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyprogram_Program2"):
                opp_val = getattr(old_value, "studyprogram_Program2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyprogram_Program2"):
                opp_val = getattr(value, "studyprogram_Program2", None)
                if opp_val is None:
                    setattr(value, "studyprogram_Program2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def studyprogram_Specialization6(self):
        return self.__studyprogram_Specialization6

    @studyprogram_Specialization6.setter
    def studyprogram_Specialization6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Specialization__studyprogram_Specialization6", None)
        self.__studyprogram_Specialization6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studyprogram_Specialization8"):
                    opp_val = getattr(item, "studyprogram_Specialization8", None)
                    
                    if opp_val == self:
                        setattr(item, "studyprogram_Specialization8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studyprogram_Specialization8"):
                    opp_val = getattr(item, "studyprogram_Specialization8", None)
                    
                    setattr(item, "studyprogram_Specialization8", self)
                    

class studyprogram_Semester:

    def __init__(self, season: str, year: int, studyprogram_Semester: "studyprogram_Program" = None, studyprogram_Semester5: "studyprogram_Specialization" = None, studyprogram_Semester10: set["studyprogram_Slot"] = None):
        self.season = season
        self.year = year
        self.studyprogram_Semester = studyprogram_Semester
        self.studyprogram_Semester5 = studyprogram_Semester5
        self.studyprogram_Semester10 = studyprogram_Semester10 if studyprogram_Semester10 is not None else set()
        
    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def season(self) -> str:
        return self.__season

    @season.setter
    def season(self, season: str):
        self.__season = season

    @property
    def studyprogram_Semester5(self):
        return self.__studyprogram_Semester5

    @studyprogram_Semester5.setter
    def studyprogram_Semester5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Semester__studyprogram_Semester5", None)
        self.__studyprogram_Semester5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyprogram_Specialization4"):
                opp_val = getattr(old_value, "studyprogram_Specialization4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyprogram_Specialization4"):
                opp_val = getattr(value, "studyprogram_Specialization4", None)
                if opp_val is None:
                    setattr(value, "studyprogram_Specialization4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def studyprogram_Semester(self):
        return self.__studyprogram_Semester

    @studyprogram_Semester.setter
    def studyprogram_Semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Semester__studyprogram_Semester", None)
        self.__studyprogram_Semester = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyprogram_Program"):
                opp_val = getattr(old_value, "studyprogram_Program", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyprogram_Program"):
                opp_val = getattr(value, "studyprogram_Program", None)
                if opp_val is None:
                    setattr(value, "studyprogram_Program", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def studyprogram_Semester10(self):
        return self.__studyprogram_Semester10

    @studyprogram_Semester10.setter
    def studyprogram_Semester10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Semester__studyprogram_Semester10", None)
        self.__studyprogram_Semester10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studyprogram_Slot"):
                    opp_val = getattr(item, "studyprogram_Slot", None)
                    
                    if opp_val == self:
                        setattr(item, "studyprogram_Slot", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studyprogram_Slot"):
                    opp_val = getattr(item, "studyprogram_Slot", None)
                    
                    setattr(item, "studyprogram_Slot", self)
                    

class studyprogram_Program:

    def __init__(self, name: str, studyprogram_Program: set["studyprogram_Semester"] = None, studyprogram_Program2: set["studyprogram_Specialization"] = None, studyprogram_Program20: "studyprogram_Department" = None):
        self.name = name
        self.studyprogram_Program = studyprogram_Program if studyprogram_Program is not None else set()
        self.studyprogram_Program2 = studyprogram_Program2 if studyprogram_Program2 is not None else set()
        self.studyprogram_Program20 = studyprogram_Program20
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def studyprogram_Program2(self):
        return self.__studyprogram_Program2

    @studyprogram_Program2.setter
    def studyprogram_Program2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Program__studyprogram_Program2", None)
        self.__studyprogram_Program2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studyprogram_Specialization"):
                    opp_val = getattr(item, "studyprogram_Specialization", None)
                    
                    if opp_val == self:
                        setattr(item, "studyprogram_Specialization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studyprogram_Specialization"):
                    opp_val = getattr(item, "studyprogram_Specialization", None)
                    
                    setattr(item, "studyprogram_Specialization", self)
                    

    @property
    def studyprogram_Program(self):
        return self.__studyprogram_Program

    @studyprogram_Program.setter
    def studyprogram_Program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Program__studyprogram_Program", None)
        self.__studyprogram_Program = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "studyprogram_Semester"):
                    opp_val = getattr(item, "studyprogram_Semester", None)
                    
                    if opp_val == self:
                        setattr(item, "studyprogram_Semester", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "studyprogram_Semester"):
                    opp_val = getattr(item, "studyprogram_Semester", None)
                    
                    setattr(item, "studyprogram_Semester", self)
                    

    @property
    def studyprogram_Program20(self):
        return self.__studyprogram_Program20

    @studyprogram_Program20.setter
    def studyprogram_Program20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_studyprogram_Program__studyprogram_Program20", None)
        self.__studyprogram_Program20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyprogram_Department19"):
                opp_val = getattr(old_value, "studyprogram_Department19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyprogram_Department19"):
                opp_val = getattr(value, "studyprogram_Department19", None)
                if opp_val is None:
                    setattr(value, "studyprogram_Department19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
