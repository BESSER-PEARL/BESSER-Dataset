from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class oving1APD_Slot:

    def __init__(self, name: str, Slot: "oving1APD_Course" = None, slot33: "oving1APD_Semester" = None, Slot15: "oving1APD_Semester" = None, slot: "oving1APD_Course" = None):
        self.name = name
        self.Slot = Slot
        self.slot33 = slot33
        self.Slot15 = Slot15
        self.slot = slot
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "Course31"):
                opp_val = getattr(old_value, "Course31", None)
                if opp_val == self:
                    setattr(old_value, "Course31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Course31"):
                opp_val = getattr(value, "Course31", None)
                setattr(value, "Course31", self)

    @property
    def slot33(self):
        return self.__slot33

    @slot33.setter
    def slot33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Slot__slot33", None)
        self.__slot33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Semester34"):
                opp_val = getattr(old_value, "Semester34", None)
                if opp_val == self:
                    setattr(old_value, "Semester34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Semester34"):
                opp_val = getattr(value, "Semester34", None)
                setattr(value, "Semester34", self)

    @property
    def Slot15(self):
        return self.__Slot15

    @Slot15.setter
    def Slot15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Slot__Slot15", None)
        self.__Slot15 = value
        
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
    def Slot(self):
        return self.__Slot

    @Slot.setter
    def Slot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Slot__Slot", None)
        self.__Slot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course12"):
                opp_val = getattr(old_value, "course12", None)
                if opp_val == self:
                    setattr(old_value, "course12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course12"):
                opp_val = getattr(value, "course12", None)
                setattr(value, "course12", self)

