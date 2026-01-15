from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Grade:

    pass
class school_Grade2(Grade):

    pass
class school_Course:

    def __init__(self, name: str, school_Course7: "school_Grade" = None, school_Course: "school_School" = None):
        self.name = name
        self.school_Course7 = school_Course7
        self.school_Course = school_Course
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def school_Course(self):
        return self.__school_Course

    @school_Course.setter
    def school_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Course__school_Course", None)
        self.__school_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_School2"):
                opp_val = getattr(old_value, "school_School2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_School2"):
                opp_val = getattr(value, "school_School2", None)
                if opp_val is None:
                    setattr(value, "school_School2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def school_Course7(self):
        return self.__school_Course7

    @school_Course7.setter
    def school_Course7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Course__school_Course7", None)
        self.__school_Course7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_Grade6"):
                opp_val = getattr(old_value, "school_Grade6", None)
                if opp_val == self:
                    setattr(old_value, "school_Grade6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_Grade6"):
                opp_val = getattr(value, "school_Grade6", None)
                setattr(value, "school_Grade6", self)

class school_Grade:

    def __init__(self, grade: str, year: str, school_Grade: "school_Pupil" = None, school_Grade6: "school_Course" = None):
        self.grade = grade
        self.year = year
        self.school_Grade = school_Grade
        self.school_Grade6 = school_Grade6
        
    @property
    def grade(self) -> str:
        return self.__grade

    @grade.setter
    def grade(self, grade: str):
        self.__grade = grade

    @property
    def year(self) -> str:
        return self.__year

    @year.setter
    def year(self, year: str):
        self.__year = year

    @property
    def school_Grade(self):
        return self.__school_Grade

    @school_Grade.setter
    def school_Grade(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Grade__school_Grade", None)
        self.__school_Grade = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_Pupil4"):
                opp_val = getattr(old_value, "school_Pupil4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_Pupil4"):
                opp_val = getattr(value, "school_Pupil4", None)
                if opp_val is None:
                    setattr(value, "school_Pupil4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def school_Grade6(self):
        return self.__school_Grade6

    @school_Grade6.setter
    def school_Grade6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Grade__school_Grade6", None)
        self.__school_Grade6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_Course7"):
                opp_val = getattr(old_value, "school_Course7", None)
                if opp_val == self:
                    setattr(old_value, "school_Course7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_Course7"):
                opp_val = getattr(value, "school_Course7", None)
                setattr(value, "school_Course7", self)

class school_Pupil:

    def __init__(self, name: str, inclass: str, school_Pupil: "school_School" = None, school_Pupil4: set["school_Grade"] = None):
        self.name = name
        self.inclass = inclass
        self.school_Pupil = school_Pupil
        self.school_Pupil4 = school_Pupil4 if school_Pupil4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def inclass(self) -> str:
        return self.__inclass

    @inclass.setter
    def inclass(self, inclass: str):
        self.__inclass = inclass

    @property
    def school_Pupil4(self):
        return self.__school_Pupil4

    @school_Pupil4.setter
    def school_Pupil4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Pupil__school_Pupil4", None)
        self.__school_Pupil4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "school_Grade"):
                    opp_val = getattr(item, "school_Grade", None)
                    
                    if opp_val == self:
                        setattr(item, "school_Grade", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "school_Grade"):
                    opp_val = getattr(item, "school_Grade", None)
                    
                    setattr(item, "school_Grade", self)
                    

    @property
    def school_Pupil(self):
        return self.__school_Pupil

    @school_Pupil.setter
    def school_Pupil(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_school_Pupil__school_Pupil", None)
        self.__school_Pupil = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "school_School"):
                opp_val = getattr(old_value, "school_School", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "school_School"):
                opp_val = getattr(value, "school_School", None)
                if opp_val is None:
                    setattr(value, "school_School", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class school_School:

    pass