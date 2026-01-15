from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class prosjekt_Semester:

    def __init__(self, name: str, Semester: "prosjekt_Course" = None, semester: "prosjekt_Course" = None):
        self.name = name
        self.Semester = Semester
        self.semester = semester
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Semester(self):
        return self.__Semester

    @Semester.setter
    def Semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prosjekt_Semester__Semester", None)
        self.__Semester = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course5"):
                opp_val = getattr(old_value, "course5", None)
                if opp_val == self:
                    setattr(old_value, "course5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course5"):
                opp_val = getattr(value, "course5", None)
                setattr(value, "course5", self)

    @property
    def semester(self):
        return self.__semester

    @semester.setter
    def semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prosjekt_Semester__semester", None)
        self.__semester = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Course10"):
                opp_val = getattr(old_value, "Course10", None)
                if opp_val == self:
                    setattr(old_value, "Course10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Course10"):
                opp_val = getattr(value, "Course10", None)
                setattr(value, "Course10", self)

class prosjekt_CourseCoordinator:

    def __init__(self, name: str, CourseCoordinator: "prosjekt_Institute" = None, CourseCoordinator8: "prosjekt_Course" = None, courseCoordinator: "prosjekt_Course" = None, courseCoordinator14: "prosjekt_Institute" = None):
        self.name = name
        self.CourseCoordinator = CourseCoordinator
        self.CourseCoordinator8 = CourseCoordinator8
        self.courseCoordinator = courseCoordinator
        self.courseCoordinator14 = courseCoordinator14
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def courseCoordinator(self):
        return self.__courseCoordinator

    @courseCoordinator.setter
    def courseCoordinator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prosjekt_CourseCoordinator__courseCoordinator", None)
        self.__courseCoordinator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Course12"):
                opp_val = getattr(old_value, "Course12", None)
                if opp_val == self:
                    setattr(old_value, "Course12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Course12"):
                opp_val = getattr(value, "Course12", None)
                setattr(value, "Course12", self)

    @property
    def courseCoordinator14(self):
        return self.__courseCoordinator14

    @courseCoordinator14.setter
    def courseCoordinator14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prosjekt_CourseCoordinator__courseCoordinator14", None)
        self.__courseCoordinator14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Institute15"):
                opp_val = getattr(old_value, "Institute15", None)
                if opp_val == self:
                    setattr(old_value, "Institute15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Institute15"):
                opp_val = getattr(value, "Institute15", None)
                setattr(value, "Institute15", self)

    @property
    def CourseCoordinator(self):
        return self.__CourseCoordinator

    @CourseCoordinator.setter
    def CourseCoordinator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prosjekt_CourseCoordinator__CourseCoordinator", None)
        self.__CourseCoordinator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "institute2"):
                opp_val = getattr(old_value, "institute2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "institute2"):
                opp_val = getattr(value, "institute2", None)
                if opp_val is None:
                    setattr(value, "institute2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CourseCoordinator8(self):
        return self.__CourseCoordinator8

    @CourseCoordinator8.setter
    def CourseCoordinator8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prosjekt_CourseCoordinator__CourseCoordinator8", None)
        self.__CourseCoordinator8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course7"):
                opp_val = getattr(old_value, "course7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course7"):
                opp_val = getattr(value, "course7", None)
                if opp_val is None:
                    setattr(value, "course7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class prosjekt_Course:

    def __init__(self, name: str, code: str, avgGrade: int, studyPoints: float, Course: "prosjekt_Institute" = None, course: "prosjekt_Institute" = None, course5: "prosjekt_Semester" = None, course7: set["prosjekt_CourseCoordinator"] = None, Course10: "prosjekt_Semester" = None, Course12: "prosjekt_CourseCoordinator" = None):
        self.name = name
        self.code = code
        self.avgGrade = avgGrade
        self.studyPoints = studyPoints
        self.Course = Course
        self.course = course
        self.course5 = course5
        self.course7 = course7 if course7 is not None else set()
        self.Course10 = Course10
        self.Course12 = Course12
        
    @property
    def studyPoints(self) -> float:
        return self.__studyPoints

    @studyPoints.setter
    def studyPoints(self, studyPoints: float):
        self.__studyPoints = studyPoints

    @property
    def avgGrade(self) -> int:
        return self.__avgGrade

    @avgGrade.setter
    def avgGrade(self, avgGrade: int):
        self.__avgGrade = avgGrade

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
    def course(self):
        return self.__course

    @course.setter
    def course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prosjekt_Course__course", None)
        self.__course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Institute"):
                opp_val = getattr(old_value, "Institute", None)
                if opp_val == self:
                    setattr(old_value, "Institute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Institute"):
                opp_val = getattr(value, "Institute", None)
                setattr(value, "Institute", self)

    @property
    def Course(self):
        return self.__Course

    @Course.setter
    def Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prosjekt_Course__Course", None)
        self.__Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "institute"):
                opp_val = getattr(old_value, "institute", None)
                if opp_val == self:
                    setattr(old_value, "institute", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "institute"):
                opp_val = getattr(value, "institute", None)
                setattr(value, "institute", self)

    @property
    def course7(self):
        return self.__course7

    @course7.setter
    def course7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prosjekt_Course__course7", None)
        self.__course7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CourseCoordinator8"):
                    opp_val = getattr(item, "CourseCoordinator8", None)
                    
                    if opp_val == self:
                        setattr(item, "CourseCoordinator8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CourseCoordinator8"):
                    opp_val = getattr(item, "CourseCoordinator8", None)
                    
                    setattr(item, "CourseCoordinator8", self)
                    

    @property
    def Course12(self):
        return self.__Course12

    @Course12.setter
    def Course12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prosjekt_Course__Course12", None)
        self.__Course12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courseCoordinator"):
                opp_val = getattr(old_value, "courseCoordinator", None)
                if opp_val == self:
                    setattr(old_value, "courseCoordinator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courseCoordinator"):
                opp_val = getattr(value, "courseCoordinator", None)
                setattr(value, "courseCoordinator", self)

    @property
    def course5(self):
        return self.__course5

    @course5.setter
    def course5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prosjekt_Course__course5", None)
        self.__course5 = value
        
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
    def Course10(self):
        return self.__Course10

    @Course10.setter
    def Course10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prosjekt_Course__Course10", None)
        self.__Course10 = value
        
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

class prosjekt_Institute:

    def __init__(self, name: str, shortName: str, institute: "prosjekt_Course" = None, institute2: set["prosjekt_CourseCoordinator"] = None, Institute: "prosjekt_Course" = None, Institute15: "prosjekt_CourseCoordinator" = None):
        self.name = name
        self.shortName = shortName
        self.institute = institute
        self.institute2 = institute2 if institute2 is not None else set()
        self.Institute = Institute
        self.Institute15 = Institute15
        
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
    def Institute(self):
        return self.__Institute

    @Institute.setter
    def Institute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prosjekt_Institute__Institute", None)
        self.__Institute = value
        
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
    def institute2(self):
        return self.__institute2

    @institute2.setter
    def institute2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prosjekt_Institute__institute2", None)
        self.__institute2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "CourseCoordinator"):
                    opp_val = getattr(item, "CourseCoordinator", None)
                    
                    if opp_val == self:
                        setattr(item, "CourseCoordinator", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "CourseCoordinator"):
                    opp_val = getattr(item, "CourseCoordinator", None)
                    
                    setattr(item, "CourseCoordinator", self)
                    

    @property
    def institute(self):
        return self.__institute

    @institute.setter
    def institute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prosjekt_Institute__institute", None)
        self.__institute = value
        
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
    def Institute15(self):
        return self.__Institute15

    @Institute15.setter
    def Institute15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_prosjekt_Institute__Institute15", None)
        self.__Institute15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courseCoordinator14"):
                opp_val = getattr(old_value, "courseCoordinator14", None)
                if opp_val == self:
                    setattr(old_value, "courseCoordinator14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courseCoordinator14"):
                opp_val = getattr(value, "courseCoordinator14", None)
                setattr(value, "courseCoordinator14", self)
