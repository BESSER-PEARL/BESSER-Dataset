from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class StudyLevel(Enum):
    FIRST_YEAR = "FIRST_YEAR"
    SECOND_YEAR = "SECOND_YEAR"
    THIRD_YEAR = "THIRD_YEAR"
    SECOND_DEGREE = "SECOND_DEGREE"
    POST_GRAD = "POST_GRAD"
class SemesterType(Enum):
    Autumn = "Autumn"
    Spring = "Spring"
class CourseType(Enum):
    MANDATORY = "MANDATORY"
    ELECTIVE = "ELECTIVE"


############################################
# Definition of Classes
############################################

class programmes_University:

    def __init__(self, name: str, programmes_University: set["programmes_Programme"] = None, programmes_University15: set["programmes_Course"] = None):
        self.name = name
        self.programmes_University = programmes_University if programmes_University is not None else set()
        self.programmes_University15 = programmes_University15 if programmes_University15 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def programmes_University15(self):
        return self.__programmes_University15

    @programmes_University15.setter
    def programmes_University15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_programmes_University__programmes_University15", None)
        self.__programmes_University15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "programmes_Course16"):
                    opp_val = getattr(item, "programmes_Course16", None)
                    
                    if opp_val == self:
                        setattr(item, "programmes_Course16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "programmes_Course16"):
                    opp_val = getattr(item, "programmes_Course16", None)
                    
                    setattr(item, "programmes_Course16", self)
                    

    @property
    def programmes_University(self):
        return self.__programmes_University

    @programmes_University.setter
    def programmes_University(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_programmes_University__programmes_University", None)
        self.__programmes_University = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "programmes_Programme13"):
                    opp_val = getattr(item, "programmes_Programme13", None)
                    
                    if opp_val == self:
                        setattr(item, "programmes_Programme13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "programmes_Programme13"):
                    opp_val = getattr(item, "programmes_Programme13", None)
                    
                    setattr(item, "programmes_Programme13", self)
                    

class Programme:

    pass
class programmes_CourseGroup:

    def __init__(self, name: str, coursesType: str, programmes_CourseGroup: "programmes_Programme" = None, programmes_CourseGroup10: set["programmes_Course"] = None):
        self.name = name
        self.coursesType = coursesType
        self.programmes_CourseGroup = programmes_CourseGroup
        self.programmes_CourseGroup10 = programmes_CourseGroup10 if programmes_CourseGroup10 is not None else set()
        
    @property
    def coursesType(self) -> str:
        return self.__coursesType

    @coursesType.setter
    def coursesType(self, coursesType: str):
        self.__coursesType = coursesType

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def programmes_CourseGroup10(self):
        return self.__programmes_CourseGroup10

    @programmes_CourseGroup10.setter
    def programmes_CourseGroup10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_programmes_CourseGroup__programmes_CourseGroup10", None)
        self.__programmes_CourseGroup10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "programmes_Course11"):
                    opp_val = getattr(item, "programmes_Course11", None)
                    
                    if opp_val == self:
                        setattr(item, "programmes_Course11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "programmes_Course11"):
                    opp_val = getattr(item, "programmes_Course11", None)
                    
                    setattr(item, "programmes_Course11", self)
                    

    @property
    def programmes_CourseGroup(self):
        return self.__programmes_CourseGroup

    @programmes_CourseGroup.setter
    def programmes_CourseGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_programmes_CourseGroup__programmes_CourseGroup", None)
        self.__programmes_CourseGroup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "programmes_Programme"):
                opp_val = getattr(old_value, "programmes_Programme", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "programmes_Programme"):
                opp_val = getattr(value, "programmes_Programme", None)
                if opp_val is None:
                    setattr(value, "programmes_Programme", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class programmes_Semester:

    def __init__(self, year: int, semesterType: str, Semester: "programmes_Programme" = None, programmes_Semester: "programmes_Specialization" = None, programmeSemester: "programmes_Programme" = None, programmes_Semester8: set["programmes_Course"] = None):
        self.year = year
        self.semesterType = semesterType
        self.Semester = Semester
        self.programmes_Semester = programmes_Semester
        self.programmeSemester = programmeSemester
        self.programmes_Semester8 = programmes_Semester8 if programmes_Semester8 is not None else set()
        
    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, year: int):
        self.__year = year

    @property
    def semesterType(self) -> str:
        return self.__semesterType

    @semesterType.setter
    def semesterType(self, semesterType: str):
        self.__semesterType = semesterType

    @property
    def Semester(self):
        return self.__Semester

    @Semester.setter
    def Semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_programmes_Semester__Semester", None)
        self.__Semester = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "programme"):
                opp_val = getattr(old_value, "programme", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "programme"):
                opp_val = getattr(value, "programme", None)
                if opp_val is None:
                    setattr(value, "programme", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def programmes_Semester8(self):
        return self.__programmes_Semester8

    @programmes_Semester8.setter
    def programmes_Semester8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_programmes_Semester__programmes_Semester8", None)
        self.__programmes_Semester8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "programmes_Course"):
                    opp_val = getattr(item, "programmes_Course", None)
                    
                    if opp_val == self:
                        setattr(item, "programmes_Course", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "programmes_Course"):
                    opp_val = getattr(item, "programmes_Course", None)
                    
                    setattr(item, "programmes_Course", self)
                    

    @property
    def programmeSemester(self):
        return self.__programmeSemester

    @programmeSemester.setter
    def programmeSemester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_programmes_Semester__programmeSemester", None)
        self.__programmeSemester = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Programme6"):
                opp_val = getattr(old_value, "Programme6", None)
                if opp_val == self:
                    setattr(old_value, "Programme6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Programme6"):
                opp_val = getattr(value, "Programme6", None)
                setattr(value, "Programme6", self)

    @property
    def programmes_Semester(self):
        return self.__programmes_Semester

    @programmes_Semester.setter
    def programmes_Semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_programmes_Semester__programmes_Semester", None)
        self.__programmes_Semester = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "programmes_Specialization"):
                opp_val = getattr(old_value, "programmes_Specialization", None)
                if opp_val == self:
                    setattr(old_value, "programmes_Specialization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "programmes_Specialization"):
                opp_val = getattr(value, "programmes_Specialization", None)
                setattr(value, "programmes_Specialization", self)

class programmes_Specialization(Programme):

    pass
class programmes_Programme:

    def __init__(self, name: str, code: str, specializesIn: set["programmes_Specialization"] = None, programme: set["programmes_Semester"] = None, programmes_Programme: set["programmes_CourseGroup"] = None, Programme: "programmes_Specialization" = None, Programme6: "programmes_Semester" = None, programmes_Programme13: "programmes_University" = None):
        self.name = name
        self.code = code
        self.specializesIn = specializesIn if specializesIn is not None else set()
        self.programme = programme if programme is not None else set()
        self.programmes_Programme = programmes_Programme if programmes_Programme is not None else set()
        self.Programme = Programme
        self.Programme6 = Programme6
        self.programmes_Programme13 = programmes_Programme13
        
    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def specializesIn(self):
        return self.__specializesIn

    @specializesIn.setter
    def specializesIn(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_programmes_Programme__specializesIn", None)
        self.__specializesIn = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Specialization"):
                    opp_val = getattr(item, "Specialization", None)
                    
                    if opp_val == self:
                        setattr(item, "Specialization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Specialization"):
                    opp_val = getattr(item, "Specialization", None)
                    
                    setattr(item, "Specialization", self)
                    

    @property
    def Programme(self):
        return self.__Programme

    @Programme.setter
    def Programme(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_programmes_Programme__Programme", None)
        self.__Programme = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specializations"):
                opp_val = getattr(old_value, "specializations", None)
                if opp_val == self:
                    setattr(old_value, "specializations", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specializations"):
                opp_val = getattr(value, "specializations", None)
                setattr(value, "specializations", self)

    @property
    def programmes_Programme13(self):
        return self.__programmes_Programme13

    @programmes_Programme13.setter
    def programmes_Programme13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_programmes_Programme__programmes_Programme13", None)
        self.__programmes_Programme13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "programmes_University"):
                opp_val = getattr(old_value, "programmes_University", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "programmes_University"):
                opp_val = getattr(value, "programmes_University", None)
                if opp_val is None:
                    setattr(value, "programmes_University", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Programme6(self):
        return self.__Programme6

    @Programme6.setter
    def Programme6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_programmes_Programme__Programme6", None)
        self.__Programme6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "programmeSemester"):
                opp_val = getattr(old_value, "programmeSemester", None)
                if opp_val == self:
                    setattr(old_value, "programmeSemester", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "programmeSemester"):
                opp_val = getattr(value, "programmeSemester", None)
                setattr(value, "programmeSemester", self)

    @property
    def programme(self):
        return self.__programme

    @programme.setter
    def programme(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_programmes_Programme__programme", None)
        self.__programme = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Semester"):
                    opp_val = getattr(item, "Semester", None)
                    
                    if opp_val == self:
                        setattr(item, "Semester", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Semester"):
                    opp_val = getattr(item, "Semester", None)
                    
                    setattr(item, "Semester", self)
                    

    @property
    def programmes_Programme(self):
        return self.__programmes_Programme

    @programmes_Programme.setter
    def programmes_Programme(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_programmes_Programme__programmes_Programme", None)
        self.__programmes_Programme = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "programmes_CourseGroup"):
                    opp_val = getattr(item, "programmes_CourseGroup", None)
                    
                    if opp_val == self:
                        setattr(item, "programmes_CourseGroup", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "programmes_CourseGroup"):
                    opp_val = getattr(item, "programmes_CourseGroup", None)
                    
                    setattr(item, "programmes_CourseGroup", self)
                    

class programmes_Course:

    def __init__(self, code: str, name: str, credits: float, level: str, programmes_Course: "programmes_Semester" = None, programmes_Course11: "programmes_CourseGroup" = None, programmes_Course16: "programmes_University" = None):
        self.code = code
        self.name = name
        self.credits = credits
        self.level = level
        self.programmes_Course = programmes_Course
        self.programmes_Course11 = programmes_Course11
        self.programmes_Course16 = programmes_Course16
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level

    @property
    def credits(self) -> float:
        return self.__credits

    @credits.setter
    def credits(self, credits: float):
        self.__credits = credits

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def programmes_Course16(self):
        return self.__programmes_Course16

    @programmes_Course16.setter
    def programmes_Course16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_programmes_Course__programmes_Course16", None)
        self.__programmes_Course16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "programmes_University15"):
                opp_val = getattr(old_value, "programmes_University15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "programmes_University15"):
                opp_val = getattr(value, "programmes_University15", None)
                if opp_val is None:
                    setattr(value, "programmes_University15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def programmes_Course11(self):
        return self.__programmes_Course11

    @programmes_Course11.setter
    def programmes_Course11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_programmes_Course__programmes_Course11", None)
        self.__programmes_Course11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "programmes_CourseGroup10"):
                opp_val = getattr(old_value, "programmes_CourseGroup10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "programmes_CourseGroup10"):
                opp_val = getattr(value, "programmes_CourseGroup10", None)
                if opp_val is None:
                    setattr(value, "programmes_CourseGroup10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def programmes_Course(self):
        return self.__programmes_Course

    @programmes_Course.setter
    def programmes_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_programmes_Course__programmes_Course", None)
        self.__programmes_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "programmes_Semester8"):
                opp_val = getattr(old_value, "programmes_Semester8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "programmes_Semester8"):
                opp_val = getattr(value, "programmes_Semester8", None)
                if opp_val is None:
                    setattr(value, "programmes_Semester8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
