from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class programmeCode(Enum):
    Datateknologi5 = "Datateknologi5"
    Informatikk = "Informatikk"
    Datateknologi2 = "Datateknologi2"


############################################
# Definition of Classes
############################################

class ra_Semester:

    def __init__(self, totalPoints: float, semesterNumber: int, ra_Semester: "ra_StudyPlan" = None, ra_Semester19: "ra_Specialization" = None, ra_Semester21: set["ra_Course"] = None, semester: set["ra_MandatoryCourse"] = None, Semester: "ra_MandatoryCourse" = None):
        self.totalPoints = totalPoints
        self.semesterNumber = semesterNumber
        self.ra_Semester = ra_Semester
        self.ra_Semester19 = ra_Semester19
        self.ra_Semester21 = ra_Semester21 if ra_Semester21 is not None else set()
        self.semester = semester if semester is not None else set()
        self.Semester = Semester
        
    @property
    def totalPoints(self) -> float:
        return self.__totalPoints

    @totalPoints.setter
    def totalPoints(self, totalPoints: float):
        self.__totalPoints = totalPoints

    @property
    def semesterNumber(self) -> int:
        return self.__semesterNumber

    @semesterNumber.setter
    def semesterNumber(self, semesterNumber: int):
        self.__semesterNumber = semesterNumber

    @property
    def Semester(self):
        return self.__Semester

    @Semester.setter
    def Semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ra_Semester__Semester", None)
        self.__Semester = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mandatoryCourse"):
                opp_val = getattr(old_value, "mandatoryCourse", None)
                if opp_val == self:
                    setattr(old_value, "mandatoryCourse", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mandatoryCourse"):
                opp_val = getattr(value, "mandatoryCourse", None)
                setattr(value, "mandatoryCourse", self)

    @property
    def ra_Semester21(self):
        return self.__ra_Semester21

    @ra_Semester21.setter
    def ra_Semester21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ra_Semester__ra_Semester21", None)
        self.__ra_Semester21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ra_Course22"):
                    opp_val = getattr(item, "ra_Course22", None)
                    
                    if opp_val == self:
                        setattr(item, "ra_Course22", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ra_Course22"):
                    opp_val = getattr(item, "ra_Course22", None)
                    
                    setattr(item, "ra_Course22", self)
                    

    @property
    def ra_Semester19(self):
        return self.__ra_Semester19

    @ra_Semester19.setter
    def ra_Semester19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ra_Semester__ra_Semester19", None)
        self.__ra_Semester19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ra_Specialization18"):
                opp_val = getattr(old_value, "ra_Specialization18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ra_Specialization18"):
                opp_val = getattr(value, "ra_Specialization18", None)
                if opp_val is None:
                    setattr(value, "ra_Specialization18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def semester(self):
        return self.__semester

    @semester.setter
    def semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ra_Semester__semester", None)
        self.__semester = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "MandatoryCourse24"):
                    opp_val = getattr(item, "MandatoryCourse24", None)
                    
                    if opp_val == self:
                        setattr(item, "MandatoryCourse24", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "MandatoryCourse24"):
                    opp_val = getattr(item, "MandatoryCourse24", None)
                    
                    setattr(item, "MandatoryCourse24", self)
                    

    @property
    def ra_Semester(self):
        return self.__ra_Semester

    @ra_Semester.setter
    def ra_Semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ra_Semester__ra_Semester", None)
        self.__ra_Semester = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ra_StudyPlan14"):
                opp_val = getattr(old_value, "ra_StudyPlan14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ra_StudyPlan14"):
                opp_val = getattr(value, "ra_StudyPlan14", None)
                if opp_val is None:
                    setattr(value, "ra_StudyPlan14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ra_MandatoryCourse:

    def __init__(self, mandatory: bool, credit: float, MandatoryCourse: "ra_Course" = None, ra_MandatoryCourse: "ra_StudyPlan" = None, MandatoryCourse24: "ra_Semester" = None, mandatoryCourse: "ra_Semester" = None, mandatoryCourse27: "ra_Course" = None):
        self.mandatory = mandatory
        self.credit = credit
        self.MandatoryCourse = MandatoryCourse
        self.ra_MandatoryCourse = ra_MandatoryCourse
        self.MandatoryCourse24 = MandatoryCourse24
        self.mandatoryCourse = mandatoryCourse
        self.mandatoryCourse27 = mandatoryCourse27
        
    @property
    def mandatory(self) -> bool:
        return self.__mandatory

    @mandatory.setter
    def mandatory(self, mandatory: bool):
        self.__mandatory = mandatory

    @property
    def credit(self) -> float:
        return self.__credit

    @credit.setter
    def credit(self, credit: float):
        self.__credit = credit

    @property
    def mandatoryCourse27(self):
        return self.__mandatoryCourse27

    @mandatoryCourse27.setter
    def mandatoryCourse27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ra_MandatoryCourse__mandatoryCourse27", None)
        self.__mandatoryCourse27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Course"):
                opp_val = getattr(old_value, "Course", None)
                if opp_val == self:
                    setattr(old_value, "Course", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Course"):
                opp_val = getattr(value, "Course", None)
                setattr(value, "Course", self)

    @property
    def ra_MandatoryCourse(self):
        return self.__ra_MandatoryCourse

    @ra_MandatoryCourse.setter
    def ra_MandatoryCourse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ra_MandatoryCourse__ra_MandatoryCourse", None)
        self.__ra_MandatoryCourse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ra_StudyPlan16"):
                opp_val = getattr(old_value, "ra_StudyPlan16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ra_StudyPlan16"):
                opp_val = getattr(value, "ra_StudyPlan16", None)
                if opp_val is None:
                    setattr(value, "ra_StudyPlan16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def mandatoryCourse(self):
        return self.__mandatoryCourse

    @mandatoryCourse.setter
    def mandatoryCourse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ra_MandatoryCourse__mandatoryCourse", None)
        self.__mandatoryCourse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Semester"):
                opp_val = getattr(old_value, "Semester", None)
                if opp_val == self:
                    setattr(old_value, "Semester", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Semester"):
                opp_val = getattr(value, "Semester", None)
                setattr(value, "Semester", self)

    @property
    def MandatoryCourse24(self):
        return self.__MandatoryCourse24

    @MandatoryCourse24.setter
    def MandatoryCourse24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ra_MandatoryCourse__MandatoryCourse24", None)
        self.__MandatoryCourse24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "semester"):
                opp_val = getattr(old_value, "semester", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "semester"):
                opp_val = getattr(value, "semester", None)
                if opp_val is None:
                    setattr(value, "semester", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def MandatoryCourse(self):
        return self.__MandatoryCourse

    @MandatoryCourse.setter
    def MandatoryCourse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ra_MandatoryCourse__MandatoryCourse", None)
        self.__MandatoryCourse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course"):
                opp_val = getattr(old_value, "course", None)
                if opp_val == self:
                    setattr(old_value, "course", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course"):
                opp_val = getattr(value, "course", None)
                setattr(value, "course", self)

class ra_Specialization:

    def __init__(self, name: str, ra_Specialization: "ra_Department" = None, ra_Specialization12: "ra_StudyPlan" = None, ra_Specialization18: set["ra_Semester"] = None):
        self.name = name
        self.ra_Specialization = ra_Specialization
        self.ra_Specialization12 = ra_Specialization12
        self.ra_Specialization18 = ra_Specialization18 if ra_Specialization18 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ra_Specialization18(self):
        return self.__ra_Specialization18

    @ra_Specialization18.setter
    def ra_Specialization18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ra_Specialization__ra_Specialization18", None)
        self.__ra_Specialization18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "ra_Semester19"):
                    opp_val = getattr(item, "ra_Semester19", None)
                    
                    if opp_val == self:
                        setattr(item, "ra_Semester19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "ra_Semester19"):
                    opp_val = getattr(item, "ra_Semester19", None)
                    
                    setattr(item, "ra_Semester19", self)
                    

    @property
    def ra_Specialization12(self):
        return self.__ra_Specialization12

    @ra_Specialization12.setter
    def ra_Specialization12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ra_Specialization__ra_Specialization12", None)
        self.__ra_Specialization12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ra_StudyPlan11"):
                opp_val = getattr(old_value, "ra_StudyPlan11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ra_StudyPlan11"):
                opp_val = getattr(value, "ra_StudyPlan11", None)
                if opp_val is None:
                    setattr(value, "ra_StudyPlan11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ra_Specialization(self):
        return self.__ra_Specialization

    @ra_Specialization.setter
    def ra_Specialization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ra_Specialization__ra_Specialization", None)
        self.__ra_Specialization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ra_Department6"):
                opp_val = getattr(old_value, "ra_Department6", None)
                if opp_val == self:
                    setattr(old_value, "ra_Department6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ra_Department6"):
                opp_val = getattr(value, "ra_Department6", None)
                setattr(value, "ra_Department6", self)

class ra_StudyPlan:

    pass
class ra_Course:

    def __init__(self, name: str, code: str, ra_Course: "ra_Department" = None, course: "ra_MandatoryCourse" = None, ra_Course22: "ra_Semester" = None, Course: "ra_MandatoryCourse" = None):
        self.name = name
        self.code = code
        self.ra_Course = ra_Course
        self.course = course
        self.ra_Course22 = ra_Course22
        self.Course = Course
        
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
    def ra_Course22(self):
        return self.__ra_Course22

    @ra_Course22.setter
    def ra_Course22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ra_Course__ra_Course22", None)
        self.__ra_Course22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ra_Semester21"):
                opp_val = getattr(old_value, "ra_Semester21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ra_Semester21"):
                opp_val = getattr(value, "ra_Semester21", None)
                if opp_val is None:
                    setattr(value, "ra_Semester21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def ra_Course(self):
        return self.__ra_Course

    @ra_Course.setter
    def ra_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ra_Course__ra_Course", None)
        self.__ra_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ra_Department2"):
                opp_val = getattr(old_value, "ra_Department2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ra_Department2"):
                opp_val = getattr(value, "ra_Department2", None)
                if opp_val is None:
                    setattr(value, "ra_Department2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ra_Course__course", None)
        self.__course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "MandatoryCourse"):
                opp_val = getattr(old_value, "MandatoryCourse", None)
                if opp_val == self:
                    setattr(old_value, "MandatoryCourse", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "MandatoryCourse"):
                opp_val = getattr(value, "MandatoryCourse", None)
                setattr(value, "MandatoryCourse", self)

    @property
    def Course(self):
        return self.__Course

    @Course.setter
    def Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ra_Course__Course", None)
        self.__Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "mandatoryCourse27"):
                opp_val = getattr(old_value, "mandatoryCourse27", None)
                if opp_val == self:
                    setattr(old_value, "mandatoryCourse27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "mandatoryCourse27"):
                opp_val = getattr(value, "mandatoryCourse27", None)
                setattr(value, "mandatoryCourse27", self)

class ra_Programme:

    def __init__(self, name: str, mCode: str, ra_Programme: "ra_Department" = None, Programme: "ra_StudyPlan" = None, programme: "ra_StudyPlan" = None):
        self.name = name
        self.mCode = mCode
        self.ra_Programme = ra_Programme
        self.Programme = Programme
        self.programme = programme
        
    @property
    def mCode(self) -> str:
        return self.__mCode

    @mCode.setter
    def mCode(self, mCode: str):
        self.__mCode = mCode

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def programme(self):
        return self.__programme

    @programme.setter
    def programme(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ra_Programme__programme", None)
        self.__programme = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StudyPlan"):
                opp_val = getattr(old_value, "StudyPlan", None)
                if opp_val == self:
                    setattr(old_value, "StudyPlan", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StudyPlan"):
                opp_val = getattr(value, "StudyPlan", None)
                setattr(value, "StudyPlan", self)

    @property
    def ra_Programme(self):
        return self.__ra_Programme

    @ra_Programme.setter
    def ra_Programme(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ra_Programme__ra_Programme", None)
        self.__ra_Programme = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ra_Department"):
                opp_val = getattr(old_value, "ra_Department", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ra_Department"):
                opp_val = getattr(value, "ra_Department", None)
                if opp_val is None:
                    setattr(value, "ra_Department", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Programme(self):
        return self.__Programme

    @Programme.setter
    def Programme(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ra_Programme__Programme", None)
        self.__Programme = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyPlan"):
                opp_val = getattr(old_value, "studyPlan", None)
                if opp_val == self:
                    setattr(old_value, "studyPlan", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyPlan"):
                opp_val = getattr(value, "studyPlan", None)
                setattr(value, "studyPlan", self)

class ra_Department:

    pass