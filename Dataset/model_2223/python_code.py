from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class CourseStatus(Enum):
    Mandatory = "Mandatory"
    Elective = "Elective"


############################################
# Definition of Classes
############################################

class oving1APD_Slot:

    def __init__(self, name: str, Slot14: "oving1APD_Semester" = None, Slot: "oving1APD_Course" = None, slot32: "oving1APD_Semester" = None, slot: "oving1APD_Course" = None):
        self.name = name
        self.Slot14 = Slot14
        self.Slot = Slot
        self.slot32 = slot32
        self.slot = slot
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Slot(self):
        return self.__Slot

    @Slot.setter
    def Slot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Slot__Slot", None)
        self.__Slot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course11"):
                opp_val = getattr(old_value, "course11", None)
                if opp_val == self:
                    setattr(old_value, "course11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course11"):
                opp_val = getattr(value, "course11", None)
                setattr(value, "course11", self)

    @property
    def Slot14(self):
        return self.__Slot14

    @Slot14.setter
    def Slot14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Slot__Slot14", None)
        self.__Slot14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "semester"):
                opp_val = getattr(old_value, "semester", None)
                if opp_val == self:
                    setattr(old_value, "semester", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "semester"):
                opp_val = getattr(value, "semester", None)
                setattr(value, "semester", self)

    @property
    def slot(self):
        return self.__slot

    @slot.setter
    def slot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Slot__slot", None)
        self.__slot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Course30"):
                opp_val = getattr(old_value, "Course30", None)
                if opp_val == self:
                    setattr(old_value, "Course30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Course30"):
                opp_val = getattr(value, "Course30", None)
                setattr(value, "Course30", self)

    @property
    def slot32(self):
        return self.__slot32

    @slot32.setter
    def slot32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Slot__slot32", None)
        self.__slot32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Semester33"):
                opp_val = getattr(old_value, "Semester33", None)
                if opp_val == self:
                    setattr(old_value, "Semester33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Semester33"):
                opp_val = getattr(value, "Semester33", None)
                setattr(value, "Semester33", self)