class oving1APD_Semester:

    def __init__(self, number: int, Semester: "oving1APD_StudyProgram" = None, Semester8: "oving1APD_Course" = None, Semester34: "oving1APD_Slot" = None, courseInSemester: set["oving1APD_Course"] = None, semester: "oving1APD_Slot" = None, semester17: "oving1APD_StudyProgram" = None, semester20: "oving1APD_Specialization" = None, Semester23: "oving1APD_Specialization" = None):
        self.number = number
        self.Semester = Semester
        self.Semester8 = Semester8
        self.Semester34 = Semester34
        self.courseInSemester = courseInSemester if courseInSemester is not None else set()
        self.semester = semester
        self.semester17 = semester17
        self.semester20 = semester20
        self.Semester23 = Semester23
        
    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

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
            if hasattr(old_value, "studyProgram4"):
                opp_val = getattr(old_value, "studyProgram4", None)
                if opp_val == self:
                    setattr(old_value, "studyProgram4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyProgram4"):
                opp_val = getattr(value, "studyProgram4", None)
                setattr(value, "studyProgram4", self)

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
            if hasattr(old_value, "Slot15"):
                opp_val = getattr(old_value, "Slot15", None)
                if opp_val == self:
                    setattr(old_value, "Slot15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Slot15"):
                opp_val = getattr(value, "Slot15", None)
                setattr(value, "Slot15", self)

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
    def Semester34(self):
        return self.__Semester34

    @Semester34.setter
    def Semester34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Semester__Semester34", None)
        self.__Semester34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "slot33"):
                opp_val = getattr(old_value, "slot33", None)
                if opp_val == self:
                    setattr(old_value, "slot33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "slot33"):
                opp_val = getattr(value, "slot33", None)
                setattr(value, "slot33", self)

    @property
    def Semester8(self):
        return self.__Semester8

    @Semester8.setter
    def Semester8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Semester__Semester8", None)
        self.__Semester8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hasCourse"):
                opp_val = getattr(old_value, "hasCourse", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hasCourse"):
                opp_val = getattr(value, "hasCourse", None)
                if opp_val is None:
                    setattr(value, "hasCourse", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Semester23(self):
        return self.__Semester23

    @Semester23.setter
    def Semester23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Semester__Semester23", None)
        self.__Semester23 = value
        
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
    def semester17(self):
        return self.__semester17

    @semester17.setter
    def semester17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Semester__semester17", None)
        self.__semester17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StudyProgram18"):
                opp_val = getattr(old_value, "StudyProgram18", None)
                if opp_val == self:
                    setattr(old_value, "StudyProgram18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StudyProgram18"):
                opp_val = getattr(value, "StudyProgram18", None)
                setattr(value, "StudyProgram18", self)

    @property
    def semester20(self):
        return self.__semester20

    @semester20.setter
    def semester20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Semester__semester20", None)
        self.__semester20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Specialization21"):
                opp_val = getattr(old_value, "Specialization21", None)
                if opp_val == self:
                    setattr(old_value, "Specialization21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Specialization21"):
                opp_val = getattr(value, "Specialization21", None)
                setattr(value, "Specialization21", self)

class oving1APD_Specialization:

    def __init__(self, name: str, Specialization: "oving1APD_StudyProgram" = None, Specialization10: "oving1APD_Course" = None, Specialization21: "oving1APD_Semester" = None, specialization: "oving1APD_Semester" = None, specialization25: set["oving1APD_Course"] = None, specialization28: "oving1APD_StudyProgram" = None):
        self.name = name
        self.Specialization = Specialization
        self.Specialization10 = Specialization10
        self.Specialization21 = Specialization21
        self.specialization = specialization
        self.specialization25 = specialization25 if specialization25 is not None else set()
        self.specialization28 = specialization28
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Specialization10(self):
        return self.__Specialization10

    @Specialization10.setter
    def Specialization10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Specialization__Specialization10", None)
        self.__Specialization10 = value
        
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
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyProgram"):
                opp_val = getattr(value, "studyProgram", None)
                if opp_val is None:
                    setattr(value, "studyProgram", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "Semester23"):
                opp_val = getattr(old_value, "Semester23", None)
                if opp_val == self:
                    setattr(old_value, "Semester23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Semester23"):
                opp_val = getattr(value, "Semester23", None)
                setattr(value, "Semester23", self)

    @property
    def Specialization21(self):
        return self.__Specialization21

    @Specialization21.setter
    def Specialization21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Specialization__Specialization21", None)
        self.__Specialization21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "semester20"):
                opp_val = getattr(old_value, "semester20", None)
                if opp_val == self:
                    setattr(old_value, "semester20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "semester20"):
                opp_val = getattr(value, "semester20", None)
                setattr(value, "semester20", self)

    @property
    def specialization28(self):
        return self.__specialization28

    @specialization28.setter
    def specialization28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Specialization__specialization28", None)
        self.__specialization28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StudyProgram29"):
                opp_val = getattr(old_value, "StudyProgram29", None)
                if opp_val == self:
                    setattr(old_value, "StudyProgram29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StudyProgram29"):
                opp_val = getattr(value, "StudyProgram29", None)
                setattr(value, "StudyProgram29", self)

    @property
    def specialization25(self):
        return self.__specialization25

    @specialization25.setter
    def specialization25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Specialization__specialization25", None)
        self.__specialization25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Course26"):
                    opp_val = getattr(item, "Course26", None)
                    
                    if opp_val == self:
                        setattr(item, "Course26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Course26"):
                    opp_val = getattr(item, "Course26", None)
                    
                    setattr(item, "Course26", self)
                    

class oving1APD_Course:

    def __init__(self, name: str, credit: float, code: str, level: int, oving1APD_Course: "oving1APD_Department" = None, hasCourse: set["oving1APD_Semester"] = None, course: "oving1APD_Specialization" = None, course12: "oving1APD_Slot" = None, Course: "oving1APD_Semester" = None, Course26: "oving1APD_Specialization" = None, Course31: "oving1APD_Slot" = None):
        self.name = name
        self.credit = credit
        self.code = code
        self.level = level
        self.oving1APD_Course = oving1APD_Course
        self.hasCourse = hasCourse if hasCourse is not None else set()
        self.course = course
        self.course12 = course12
        self.Course = Course
        self.Course26 = Course26
        self.Course31 = Course31
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def credit(self) -> float:
        return self.__credit

    @credit.setter
    def credit(self, credit: float):
        self.__credit = credit

    @property
    def level(self) -> int:
        return self.__level

    @level.setter
    def level(self, level: int):
        self.__level = level

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
        self.__hasCourse = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Semester8"):
                    opp_val = getattr(item, "Semester8", None)
                    
                    if opp_val == self:
                        setattr(item, "Semester8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Semester8"):
                    opp_val = getattr(item, "Semester8", None)
                    
                    setattr(item, "Semester8", self)
                    

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
    def Course31(self):
        return self.__Course31

    @Course31.setter
    def Course31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Course__Course31", None)
        self.__Course31 = value
        
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
    def Course26(self):
        return self.__Course26

    @Course26.setter
    def Course26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Course__Course26", None)
        self.__Course26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specialization25"):
                opp_val = getattr(old_value, "specialization25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specialization25"):
                opp_val = getattr(value, "specialization25", None)
                if opp_val is None:
                    setattr(value, "specialization25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "Specialization10"):
                opp_val = getattr(old_value, "Specialization10", None)
                if opp_val == self:
                    setattr(old_value, "Specialization10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Specialization10"):
                opp_val = getattr(value, "Specialization10", None)
                setattr(value, "Specialization10", self)

    @property
    def course12(self):
        return self.__course12

    @course12.setter
    def course12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Course__course12", None)
        self.__course12 = value
        
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

    @property
    def oving1APD_Course(self):
        return self.__oving1APD_Course

    @oving1APD_Course.setter
    def oving1APD_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Course__oving1APD_Course", None)
        self.__oving1APD_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "oving1APD_Department"):
                opp_val = getattr(old_value, "oving1APD_Department", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "oving1APD_Department"):
                opp_val = getattr(value, "oving1APD_Department", None)
                if opp_val is None:
                    setattr(value, "oving1APD_Department", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class oving1APD_StudyProgram:

    def __init__(self, name: str, shortName: str, StudyProgram: "oving1APD_Department" = None, studyProgram: set["oving1APD_Specialization"] = None, studyProgram4: "oving1APD_Semester" = None, studyProgram6: "oving1APD_Department" = None, StudyProgram18: "oving1APD_Semester" = None, StudyProgram29: "oving1APD_Specialization" = None):
        self.name = name
        self.shortName = shortName
        self.StudyProgram = StudyProgram
        self.studyProgram = studyProgram if studyProgram is not None else set()
        self.studyProgram4 = studyProgram4
        self.studyProgram6 = studyProgram6
        self.StudyProgram18 = StudyProgram18
        self.StudyProgram29 = StudyProgram29
        
    @property
    def shortName(self) -> str:
        return self.__shortName

    @shortName.setter
    def shortName(self, shortName: str):
        self.__shortName = shortName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def studyProgram(self):
        return self.__studyProgram

    @studyProgram.setter
    def studyProgram(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_StudyProgram__studyProgram", None)
        self.__studyProgram = value if value is not None else set()
        
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
    def studyProgram6(self):
        return self.__studyProgram6

    @studyProgram6.setter
    def studyProgram6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_StudyProgram__studyProgram6", None)
        self.__studyProgram6 = value
        
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
    def StudyProgram29(self):
        return self.__StudyProgram29

    @StudyProgram29.setter
    def StudyProgram29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_StudyProgram__StudyProgram29", None)
        self.__StudyProgram29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "specialization28"):
                opp_val = getattr(old_value, "specialization28", None)
                if opp_val == self:
                    setattr(old_value, "specialization28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "specialization28"):
                opp_val = getattr(value, "specialization28", None)
                setattr(value, "specialization28", self)

    @property
    def StudyProgram18(self):
        return self.__StudyProgram18

    @StudyProgram18.setter
    def StudyProgram18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_StudyProgram__StudyProgram18", None)
        self.__StudyProgram18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "semester17"):
                opp_val = getattr(old_value, "semester17", None)
                if opp_val == self:
                    setattr(old_value, "semester17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "semester17"):
                opp_val = getattr(value, "semester17", None)
                setattr(value, "semester17", self)

    @property
    def studyProgram4(self):
        return self.__studyProgram4

    @studyProgram4.setter
    def studyProgram4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_StudyProgram__studyProgram4", None)
        self.__studyProgram4 = value
        
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
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department"):
                opp_val = getattr(value, "department", None)
                if opp_val is None:
                    setattr(value, "department", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class oving1APD_Department:

    def __init__(self, name: str, shortName: str, department: set["oving1APD_StudyProgram"] = None, oving1APD_Department: set["oving1APD_Course"] = None, Department: "oving1APD_StudyProgram" = None):
        self.name = name
        self.shortName = shortName
        self.department = department if department is not None else set()
        self.oving1APD_Department = oving1APD_Department if oving1APD_Department is not None else set()
        self.Department = Department
        
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
        self.__department = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StudyProgram"):
                    opp_val = getattr(item, "StudyProgram", None)
                    
                    if opp_val == self:
                        setattr(item, "StudyProgram", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StudyProgram"):
                    opp_val = getattr(item, "StudyProgram", None)
                    
                    setattr(item, "StudyProgram", self)
                    

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
            if hasattr(old_value, "studyProgram6"):
                opp_val = getattr(old_value, "studyProgram6", None)
                if opp_val == self:
                    setattr(old_value, "studyProgram6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "studyProgram6"):
                opp_val = getattr(value, "studyProgram6", None)
                setattr(value, "studyProgram6", self)

    @property
    def oving1APD_Department(self):
        return self.__oving1APD_Department

    @oving1APD_Department.setter
    def oving1APD_Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_oving1APD_Department__oving1APD_Department", None)
        self.__oving1APD_Department = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "oving1APD_Course"):
                    opp_val = getattr(item, "oving1APD_Course", None)
                    
                    if opp_val == self:
                        setattr(item, "oving1APD_Course", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "oving1APD_Course"):
                    opp_val = getattr(item, "oving1APD_Course", None)
                    
                    setattr(item, "oving1APD_Course", self)
                    
