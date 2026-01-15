from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Fall_or_spring(Enum):
    Fall = "Fall"
    Spring = "Spring"


############################################
# Definition of Classes
############################################

class tDT4250_asssignment1_2_Department:

    def __init__(self, Name: str, tDT4250_asssignment1_2_Department: set["tDT4250_asssignment1_2_Course"] = None, tDT4250_asssignment1_2_Department21: set["tDT4250_asssignment1_2_Program"] = None):
        self.Name = Name
        self.tDT4250_asssignment1_2_Department = tDT4250_asssignment1_2_Department if tDT4250_asssignment1_2_Department is not None else set()
        self.tDT4250_asssignment1_2_Department21 = tDT4250_asssignment1_2_Department21 if tDT4250_asssignment1_2_Department21 is not None else set()
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def tDT4250_asssignment1_2_Department21(self):
        return self.__tDT4250_asssignment1_2_Department21

    @tDT4250_asssignment1_2_Department21.setter
    def tDT4250_asssignment1_2_Department21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tDT4250_asssignment1_2_Department__tDT4250_asssignment1_2_Department21", None)
        self.__tDT4250_asssignment1_2_Department21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tDT4250_asssignment1_2_Program22"):
                    opp_val = getattr(item, "tDT4250_asssignment1_2_Program22", None)
                    
                    if opp_val == self:
                        setattr(item, "tDT4250_asssignment1_2_Program22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tDT4250_asssignment1_2_Program22"):
                    opp_val = getattr(item, "tDT4250_asssignment1_2_Program22", None)
                    
                    setattr(item, "tDT4250_asssignment1_2_Program22", self)
                    

    @property
    def tDT4250_asssignment1_2_Department(self):
        return self.__tDT4250_asssignment1_2_Department

    @tDT4250_asssignment1_2_Department.setter
    def tDT4250_asssignment1_2_Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tDT4250_asssignment1_2_Department__tDT4250_asssignment1_2_Department", None)
        self.__tDT4250_asssignment1_2_Department = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tDT4250_asssignment1_2_Course19"):
                    opp_val = getattr(item, "tDT4250_asssignment1_2_Course19", None)
                    
                    if opp_val == self:
                        setattr(item, "tDT4250_asssignment1_2_Course19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tDT4250_asssignment1_2_Course19"):
                    opp_val = getattr(item, "tDT4250_asssignment1_2_Course19", None)
                    
                    setattr(item, "tDT4250_asssignment1_2_Course19", self)
                    