class oving1APD_StudyProgram:

    def __init__(self, name: str, shortName: str, studyProgram: "oving1APD_Specialization" = None, studyProgram3: "oving1APD_Semester" = None, studyProgram5: "oving1APD_Department" = None, StudyProgram: "oving1APD_Department" = None, StudyProgram17: "oving1APD_Semester" = None, StudyProgram28: "oving1APD_Specialization" = None):
        self.name = name
        self.shortName = shortName
        self.studyProgram = studyProgram
        self.studyProgram3 = studyProgram3
        self.studyProgram5 = studyProgram5
        self.StudyProgram = StudyProgram
        self.StudyProgram17 = StudyProgram17
        self.StudyProgram28 = StudyProgram28
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def shortName(self) -> str:
        return self.__shortName

    @shortName.setter
    def shortName(self, shortName: str):
        self.__shortName = shortName

    @property
    def StudyProgram17(self):
        return self.__StudyProgram17

    @StudyProgram17.setter
    def StudyProgram17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_StudyProgram__StudyProgram17", None)
        self.__StudyProgram17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "semester16"):
                opp_val = getattr(old_value, "semester16", None)
                if opp_val == self:
                    setattr(old_value, "semester16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "semester16"):
                opp_val = getattr(value, "semester16", None)
                setattr(value, "semester16", self)

    @property
    def StudyProgram28(self):
        return self.__StudyProgram28

    @StudyProgram28.setter
    def StudyProgram28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_StudyProgram__StudyProgram28", None)
        self.__StudyProgram28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specialization27"):
                opp_val = getattr(old_value, "specialization27", None)
                if opp_val == self:
                    setattr(old_value, "specialization27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specialization27"):
                opp_val = getattr(value, "specialization27", None)
                setattr(value, "specialization27", self)

    @property
    def studyProgram(self):
        return self.__studyProgram

    @studyProgram.setter
    def studyProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_StudyProgram__studyProgram", None)
        self.__studyProgram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Specialization"):
                opp_val = getattr(old_value, "Specialization", None)
                if opp_val == self:
                    setattr(old_value, "Specialization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Specialization"):
                opp_val = getattr(value, "Specialization", None)
                setattr(value, "Specialization", self)

    @property
    def studyProgram5(self):
        return self.__studyProgram5

    @studyProgram5.setter
    def studyProgram5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_StudyProgram__studyProgram5", None)
        self.__studyProgram5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Department"):
                opp_val = getattr(old_value, "Department", None)
                if opp_val == self:
                    setattr(old_value, "Department", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Department"):
                opp_val = getattr(value, "Department", None)
                setattr(value, "Department", self)

    @property
    def studyProgram3(self):
        return self.__studyProgram3

    @studyProgram3.setter
    def studyProgram3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_StudyProgram__studyProgram3", None)
        self.__studyProgram3 = value
        
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
    def StudyProgram(self):
        return self.__StudyProgram

    @StudyProgram.setter
    def StudyProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_StudyProgram__StudyProgram", None)
        self.__StudyProgram = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department"):
                opp_val = getattr(old_value, "department", None)
                if opp_val == self:
                    setattr(old_value, "department", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department"):
                opp_val = getattr(value, "department", None)
                setattr(value, "department", self)

class oving1APD_Course:

    def __init__(self, name: str, credit: float, code: str, level: int, hasCourse: "oving1APD_Semester" = None, course: "oving1APD_Specialization" = None, Course: "oving1APD_Semester" = None, Course25: "oving1APD_Specialization" = None, course11: "oving1APD_Slot" = None, Course30: "oving1APD_Slot" = None):
        self.name = name
        self.credit = credit
        self.code = code
        self.level = level
        self.hasCourse = hasCourse
        self.course = course
        self.Course = Course
        self.Course25 = Course25
        self.course11 = course11
        self.Course30 = Course30
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def level(self) -> int:
        return self.__level

    @level.setter
    def level(self, level: int):
        self.__level = level

    @property
    def credit(self) -> float:
        return self.__credit

    @credit.setter
    def credit(self, credit: float):
        self.__credit = credit

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def hasCourse(self):
        return self.__hasCourse

    @hasCourse.setter
    def hasCourse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Course__hasCourse", None)
        self.__hasCourse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Semester7"):
                opp_val = getattr(old_value, "Semester7", None)
                if opp_val == self:
                    setattr(old_value, "Semester7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Semester7"):
                opp_val = getattr(value, "Semester7", None)
                setattr(value, "Semester7", self)

    @property
    def Course30(self):
        return self.__Course30

    @Course30.setter
    def Course30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Course__Course30", None)
        self.__Course30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "slot"):
                opp_val = getattr(old_value, "slot", None)
                if opp_val == self:
                    setattr(old_value, "slot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "slot"):
                opp_val = getattr(value, "slot", None)
                setattr(value, "slot", self)

    @property
    def Course(self):
        return self.__Course

    @Course.setter
    def Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Course__Course", None)
        self.__Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courseInSemester"):
                opp_val = getattr(old_value, "courseInSemester", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courseInSemester"):
                opp_val = getattr(value, "courseInSemester", None)
                if opp_val is None:
                    setattr(value, "courseInSemester", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Course25(self):
        return self.__Course25

    @Course25.setter
    def Course25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Course__Course25", None)
        self.__Course25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specialization24"):
                opp_val = getattr(old_value, "specialization24", None)
                if opp_val == self:
                    setattr(old_value, "specialization24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specialization24"):
                opp_val = getattr(value, "specialization24", None)
                setattr(value, "specialization24", self)

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Course__course", None)
        self.__course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Specialization9"):
                opp_val = getattr(old_value, "Specialization9", None)
                if opp_val == self:
                    setattr(old_value, "Specialization9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Specialization9"):
                opp_val = getattr(value, "Specialization9", None)
                setattr(value, "Specialization9", self)

    @property
    def course11(self):
        return self.__course11

    @course11.setter
    def course11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Course__course11", None)
        self.__course11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Slot"):
                opp_val = getattr(old_value, "Slot", None)
                if opp_val == self:
                    setattr(old_value, "Slot", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Slot"):
                opp_val = getattr(value, "Slot", None)
                setattr(value, "Slot", self)

class oving1APD_Semester:

    def __init__(self, number: int, Semester: "oving1APD_StudyProgram" = None, Semester7: "oving1APD_Course" = None, courseInSemester: set["oving1APD_Course"] = None, semester: "oving1APD_Slot" = None, semester16: "oving1APD_StudyProgram" = None, semester19: "oving1APD_Specialization" = None, Semester22: "oving1APD_Specialization" = None, Semester33: "oving1APD_Slot" = None):
        self.number = number
        self.Semester = Semester
        self.Semester7 = Semester7
        self.courseInSemester = courseInSemester if courseInSemester is not None else set()
        self.semester = semester
        self.semester16 = semester16
        self.semester19 = semester19
        self.Semester22 = Semester22
        self.Semester33 = Semester33
        
    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def semester16(self):
        return self.__semester16

    @semester16.setter
    def semester16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Semester__semester16", None)
        self.__semester16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StudyProgram17"):
                opp_val = getattr(old_value, "StudyProgram17", None)
                if opp_val == self:
                    setattr(old_value, "StudyProgram17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StudyProgram17"):
                opp_val = getattr(value, "StudyProgram17", None)
                setattr(value, "StudyProgram17", self)

    @property
    def semester19(self):
        return self.__semester19

    @semester19.setter
    def semester19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Semester__semester19", None)
        self.__semester19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Specialization20"):
                opp_val = getattr(old_value, "Specialization20", None)
                if opp_val == self:
                    setattr(old_value, "Specialization20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Specialization20"):
                opp_val = getattr(value, "Specialization20", None)
                setattr(value, "Specialization20", self)

    @property
    def Semester33(self):
        return self.__Semester33

    @Semester33.setter
    def Semester33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Semester__Semester33", None)
        self.__Semester33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "slot32"):
                opp_val = getattr(old_value, "slot32", None)
                if opp_val == self:
                    setattr(old_value, "slot32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "slot32"):
                opp_val = getattr(value, "slot32", None)
                setattr(value, "slot32", self)

    @property
    def Semester22(self):
        return self.__Semester22

    @Semester22.setter
    def Semester22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Semester__Semester22", None)
        self.__Semester22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specialization"):
                opp_val = getattr(old_value, "specialization", None)
                if opp_val == self:
                    setattr(old_value, "specialization", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specialization"):
                opp_val = getattr(value, "specialization", None)
                setattr(value, "specialization", self)

    @property
    def Semester7(self):
        return self.__Semester7

    @Semester7.setter
    def Semester7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Semester__Semester7", None)
        self.__Semester7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hasCourse"):
                opp_val = getattr(old_value, "hasCourse", None)
                if opp_val == self:
                    setattr(old_value, "hasCourse", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hasCourse"):
                opp_val = getattr(value, "hasCourse", None)
                setattr(value, "hasCourse", self)

    @property
    def semester(self):
        return self.__semester

    @semester.setter
    def semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Semester__semester", None)
        self.__semester = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Slot14"):
                opp_val = getattr(old_value, "Slot14", None)
                if opp_val == self:
                    setattr(old_value, "Slot14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Slot14"):
                opp_val = getattr(value, "Slot14", None)
                setattr(value, "Slot14", self)

    @property
    def courseInSemester(self):
        return self.__courseInSemester

    @courseInSemester.setter
    def courseInSemester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Semester__courseInSemester", None)
        self.__courseInSemester = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Course"):
                    opp_val = getattr(item, "Course", None)
                    
                    if opp_val == self:
                        setattr(item, "Course", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Course"):
                    opp_val = getattr(item, "Course", None)
                    
                    setattr(item, "Course", self)
                    

    @property
    def Semester(self):
        return self.__Semester

    @Semester.setter
    def Semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Semester__Semester", None)
        self.__Semester = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyProgram3"):
                opp_val = getattr(old_value, "studyProgram3", None)
                if opp_val == self:
                    setattr(old_value, "studyProgram3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyProgram3"):
                opp_val = getattr(value, "studyProgram3", None)
                setattr(value, "studyProgram3", self)

class oving1APD_Specialization:

    def __init__(self, name: str, Specialization: "oving1APD_StudyProgram" = None, Specialization9: "oving1APD_Course" = None, Specialization20: "oving1APD_Semester" = None, specialization: "oving1APD_Semester" = None, specialization24: "oving1APD_Course" = None, specialization27: "oving1APD_StudyProgram" = None):
        self.name = name
        self.Specialization = Specialization
        self.Specialization9 = Specialization9
        self.Specialization20 = Specialization20
        self.specialization = specialization
        self.specialization24 = specialization24
        self.specialization27 = specialization27
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def specialization(self):
        return self.__specialization

    @specialization.setter
    def specialization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Specialization__specialization", None)
        self.__specialization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Semester22"):
                opp_val = getattr(old_value, "Semester22", None)
                if opp_val == self:
                    setattr(old_value, "Semester22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Semester22"):
                opp_val = getattr(value, "Semester22", None)
                setattr(value, "Semester22", self)

    @property
    def Specialization(self):
        return self.__Specialization

    @Specialization.setter
    def Specialization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Specialization__Specialization", None)
        self.__Specialization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyProgram"):
                opp_val = getattr(old_value, "studyProgram", None)
                if opp_val == self:
                    setattr(old_value, "studyProgram", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyProgram"):
                opp_val = getattr(value, "studyProgram", None)
                setattr(value, "studyProgram", self)

    @property
    def specialization27(self):
        return self.__specialization27

    @specialization27.setter
    def specialization27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Specialization__specialization27", None)
        self.__specialization27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StudyProgram28"):
                opp_val = getattr(old_value, "StudyProgram28", None)
                if opp_val == self:
                    setattr(old_value, "StudyProgram28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StudyProgram28"):
                opp_val = getattr(value, "StudyProgram28", None)
                setattr(value, "StudyProgram28", self)

    @property
    def Specialization20(self):
        return self.__Specialization20

    @Specialization20.setter
    def Specialization20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Specialization__Specialization20", None)
        self.__Specialization20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "semester19"):
                opp_val = getattr(old_value, "semester19", None)
                if opp_val == self:
                    setattr(old_value, "semester19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "semester19"):
                opp_val = getattr(value, "semester19", None)
                setattr(value, "semester19", self)

    @property
    def specialization24(self):
        return self.__specialization24

    @specialization24.setter
    def specialization24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Specialization__specialization24", None)
        self.__specialization24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Course25"):
                opp_val = getattr(old_value, "Course25", None)
                if opp_val == self:
                    setattr(old_value, "Course25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Course25"):
                opp_val = getattr(value, "Course25", None)
                setattr(value, "Course25", self)

    @property
    def Specialization9(self):
        return self.__Specialization9

    @Specialization9.setter
    def Specialization9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Specialization__Specialization9", None)
        self.__Specialization9 = value
        
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

class oving1APD_Department:

    def __init__(self, name: str, shortName: str, Department: "oving1APD_StudyProgram" = None, department: "oving1APD_StudyProgram" = None):
        self.name = name
        self.shortName = shortName
        self.Department = Department
        self.department = department
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def shortName(self) -> str:
        return self.__shortName

    @shortName.setter
    def shortName(self, shortName: str):
        self.__shortName = shortName

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Department__department", None)
        self.__department = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StudyProgram"):
                opp_val = getattr(old_value, "StudyProgram", None)
                if opp_val == self:
                    setattr(old_value, "StudyProgram", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StudyProgram"):
                opp_val = getattr(value, "StudyProgram", None)
                setattr(value, "StudyProgram", self)

    @property
    def Department(self):
        return self.__Department

    @Department.setter
    def Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Department__Department", None)
        self.__Department = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "studyProgram5"):
                opp_val = getattr(old_value, "studyProgram5", None)
                if opp_val == self:
                    setattr(old_value, "studyProgram5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyProgram5"):
                opp_val = getattr(value, "studyProgram5", None)
                setattr(value, "studyProgram5", self)
