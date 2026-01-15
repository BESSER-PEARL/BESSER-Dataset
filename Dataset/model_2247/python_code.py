from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class StudyProgramName(Enum):
    computer_science_5_years = "computer_science_5_years"
    computer_science_2_years = "computer_science_2_years"
    informatics = "informatics"
class Semester(Enum):
    spring = "spring"
    autumn = "autumn"


############################################
# Definition of Classes
############################################

class tdt4250_CourseGroup:

    pass
class tdt4250_Student:

    def __init__(self, studentID: int, current_semester: int, tdt4250_Student: "tdt4250_StudyProgram" = None, tdt4250_Student18: "tdt4250_Specialisation" = None, tdt4250_Student6: set["tdt4250_Course"] = None):
        self.studentID = studentID
        self.current_semester = current_semester
        self.tdt4250_Student = tdt4250_Student
        self.tdt4250_Student18 = tdt4250_Student18
        self.tdt4250_Student6 = tdt4250_Student6 if tdt4250_Student6 is not None else set()
        
    @property
    def studentID(self) -> int:
        return self.__studentID

    @studentID.setter
    def studentID(self, studentID: int):
        self.__studentID = studentID

    @property
    def current_semester(self) -> int:
        return self.__current_semester

    @current_semester.setter
    def current_semester(self, current_semester: int):
        self.__current_semester = current_semester

    @property
    def tdt4250_Student(self):
        return self.__tdt4250_Student

    @tdt4250_Student.setter
    def tdt4250_Student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250_Student__tdt4250_Student", None)
        self.__tdt4250_Student = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tdt4250_StudyProgram"):
                opp_val = getattr(old_value, "tdt4250_StudyProgram", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tdt4250_StudyProgram"):
                opp_val = getattr(value, "tdt4250_StudyProgram", None)
                if opp_val is None:
                    setattr(value, "tdt4250_StudyProgram", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tdt4250_Student6(self):
        return self.__tdt4250_Student6

    @tdt4250_Student6.setter
    def tdt4250_Student6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250_Student__tdt4250_Student6", None)
        self.__tdt4250_Student6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tdt4250_Course7"):
                    opp_val = getattr(item, "tdt4250_Course7", None)
                    
                    if opp_val == self:
                        setattr(item, "tdt4250_Course7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tdt4250_Course7"):
                    opp_val = getattr(item, "tdt4250_Course7", None)
                    
                    setattr(item, "tdt4250_Course7", self)
                    

    @property
    def tdt4250_Student18(self):
        return self.__tdt4250_Student18

    @tdt4250_Student18.setter
    def tdt4250_Student18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250_Student__tdt4250_Student18", None)
        self.__tdt4250_Student18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tdt4250_Specialisation17"):
                opp_val = getattr(old_value, "tdt4250_Specialisation17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tdt4250_Specialisation17"):
                opp_val = getattr(value, "tdt4250_Specialisation17", None)
                if opp_val is None:
                    setattr(value, "tdt4250_Specialisation17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tdt4250_StudyProgram:

    def __init__(self, number_of_semesters: int, name: str, tdt4250_StudyProgram2: set["tdt4250_Specialisation"] = None, tdt4250_StudyProgram4: set["tdt4250_Course"] = None, tdt4250_StudyProgram: set["tdt4250_Student"] = None):
        self.number_of_semesters = number_of_semesters
        self.name = name
        self.tdt4250_StudyProgram2 = tdt4250_StudyProgram2 if tdt4250_StudyProgram2 is not None else set()
        self.tdt4250_StudyProgram4 = tdt4250_StudyProgram4 if tdt4250_StudyProgram4 is not None else set()
        self.tdt4250_StudyProgram = tdt4250_StudyProgram if tdt4250_StudyProgram is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def number_of_semesters(self) -> int:
        return self.__number_of_semesters

    @number_of_semesters.setter
    def number_of_semesters(self, number_of_semesters: int):
        self.__number_of_semesters = number_of_semesters

    @property
    def tdt4250_StudyProgram4(self):
        return self.__tdt4250_StudyProgram4

    @tdt4250_StudyProgram4.setter
    def tdt4250_StudyProgram4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250_StudyProgram__tdt4250_StudyProgram4", None)
        self.__tdt4250_StudyProgram4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tdt4250_Course"):
                    opp_val = getattr(item, "tdt4250_Course", None)
                    
                    if opp_val == self:
                        setattr(item, "tdt4250_Course", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tdt4250_Course"):
                    opp_val = getattr(item, "tdt4250_Course", None)
                    
                    setattr(item, "tdt4250_Course", self)
                    

    @property
    def tdt4250_StudyProgram2(self):
        return self.__tdt4250_StudyProgram2

    @tdt4250_StudyProgram2.setter
    def tdt4250_StudyProgram2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250_StudyProgram__tdt4250_StudyProgram2", None)
        self.__tdt4250_StudyProgram2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tdt4250_Specialisation"):
                    opp_val = getattr(item, "tdt4250_Specialisation", None)
                    
                    if opp_val == self:
                        setattr(item, "tdt4250_Specialisation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tdt4250_Specialisation"):
                    opp_val = getattr(item, "tdt4250_Specialisation", None)
                    
                    setattr(item, "tdt4250_Specialisation", self)
                    

    @property
    def tdt4250_StudyProgram(self):
        return self.__tdt4250_StudyProgram

    @tdt4250_StudyProgram.setter
    def tdt4250_StudyProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250_StudyProgram__tdt4250_StudyProgram", None)
        self.__tdt4250_StudyProgram = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tdt4250_Student"):
                    opp_val = getattr(item, "tdt4250_Student", None)
                    
                    if opp_val == self:
                        setattr(item, "tdt4250_Student", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tdt4250_Student"):
                    opp_val = getattr(item, "tdt4250_Student", None)
                    
                    setattr(item, "tdt4250_Student", self)
                    

class tdt4250_Course:

    def __init__(self, code: str, name: str, study_points: float, level: str, semester: str, tdt4250_Course: "tdt4250_StudyProgram" = None, tdt4250_Course9: "tdt4250_CourseGroup" = None, tdt4250_Course12: "tdt4250_CourseGroup" = None, tdt4250_Course7: "tdt4250_Student" = None):
        self.code = code
        self.name = name
        self.study_points = study_points
        self.level = level
        self.semester = semester
        self.tdt4250_Course = tdt4250_Course
        self.tdt4250_Course9 = tdt4250_Course9
        self.tdt4250_Course12 = tdt4250_Course12
        self.tdt4250_Course7 = tdt4250_Course7
        
    @property
    def study_points(self) -> float:
        return self.__study_points

    @study_points.setter
    def study_points(self, study_points: float):
        self.__study_points = study_points

    @property
    def semester(self) -> str:
        return self.__semester

    @semester.setter
    def semester(self, semester: str):
        self.__semester = semester

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level

    @property
    def tdt4250_Course(self):
        return self.__tdt4250_Course

    @tdt4250_Course.setter
    def tdt4250_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250_Course__tdt4250_Course", None)
        self.__tdt4250_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tdt4250_StudyProgram4"):
                opp_val = getattr(old_value, "tdt4250_StudyProgram4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tdt4250_StudyProgram4"):
                opp_val = getattr(value, "tdt4250_StudyProgram4", None)
                if opp_val is None:
                    setattr(value, "tdt4250_StudyProgram4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tdt4250_Course12(self):
        return self.__tdt4250_Course12

    @tdt4250_Course12.setter
    def tdt4250_Course12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250_Course__tdt4250_Course12", None)
        self.__tdt4250_Course12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tdt4250_CourseGroup11"):
                opp_val = getattr(old_value, "tdt4250_CourseGroup11", None)
                if opp_val == self:
                    setattr(old_value, "tdt4250_CourseGroup11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tdt4250_CourseGroup11"):
                opp_val = getattr(value, "tdt4250_CourseGroup11", None)
                setattr(value, "tdt4250_CourseGroup11", self)

    @property
    def tdt4250_Course9(self):
        return self.__tdt4250_Course9

    @tdt4250_Course9.setter
    def tdt4250_Course9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250_Course__tdt4250_Course9", None)
        self.__tdt4250_Course9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tdt4250_CourseGroup"):
                opp_val = getattr(old_value, "tdt4250_CourseGroup", None)
                if opp_val == self:
                    setattr(old_value, "tdt4250_CourseGroup", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tdt4250_CourseGroup"):
                opp_val = getattr(value, "tdt4250_CourseGroup", None)
                setattr(value, "tdt4250_CourseGroup", self)

    @property
    def tdt4250_Course7(self):
        return self.__tdt4250_Course7

    @tdt4250_Course7.setter
    def tdt4250_Course7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250_Course__tdt4250_Course7", None)
        self.__tdt4250_Course7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tdt4250_Student6"):
                opp_val = getattr(old_value, "tdt4250_Student6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tdt4250_Student6"):
                opp_val = getattr(value, "tdt4250_Student6", None)
                if opp_val is None:
                    setattr(value, "tdt4250_Student6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class tdt4250_Specialisation:

    def __init__(self, name: str, tdt4250_Specialisation: "tdt4250_StudyProgram" = None, tdt4250_Specialisation15: "tdt4250_CourseGroup" = None, tdt4250_Specialisation17: set["tdt4250_Student"] = None, tdt4250_Specialisation21: "tdt4250_Specialisation" = None, tdt4250_Specialisation19: "tdt4250_Specialisation" = None, tdt4250_Specialisation23: "tdt4250_CourseGroup" = None):
        self.name = name
        self.tdt4250_Specialisation = tdt4250_Specialisation
        self.tdt4250_Specialisation15 = tdt4250_Specialisation15
        self.tdt4250_Specialisation17 = tdt4250_Specialisation17 if tdt4250_Specialisation17 is not None else set()
        self.tdt4250_Specialisation21 = tdt4250_Specialisation21
        self.tdt4250_Specialisation19 = tdt4250_Specialisation19
        self.tdt4250_Specialisation23 = tdt4250_Specialisation23
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def tdt4250_Specialisation19(self):
        return self.__tdt4250_Specialisation19

    @tdt4250_Specialisation19.setter
    def tdt4250_Specialisation19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250_Specialisation__tdt4250_Specialisation19", None)
        self.__tdt4250_Specialisation19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tdt4250_Specialisation21"):
                opp_val = getattr(old_value, "tdt4250_Specialisation21", None)
                if opp_val == self:
                    setattr(old_value, "tdt4250_Specialisation21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tdt4250_Specialisation21"):
                opp_val = getattr(value, "tdt4250_Specialisation21", None)
                setattr(value, "tdt4250_Specialisation21", self)

    @property
    def tdt4250_Specialisation17(self):
        return self.__tdt4250_Specialisation17

    @tdt4250_Specialisation17.setter
    def tdt4250_Specialisation17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250_Specialisation__tdt4250_Specialisation17", None)
        self.__tdt4250_Specialisation17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "tdt4250_Student18"):
                    opp_val = getattr(item, "tdt4250_Student18", None)
                    
                    if opp_val == self:
                        setattr(item, "tdt4250_Student18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "tdt4250_Student18"):
                    opp_val = getattr(item, "tdt4250_Student18", None)
                    
                    setattr(item, "tdt4250_Student18", self)
                    

    @property
    def tdt4250_Specialisation21(self):
        return self.__tdt4250_Specialisation21

    @tdt4250_Specialisation21.setter
    def tdt4250_Specialisation21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250_Specialisation__tdt4250_Specialisation21", None)
        self.__tdt4250_Specialisation21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tdt4250_Specialisation19"):
                opp_val = getattr(old_value, "tdt4250_Specialisation19", None)
                if opp_val == self:
                    setattr(old_value, "tdt4250_Specialisation19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tdt4250_Specialisation19"):
                opp_val = getattr(value, "tdt4250_Specialisation19", None)
                setattr(value, "tdt4250_Specialisation19", self)

    @property
    def tdt4250_Specialisation23(self):
        return self.__tdt4250_Specialisation23

    @tdt4250_Specialisation23.setter
    def tdt4250_Specialisation23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250_Specialisation__tdt4250_Specialisation23", None)
        self.__tdt4250_Specialisation23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tdt4250_CourseGroup24"):
                opp_val = getattr(old_value, "tdt4250_CourseGroup24", None)
                if opp_val == self:
                    setattr(old_value, "tdt4250_CourseGroup24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tdt4250_CourseGroup24"):
                opp_val = getattr(value, "tdt4250_CourseGroup24", None)
                setattr(value, "tdt4250_CourseGroup24", self)

    @property
    def tdt4250_Specialisation15(self):
        return self.__tdt4250_Specialisation15

    @tdt4250_Specialisation15.setter
    def tdt4250_Specialisation15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250_Specialisation__tdt4250_Specialisation15", None)
        self.__tdt4250_Specialisation15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tdt4250_CourseGroup14"):
                opp_val = getattr(old_value, "tdt4250_CourseGroup14", None)
                if opp_val == self:
                    setattr(old_value, "tdt4250_CourseGroup14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tdt4250_CourseGroup14"):
                opp_val = getattr(value, "tdt4250_CourseGroup14", None)
                setattr(value, "tdt4250_CourseGroup14", self)

    @property
    def tdt4250_Specialisation(self):
        return self.__tdt4250_Specialisation

    @tdt4250_Specialisation.setter
    def tdt4250_Specialisation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_tdt4250_Specialisation__tdt4250_Specialisation", None)
        self.__tdt4250_Specialisation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tdt4250_StudyProgram2"):
                opp_val = getattr(old_value, "tdt4250_StudyProgram2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tdt4250_StudyProgram2"):
                opp_val = getattr(value, "tdt4250_StudyProgram2", None)
                if opp_val is None:
                    setattr(value, "tdt4250_StudyProgram2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