class tDT4250_asssignment1_2_Semester:

    def __init__(self, Number: int, Credits: str, tDT4250_asssignment1_2_Semester7: "tDT4250_asssignment1_2_Specialization" = None, tDT4250_asssignment1_2_Semester12: set["tDT4250_asssignment1_2_Semester_Course"] = None, tDT4250_asssignment1_2_Semester: "tDT4250_asssignment1_2_Program" = None):
        self.Number = Number
        self.Credits = Credits
        self.tDT4250_asssignment1_2_Semester7 = tDT4250_asssignment1_2_Semester7
        self.tDT4250_asssignment1_2_Semester12 = tDT4250_asssignment1_2_Semester12 if tDT4250_asssignment1_2_Semester12 is not None else set()
        self.tDT4250_asssignment1_2_Semester = tDT4250_asssignment1_2_Semester
        
    @property
    def Credits(self) -> str:
        return self.__Credits

    @Credits.setter
    def Credits(self, Credits: str):
        self.__Credits = Credits

    @property
    def Number(self) -> int:
        return self.__Number

    @Number.setter
    def Number(self, Number: int):
        self.__Number = Number

    @property
    def tDT4250_asssignment1_2_Semester12(self):
        return self.__tDT4250_asssignment1_2_Semester12

    @tDT4250_asssignment1_2_Semester12.setter
    def tDT4250_asssignment1_2_Semester12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tDT4250_asssignment1_2_Semester__tDT4250_asssignment1_2_Semester12", None)
        self.__tDT4250_asssignment1_2_Semester12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tDT4250_asssignment1_2_Semester_Course"):
                    opp_val = getattr(item, "tDT4250_asssignment1_2_Semester_Course", None)
                    
                    if opp_val == self:
                        setattr(item, "tDT4250_asssignment1_2_Semester_Course", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tDT4250_asssignment1_2_Semester_Course"):
                    opp_val = getattr(item, "tDT4250_asssignment1_2_Semester_Course", None)
                    
                    setattr(item, "tDT4250_asssignment1_2_Semester_Course", self)
                    

    @property
    def tDT4250_asssignment1_2_Semester(self):
        return self.__tDT4250_asssignment1_2_Semester

    @tDT4250_asssignment1_2_Semester.setter
    def tDT4250_asssignment1_2_Semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tDT4250_asssignment1_2_Semester__tDT4250_asssignment1_2_Semester", None)
        self.__tDT4250_asssignment1_2_Semester = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tDT4250_asssignment1_2_Program4"):
                opp_val = getattr(old_value, "tDT4250_asssignment1_2_Program4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tDT4250_asssignment1_2_Program4"):
                opp_val = getattr(value, "tDT4250_asssignment1_2_Program4", None)
                if opp_val is None:
                    setattr(value, "tDT4250_asssignment1_2_Program4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tDT4250_asssignment1_2_Semester7(self):
        return self.__tDT4250_asssignment1_2_Semester7

    @tDT4250_asssignment1_2_Semester7.setter
    def tDT4250_asssignment1_2_Semester7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tDT4250_asssignment1_2_Semester__tDT4250_asssignment1_2_Semester7", None)
        self.__tDT4250_asssignment1_2_Semester7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tDT4250_asssignment1_2_Specialization6"):
                opp_val = getattr(old_value, "tDT4250_asssignment1_2_Specialization6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tDT4250_asssignment1_2_Specialization6"):
                opp_val = getattr(value, "tDT4250_asssignment1_2_Specialization6", None)
                if opp_val is None:
                    setattr(value, "tDT4250_asssignment1_2_Specialization6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tDT4250_asssignment1_2_Course:

    def __init__(self, Name: str, Code: str, Credits: float, StartDate: str, ExamDate: str, tDT4250_asssignment1_2_Course: "tDT4250_asssignment1_2_Semester_Course" = None, tDT4250_asssignment1_2_Course17: "tDT4250_asssignment1_2_Program_course" = None, tDT4250_asssignment1_2_Course19: "tDT4250_asssignment1_2_Department" = None):
        self.Name = Name
        self.Code = Code
        self.Credits = Credits
        self.StartDate = StartDate
        self.ExamDate = ExamDate
        self.tDT4250_asssignment1_2_Course = tDT4250_asssignment1_2_Course
        self.tDT4250_asssignment1_2_Course17 = tDT4250_asssignment1_2_Course17
        self.tDT4250_asssignment1_2_Course19 = tDT4250_asssignment1_2_Course19
        
    @property
    def StartDate(self) -> str:
        return self.__StartDate

    @StartDate.setter
    def StartDate(self, StartDate: str):
        self.__StartDate = StartDate

    @property
    def Code(self) -> str:
        return self.__Code

    @Code.setter
    def Code(self, Code: str):
        self.__Code = Code

    @property
    def Credits(self) -> float:
        return self.__Credits

    @Credits.setter
    def Credits(self, Credits: float):
        self.__Credits = Credits

    @property
    def ExamDate(self) -> str:
        return self.__ExamDate

    @ExamDate.setter
    def ExamDate(self, ExamDate: str):
        self.__ExamDate = ExamDate

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def tDT4250_asssignment1_2_Course(self):
        return self.__tDT4250_asssignment1_2_Course

    @tDT4250_asssignment1_2_Course.setter
    def tDT4250_asssignment1_2_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tDT4250_asssignment1_2_Course__tDT4250_asssignment1_2_Course", None)
        self.__tDT4250_asssignment1_2_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tDT4250_asssignment1_2_Semester_Course14"):
                opp_val = getattr(old_value, "tDT4250_asssignment1_2_Semester_Course14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tDT4250_asssignment1_2_Semester_Course14"):
                opp_val = getattr(value, "tDT4250_asssignment1_2_Semester_Course14", None)
                if opp_val is None:
                    setattr(value, "tDT4250_asssignment1_2_Semester_Course14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tDT4250_asssignment1_2_Course19(self):
        return self.__tDT4250_asssignment1_2_Course19

    @tDT4250_asssignment1_2_Course19.setter
    def tDT4250_asssignment1_2_Course19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tDT4250_asssignment1_2_Course__tDT4250_asssignment1_2_Course19", None)
        self.__tDT4250_asssignment1_2_Course19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tDT4250_asssignment1_2_Department"):
                opp_val = getattr(old_value, "tDT4250_asssignment1_2_Department", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tDT4250_asssignment1_2_Department"):
                opp_val = getattr(value, "tDT4250_asssignment1_2_Department", None)
                if opp_val is None:
                    setattr(value, "tDT4250_asssignment1_2_Department", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tDT4250_asssignment1_2_Course17(self):
        return self.__tDT4250_asssignment1_2_Course17

    @tDT4250_asssignment1_2_Course17.setter
    def tDT4250_asssignment1_2_Course17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tDT4250_asssignment1_2_Course__tDT4250_asssignment1_2_Course17", None)
        self.__tDT4250_asssignment1_2_Course17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tDT4250_asssignment1_2_Program_course16"):
                opp_val = getattr(old_value, "tDT4250_asssignment1_2_Program_course16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tDT4250_asssignment1_2_Program_course16"):
                opp_val = getattr(value, "tDT4250_asssignment1_2_Program_course16", None)
                if opp_val is None:
                    setattr(value, "tDT4250_asssignment1_2_Program_course16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tDT4250_asssignment1_2_Semester_Course:

    def __init__(self, Mandatory: bool, Fall_or_spring: str, tDT4250_asssignment1_2_Semester_Course: "tDT4250_asssignment1_2_Semester" = None, tDT4250_asssignment1_2_Semester_Course14: set["tDT4250_asssignment1_2_Course"] = None):
        self.Mandatory = Mandatory
        self.Fall_or_spring = Fall_or_spring
        self.tDT4250_asssignment1_2_Semester_Course = tDT4250_asssignment1_2_Semester_Course
        self.tDT4250_asssignment1_2_Semester_Course14 = tDT4250_asssignment1_2_Semester_Course14 if tDT4250_asssignment1_2_Semester_Course14 is not None else set()
        
    @property
    def Mandatory(self) -> bool:
        return self.__Mandatory

    @Mandatory.setter
    def Mandatory(self, Mandatory: bool):
        self.__Mandatory = Mandatory

    @property
    def Fall_or_spring(self) -> str:
        return self.__Fall_or_spring

    @Fall_or_spring.setter
    def Fall_or_spring(self, Fall_or_spring: str):
        self.__Fall_or_spring = Fall_or_spring

    @property
    def tDT4250_asssignment1_2_Semester_Course14(self):
        return self.__tDT4250_asssignment1_2_Semester_Course14

    @tDT4250_asssignment1_2_Semester_Course14.setter
    def tDT4250_asssignment1_2_Semester_Course14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tDT4250_asssignment1_2_Semester_Course__tDT4250_asssignment1_2_Semester_Course14", None)
        self.__tDT4250_asssignment1_2_Semester_Course14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tDT4250_asssignment1_2_Course"):
                    opp_val = getattr(item, "tDT4250_asssignment1_2_Course", None)
                    
                    if opp_val == self:
                        setattr(item, "tDT4250_asssignment1_2_Course", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tDT4250_asssignment1_2_Course"):
                    opp_val = getattr(item, "tDT4250_asssignment1_2_Course", None)
                    
                    setattr(item, "tDT4250_asssignment1_2_Course", self)
                    

    @property
    def tDT4250_asssignment1_2_Semester_Course(self):
        return self.__tDT4250_asssignment1_2_Semester_Course

    @tDT4250_asssignment1_2_Semester_Course.setter
    def tDT4250_asssignment1_2_Semester_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tDT4250_asssignment1_2_Semester_Course__tDT4250_asssignment1_2_Semester_Course", None)
        self.__tDT4250_asssignment1_2_Semester_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tDT4250_asssignment1_2_Semester12"):
                opp_val = getattr(old_value, "tDT4250_asssignment1_2_Semester12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tDT4250_asssignment1_2_Semester12"):
                opp_val = getattr(value, "tDT4250_asssignment1_2_Semester12", None)
                if opp_val is None:
                    setattr(value, "tDT4250_asssignment1_2_Semester12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tDT4250_asssignment1_2_Program_course:

    def __init__(self, Fall_or_spring: str, Mandatory: bool, tDT4250_asssignment1_2_Program_course: "tDT4250_asssignment1_2_Program" = None, tDT4250_asssignment1_2_Program_course16: set["tDT4250_asssignment1_2_Course"] = None):
        self.Fall_or_spring = Fall_or_spring
        self.Mandatory = Mandatory
        self.tDT4250_asssignment1_2_Program_course = tDT4250_asssignment1_2_Program_course
        self.tDT4250_asssignment1_2_Program_course16 = tDT4250_asssignment1_2_Program_course16 if tDT4250_asssignment1_2_Program_course16 is not None else set()
        
    @property
    def Fall_or_spring(self) -> str:
        return self.__Fall_or_spring

    @Fall_or_spring.setter
    def Fall_or_spring(self, Fall_or_spring: str):
        self.__Fall_or_spring = Fall_or_spring

    @property
    def Mandatory(self) -> bool:
        return self.__Mandatory

    @Mandatory.setter
    def Mandatory(self, Mandatory: bool):
        self.__Mandatory = Mandatory

    @property
    def tDT4250_asssignment1_2_Program_course16(self):
        return self.__tDT4250_asssignment1_2_Program_course16

    @tDT4250_asssignment1_2_Program_course16.setter
    def tDT4250_asssignment1_2_Program_course16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tDT4250_asssignment1_2_Program_course__tDT4250_asssignment1_2_Program_course16", None)
        self.__tDT4250_asssignment1_2_Program_course16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tDT4250_asssignment1_2_Course17"):
                    opp_val = getattr(item, "tDT4250_asssignment1_2_Course17", None)
                    
                    if opp_val == self:
                        setattr(item, "tDT4250_asssignment1_2_Course17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tDT4250_asssignment1_2_Course17"):
                    opp_val = getattr(item, "tDT4250_asssignment1_2_Course17", None)
                    
                    setattr(item, "tDT4250_asssignment1_2_Course17", self)
                    

    @property
    def tDT4250_asssignment1_2_Program_course(self):
        return self.__tDT4250_asssignment1_2_Program_course

    @tDT4250_asssignment1_2_Program_course.setter
    def tDT4250_asssignment1_2_Program_course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tDT4250_asssignment1_2_Program_course__tDT4250_asssignment1_2_Program_course", None)
        self.__tDT4250_asssignment1_2_Program_course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tDT4250_asssignment1_2_Program2"):
                opp_val = getattr(old_value, "tDT4250_asssignment1_2_Program2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tDT4250_asssignment1_2_Program2"):
                opp_val = getattr(value, "tDT4250_asssignment1_2_Program2", None)
                if opp_val is None:
                    setattr(value, "tDT4250_asssignment1_2_Program2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tDT4250_asssignment1_2_Specialization:

    def __init__(self, Name: str, tDT4250_asssignment1_2_Specialization: "tDT4250_asssignment1_2_Program" = None, tDT4250_asssignment1_2_Specialization6: set["tDT4250_asssignment1_2_Semester"] = None, tDT4250_asssignment1_2_Specialization10: "tDT4250_asssignment1_2_Specialization" = None, tDT4250_asssignment1_2_Specialization8: set["tDT4250_asssignment1_2_Specialization"] = None):
        self.Name = Name
        self.tDT4250_asssignment1_2_Specialization = tDT4250_asssignment1_2_Specialization
        self.tDT4250_asssignment1_2_Specialization6 = tDT4250_asssignment1_2_Specialization6 if tDT4250_asssignment1_2_Specialization6 is not None else set()
        self.tDT4250_asssignment1_2_Specialization10 = tDT4250_asssignment1_2_Specialization10
        self.tDT4250_asssignment1_2_Specialization8 = tDT4250_asssignment1_2_Specialization8 if tDT4250_asssignment1_2_Specialization8 is not None else set()
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def tDT4250_asssignment1_2_Specialization6(self):
        return self.__tDT4250_asssignment1_2_Specialization6

    @tDT4250_asssignment1_2_Specialization6.setter
    def tDT4250_asssignment1_2_Specialization6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tDT4250_asssignment1_2_Specialization__tDT4250_asssignment1_2_Specialization6", None)
        self.__tDT4250_asssignment1_2_Specialization6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tDT4250_asssignment1_2_Semester7"):
                    opp_val = getattr(item, "tDT4250_asssignment1_2_Semester7", None)
                    
                    if opp_val == self:
                        setattr(item, "tDT4250_asssignment1_2_Semester7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tDT4250_asssignment1_2_Semester7"):
                    opp_val = getattr(item, "tDT4250_asssignment1_2_Semester7", None)
                    
                    setattr(item, "tDT4250_asssignment1_2_Semester7", self)
                    

    @property
    def tDT4250_asssignment1_2_Specialization10(self):
        return self.__tDT4250_asssignment1_2_Specialization10

    @tDT4250_asssignment1_2_Specialization10.setter
    def tDT4250_asssignment1_2_Specialization10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tDT4250_asssignment1_2_Specialization__tDT4250_asssignment1_2_Specialization10", None)
        self.__tDT4250_asssignment1_2_Specialization10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tDT4250_asssignment1_2_Specialization8"):
                opp_val = getattr(old_value, "tDT4250_asssignment1_2_Specialization8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tDT4250_asssignment1_2_Specialization8"):
                opp_val = getattr(value, "tDT4250_asssignment1_2_Specialization8", None)
                if opp_val is None:
                    setattr(value, "tDT4250_asssignment1_2_Specialization8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tDT4250_asssignment1_2_Specialization8(self):
        return self.__tDT4250_asssignment1_2_Specialization8

    @tDT4250_asssignment1_2_Specialization8.setter
    def tDT4250_asssignment1_2_Specialization8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tDT4250_asssignment1_2_Specialization__tDT4250_asssignment1_2_Specialization8", None)
        self.__tDT4250_asssignment1_2_Specialization8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tDT4250_asssignment1_2_Specialization10"):
                    opp_val = getattr(item, "tDT4250_asssignment1_2_Specialization10", None)
                    
                    if opp_val == self:
                        setattr(item, "tDT4250_asssignment1_2_Specialization10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tDT4250_asssignment1_2_Specialization10"):
                    opp_val = getattr(item, "tDT4250_asssignment1_2_Specialization10", None)
                    
                    setattr(item, "tDT4250_asssignment1_2_Specialization10", self)
                    

    @property
    def tDT4250_asssignment1_2_Specialization(self):
        return self.__tDT4250_asssignment1_2_Specialization

    @tDT4250_asssignment1_2_Specialization.setter
    def tDT4250_asssignment1_2_Specialization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tDT4250_asssignment1_2_Specialization__tDT4250_asssignment1_2_Specialization", None)
        self.__tDT4250_asssignment1_2_Specialization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tDT4250_asssignment1_2_Program"):
                opp_val = getattr(old_value, "tDT4250_asssignment1_2_Program", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tDT4250_asssignment1_2_Program"):
                opp_val = getattr(value, "tDT4250_asssignment1_2_Program", None)
                if opp_val is None:
                    setattr(value, "tDT4250_asssignment1_2_Program", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tDT4250_asssignment1_2_Program:

    def __init__(self, Name: str, Credits: str, tDT4250_asssignment1_2_Program: set["tDT4250_asssignment1_2_Specialization"] = None, tDT4250_asssignment1_2_Program2: set["tDT4250_asssignment1_2_Program_course"] = None, tDT4250_asssignment1_2_Program4: set["tDT4250_asssignment1_2_Semester"] = None, tDT4250_asssignment1_2_Program22: "tDT4250_asssignment1_2_Department" = None):
        self.Name = Name
        self.Credits = Credits
        self.tDT4250_asssignment1_2_Program = tDT4250_asssignment1_2_Program if tDT4250_asssignment1_2_Program is not None else set()
        self.tDT4250_asssignment1_2_Program2 = tDT4250_asssignment1_2_Program2 if tDT4250_asssignment1_2_Program2 is not None else set()
        self.tDT4250_asssignment1_2_Program4 = tDT4250_asssignment1_2_Program4 if tDT4250_asssignment1_2_Program4 is not None else set()
        self.tDT4250_asssignment1_2_Program22 = tDT4250_asssignment1_2_Program22
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Credits(self) -> str:
        return self.__Credits

    @Credits.setter
    def Credits(self, Credits: str):
        self.__Credits = Credits

    @property
    def tDT4250_asssignment1_2_Program22(self):
        return self.__tDT4250_asssignment1_2_Program22

    @tDT4250_asssignment1_2_Program22.setter
    def tDT4250_asssignment1_2_Program22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tDT4250_asssignment1_2_Program__tDT4250_asssignment1_2_Program22", None)
        self.__tDT4250_asssignment1_2_Program22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tDT4250_asssignment1_2_Department21"):
                opp_val = getattr(old_value, "tDT4250_asssignment1_2_Department21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tDT4250_asssignment1_2_Department21"):
                opp_val = getattr(value, "tDT4250_asssignment1_2_Department21", None)
                if opp_val is None:
                    setattr(value, "tDT4250_asssignment1_2_Department21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tDT4250_asssignment1_2_Program(self):
        return self.__tDT4250_asssignment1_2_Program

    @tDT4250_asssignment1_2_Program.setter
    def tDT4250_asssignment1_2_Program(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tDT4250_asssignment1_2_Program__tDT4250_asssignment1_2_Program", None)
        self.__tDT4250_asssignment1_2_Program = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tDT4250_asssignment1_2_Specialization"):
                    opp_val = getattr(item, "tDT4250_asssignment1_2_Specialization", None)
                    
                    if opp_val == self:
                        setattr(item, "tDT4250_asssignment1_2_Specialization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tDT4250_asssignment1_2_Specialization"):
                    opp_val = getattr(item, "tDT4250_asssignment1_2_Specialization", None)
                    
                    setattr(item, "tDT4250_asssignment1_2_Specialization", self)
                    

    @property
    def tDT4250_asssignment1_2_Program2(self):
        return self.__tDT4250_asssignment1_2_Program2

    @tDT4250_asssignment1_2_Program2.setter
    def tDT4250_asssignment1_2_Program2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tDT4250_asssignment1_2_Program__tDT4250_asssignment1_2_Program2", None)
        self.__tDT4250_asssignment1_2_Program2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tDT4250_asssignment1_2_Program_course"):
                    opp_val = getattr(item, "tDT4250_asssignment1_2_Program_course", None)
                    
                    if opp_val == self:
                        setattr(item, "tDT4250_asssignment1_2_Program_course", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tDT4250_asssignment1_2_Program_course"):
                    opp_val = getattr(item, "tDT4250_asssignment1_2_Program_course", None)
                    
                    setattr(item, "tDT4250_asssignment1_2_Program_course", self)
                    

    @property
    def tDT4250_asssignment1_2_Program4(self):
        return self.__tDT4250_asssignment1_2_Program4

    @tDT4250_asssignment1_2_Program4.setter
    def tDT4250_asssignment1_2_Program4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tDT4250_asssignment1_2_Program__tDT4250_asssignment1_2_Program4", None)
        self.__tDT4250_asssignment1_2_Program4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tDT4250_asssignment1_2_Semester"):
                    opp_val = getattr(item, "tDT4250_asssignment1_2_Semester", None)
                    
                    if opp_val == self:
                        setattr(item, "tDT4250_asssignment1_2_Semester", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tDT4250_asssignment1_2_Semester"):
                    opp_val = getattr(item, "tDT4250_asssignment1_2_Semester", None)
                    
                    setattr(item, "tDT4250_asssignment1_2_Semester", self)
                    
