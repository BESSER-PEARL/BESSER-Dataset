from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class StudyProgramme_Department:

    def __init__(self, name: str, code: str, StudyProgramme_Department: set["StudyProgramme_Programme"] = None, StudyProgramme_Department22: set["StudyProgramme_Course"] = None):
        self.name = name
        self.code = code
        self.StudyProgramme_Department = StudyProgramme_Department if StudyProgramme_Department is not None else set()
        self.StudyProgramme_Department22 = StudyProgramme_Department22 if StudyProgramme_Department22 is not None else set()
        
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
    def StudyProgramme_Department(self):
        return self.__StudyProgramme_Department

    @StudyProgramme_Department.setter
    def StudyProgramme_Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StudyProgramme_Department__StudyProgramme_Department", None)
        self.__StudyProgramme_Department = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StudyProgramme_Programme20"):
                    opp_val = getattr(item, "StudyProgramme_Programme20", None)
                    
                    if opp_val == self:
                        setattr(item, "StudyProgramme_Programme20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StudyProgramme_Programme20"):
                    opp_val = getattr(item, "StudyProgramme_Programme20", None)
                    
                    setattr(item, "StudyProgramme_Programme20", self)
                    

    @property
    def StudyProgramme_Department22(self):
        return self.__StudyProgramme_Department22

    @StudyProgramme_Department22.setter
    def StudyProgramme_Department22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StudyProgramme_Department__StudyProgramme_Department22", None)
        self.__StudyProgramme_Department22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StudyProgramme_Course23"):
                    opp_val = getattr(item, "StudyProgramme_Course23", None)
                    
                    if opp_val == self:
                        setattr(item, "StudyProgramme_Course23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StudyProgramme_Course23"):
                    opp_val = getattr(item, "StudyProgramme_Course23", None)
                    
                    setattr(item, "StudyProgramme_Course23", self)
                    

class StudyProgramme_CourseGroup:

    def __init__(self, status: str, StudyProgramme_CourseGroup: "StudyProgramme_Semester" = None, StudyProgramme_CourseGroup17: set["StudyProgramme_Course"] = None):
        self.status = status
        self.StudyProgramme_CourseGroup = StudyProgramme_CourseGroup
        self.StudyProgramme_CourseGroup17 = StudyProgramme_CourseGroup17 if StudyProgramme_CourseGroup17 is not None else set()
        
    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def StudyProgramme_CourseGroup(self):
        return self.__StudyProgramme_CourseGroup

    @StudyProgramme_CourseGroup.setter
    def StudyProgramme_CourseGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StudyProgramme_CourseGroup__StudyProgramme_CourseGroup", None)
        self.__StudyProgramme_CourseGroup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StudyProgramme_Semester6"):
                opp_val = getattr(old_value, "StudyProgramme_Semester6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StudyProgramme_Semester6"):
                opp_val = getattr(value, "StudyProgramme_Semester6", None)
                if opp_val is None:
                    setattr(value, "StudyProgramme_Semester6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def StudyProgramme_CourseGroup17(self):
        return self.__StudyProgramme_CourseGroup17

    @StudyProgramme_CourseGroup17.setter
    def StudyProgramme_CourseGroup17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StudyProgramme_CourseGroup__StudyProgramme_CourseGroup17", None)
        self.__StudyProgramme_CourseGroup17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StudyProgramme_Course18"):
                    opp_val = getattr(item, "StudyProgramme_Course18", None)
                    
                    if opp_val == self:
                        setattr(item, "StudyProgramme_Course18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StudyProgramme_Course18"):
                    opp_val = getattr(item, "StudyProgramme_Course18", None)
                    
                    setattr(item, "StudyProgramme_Course18", self)
                    

class StudyProgramme_Course:

    def __init__(self, name: str, code: str, credits: float, level: str, StudyProgramme_Course: "StudyProgramme_Semester" = None, StudyProgramme_Course9: "StudyProgramme_Specialization" = None, StudyProgramme_Course18: "StudyProgramme_CourseGroup" = None, StudyProgramme_Course23: "StudyProgramme_Department" = None):
        self.name = name
        self.code = code
        self.credits = credits
        self.level = level
        self.StudyProgramme_Course = StudyProgramme_Course
        self.StudyProgramme_Course9 = StudyProgramme_Course9
        self.StudyProgramme_Course18 = StudyProgramme_Course18
        self.StudyProgramme_Course23 = StudyProgramme_Course23
        
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
    def level(self) -> str:
        return self.__level

    @level.setter
    def level(self, level: str):
        self.__level = level

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def StudyProgramme_Course9(self):
        return self.__StudyProgramme_Course9

    @StudyProgramme_Course9.setter
    def StudyProgramme_Course9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StudyProgramme_Course__StudyProgramme_Course9", None)
        self.__StudyProgramme_Course9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StudyProgramme_Specialization8"):
                opp_val = getattr(old_value, "StudyProgramme_Specialization8", None)
                if opp_val == self:
                    setattr(old_value, "StudyProgramme_Specialization8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StudyProgramme_Specialization8"):
                opp_val = getattr(value, "StudyProgramme_Specialization8", None)
                setattr(value, "StudyProgramme_Specialization8", self)

    @property
    def StudyProgramme_Course(self):
        return self.__StudyProgramme_Course

    @StudyProgramme_Course.setter
    def StudyProgramme_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StudyProgramme_Course__StudyProgramme_Course", None)
        self.__StudyProgramme_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StudyProgramme_Semester4"):
                opp_val = getattr(old_value, "StudyProgramme_Semester4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StudyProgramme_Semester4"):
                opp_val = getattr(value, "StudyProgramme_Semester4", None)
                if opp_val is None:
                    setattr(value, "StudyProgramme_Semester4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def StudyProgramme_Course18(self):
        return self.__StudyProgramme_Course18

    @StudyProgramme_Course18.setter
    def StudyProgramme_Course18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StudyProgramme_Course__StudyProgramme_Course18", None)
        self.__StudyProgramme_Course18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StudyProgramme_CourseGroup17"):
                opp_val = getattr(old_value, "StudyProgramme_CourseGroup17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StudyProgramme_CourseGroup17"):
                opp_val = getattr(value, "StudyProgramme_CourseGroup17", None)
                if opp_val is None:
                    setattr(value, "StudyProgramme_CourseGroup17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def StudyProgramme_Course23(self):
        return self.__StudyProgramme_Course23

    @StudyProgramme_Course23.setter
    def StudyProgramme_Course23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StudyProgramme_Course__StudyProgramme_Course23", None)
        self.__StudyProgramme_Course23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StudyProgramme_Department22"):
                opp_val = getattr(old_value, "StudyProgramme_Department22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StudyProgramme_Department22"):
                opp_val = getattr(value, "StudyProgramme_Department22", None)
                if opp_val is None:
                    setattr(value, "StudyProgramme_Department22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class StudyProgramme_Specialization:

    def __init__(self, name: str, StudyProgramme_Specialization: "StudyProgramme_Programme" = None, StudyProgramme_Specialization8: "StudyProgramme_Course" = None, StudyProgramme_Specialization11: set["StudyProgramme_Semester"] = None, StudyProgramme_Specialization15: "StudyProgramme_Specialization" = None, StudyProgramme_Specialization13: set["StudyProgramme_Specialization"] = None):
        self.name = name
        self.StudyProgramme_Specialization = StudyProgramme_Specialization
        self.StudyProgramme_Specialization8 = StudyProgramme_Specialization8
        self.StudyProgramme_Specialization11 = StudyProgramme_Specialization11 if StudyProgramme_Specialization11 is not None else set()
        self.StudyProgramme_Specialization15 = StudyProgramme_Specialization15
        self.StudyProgramme_Specialization13 = StudyProgramme_Specialization13 if StudyProgramme_Specialization13 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def StudyProgramme_Specialization15(self):
        return self.__StudyProgramme_Specialization15

    @StudyProgramme_Specialization15.setter
    def StudyProgramme_Specialization15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StudyProgramme_Specialization__StudyProgramme_Specialization15", None)
        self.__StudyProgramme_Specialization15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StudyProgramme_Specialization13"):
                opp_val = getattr(old_value, "StudyProgramme_Specialization13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StudyProgramme_Specialization13"):
                opp_val = getattr(value, "StudyProgramme_Specialization13", None)
                if opp_val is None:
                    setattr(value, "StudyProgramme_Specialization13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def StudyProgramme_Specialization(self):
        return self.__StudyProgramme_Specialization

    @StudyProgramme_Specialization.setter
    def StudyProgramme_Specialization(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StudyProgramme_Specialization__StudyProgramme_Specialization", None)
        self.__StudyProgramme_Specialization = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StudyProgramme_Programme2"):
                opp_val = getattr(old_value, "StudyProgramme_Programme2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StudyProgramme_Programme2"):
                opp_val = getattr(value, "StudyProgramme_Programme2", None)
                if opp_val is None:
                    setattr(value, "StudyProgramme_Programme2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def StudyProgramme_Specialization11(self):
        return self.__StudyProgramme_Specialization11

    @StudyProgramme_Specialization11.setter
    def StudyProgramme_Specialization11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StudyProgramme_Specialization__StudyProgramme_Specialization11", None)
        self.__StudyProgramme_Specialization11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StudyProgramme_Semester12"):
                    opp_val = getattr(item, "StudyProgramme_Semester12", None)
                    
                    if opp_val == self:
                        setattr(item, "StudyProgramme_Semester12", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StudyProgramme_Semester12"):
                    opp_val = getattr(item, "StudyProgramme_Semester12", None)
                    
                    setattr(item, "StudyProgramme_Semester12", self)
                    

    @property
    def StudyProgramme_Specialization13(self):
        return self.__StudyProgramme_Specialization13

    @StudyProgramme_Specialization13.setter
    def StudyProgramme_Specialization13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StudyProgramme_Specialization__StudyProgramme_Specialization13", None)
        self.__StudyProgramme_Specialization13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StudyProgramme_Specialization15"):
                    opp_val = getattr(item, "StudyProgramme_Specialization15", None)
                    
                    if opp_val == self:
                        setattr(item, "StudyProgramme_Specialization15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StudyProgramme_Specialization15"):
                    opp_val = getattr(item, "StudyProgramme_Specialization15", None)
                    
                    setattr(item, "StudyProgramme_Specialization15", self)
                    

    @property
    def StudyProgramme_Specialization8(self):
        return self.__StudyProgramme_Specialization8

    @StudyProgramme_Specialization8.setter
    def StudyProgramme_Specialization8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StudyProgramme_Specialization__StudyProgramme_Specialization8", None)
        self.__StudyProgramme_Specialization8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StudyProgramme_Course9"):
                opp_val = getattr(old_value, "StudyProgramme_Course9", None)
                if opp_val == self:
                    setattr(old_value, "StudyProgramme_Course9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StudyProgramme_Course9"):
                opp_val = getattr(value, "StudyProgramme_Course9", None)
                setattr(value, "StudyProgramme_Course9", self)

class StudyProgramme_Semester:

    def __init__(self, totalCredits: float, season: str, creditConstraint: str, number: int, StudyProgramme_Semester: "StudyProgramme_Programme" = None, StudyProgramme_Semester4: set["StudyProgramme_Course"] = None, StudyProgramme_Semester6: set["StudyProgramme_CourseGroup"] = None, StudyProgramme_Semester12: "StudyProgramme_Specialization" = None):
        self.totalCredits = totalCredits
        self.season = season
        self.creditConstraint = creditConstraint
        self.number = number
        self.StudyProgramme_Semester = StudyProgramme_Semester
        self.StudyProgramme_Semester4 = StudyProgramme_Semester4 if StudyProgramme_Semester4 is not None else set()
        self.StudyProgramme_Semester6 = StudyProgramme_Semester6 if StudyProgramme_Semester6 is not None else set()
        self.StudyProgramme_Semester12 = StudyProgramme_Semester12
        
    @property
    def season(self) -> str:
        return self.__season

    @season.setter
    def season(self, season: str):
        self.__season = season

    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number

    @property
    def creditConstraint(self) -> str:
        return self.__creditConstraint

    @creditConstraint.setter
    def creditConstraint(self, creditConstraint: str):
        self.__creditConstraint = creditConstraint

    @property
    def totalCredits(self) -> float:
        return self.__totalCredits

    @totalCredits.setter
    def totalCredits(self, totalCredits: float):
        self.__totalCredits = totalCredits

    @property
    def StudyProgramme_Semester4(self):
        return self.__StudyProgramme_Semester4

    @StudyProgramme_Semester4.setter
    def StudyProgramme_Semester4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StudyProgramme_Semester__StudyProgramme_Semester4", None)
        self.__StudyProgramme_Semester4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StudyProgramme_Course"):
                    opp_val = getattr(item, "StudyProgramme_Course", None)
                    
                    if opp_val == self:
                        setattr(item, "StudyProgramme_Course", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StudyProgramme_Course"):
                    opp_val = getattr(item, "StudyProgramme_Course", None)
                    
                    setattr(item, "StudyProgramme_Course", self)
                    

    @property
    def StudyProgramme_Semester12(self):
        return self.__StudyProgramme_Semester12

    @StudyProgramme_Semester12.setter
    def StudyProgramme_Semester12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StudyProgramme_Semester__StudyProgramme_Semester12", None)
        self.__StudyProgramme_Semester12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StudyProgramme_Specialization11"):
                opp_val = getattr(old_value, "StudyProgramme_Specialization11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StudyProgramme_Specialization11"):
                opp_val = getattr(value, "StudyProgramme_Specialization11", None)
                if opp_val is None:
                    setattr(value, "StudyProgramme_Specialization11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def StudyProgramme_Semester6(self):
        return self.__StudyProgramme_Semester6

    @StudyProgramme_Semester6.setter
    def StudyProgramme_Semester6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StudyProgramme_Semester__StudyProgramme_Semester6", None)
        self.__StudyProgramme_Semester6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StudyProgramme_CourseGroup"):
                    opp_val = getattr(item, "StudyProgramme_CourseGroup", None)
                    
                    if opp_val == self:
                        setattr(item, "StudyProgramme_CourseGroup", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StudyProgramme_CourseGroup"):
                    opp_val = getattr(item, "StudyProgramme_CourseGroup", None)
                    
                    setattr(item, "StudyProgramme_CourseGroup", self)
                    

    @property
    def StudyProgramme_Semester(self):
        return self.__StudyProgramme_Semester

    @StudyProgramme_Semester.setter
    def StudyProgramme_Semester(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StudyProgramme_Semester__StudyProgramme_Semester", None)
        self.__StudyProgramme_Semester = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StudyProgramme_Programme"):
                opp_val = getattr(old_value, "StudyProgramme_Programme", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StudyProgramme_Programme"):
                opp_val = getattr(value, "StudyProgramme_Programme", None)
                if opp_val is None:
                    setattr(value, "StudyProgramme_Programme", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class StudyProgramme_Programme:

    def __init__(self, name: str, code: str, duration: int, StudyProgramme_Programme: set["StudyProgramme_Semester"] = None, StudyProgramme_Programme2: set["StudyProgramme_Specialization"] = None, StudyProgramme_Programme20: "StudyProgramme_Department" = None):
        self.name = name
        self.code = code
        self.duration = duration
        self.StudyProgramme_Programme = StudyProgramme_Programme if StudyProgramme_Programme is not None else set()
        self.StudyProgramme_Programme2 = StudyProgramme_Programme2 if StudyProgramme_Programme2 is not None else set()
        self.StudyProgramme_Programme20 = StudyProgramme_Programme20
        
    @property
    def duration(self) -> int:
        return self.__duration

    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration

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
    def StudyProgramme_Programme(self):
        return self.__StudyProgramme_Programme

    @StudyProgramme_Programme.setter
    def StudyProgramme_Programme(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StudyProgramme_Programme__StudyProgramme_Programme", None)
        self.__StudyProgramme_Programme = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StudyProgramme_Semester"):
                    opp_val = getattr(item, "StudyProgramme_Semester", None)
                    
                    if opp_val == self:
                        setattr(item, "StudyProgramme_Semester", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StudyProgramme_Semester"):
                    opp_val = getattr(item, "StudyProgramme_Semester", None)
                    
                    setattr(item, "StudyProgramme_Semester", self)
                    

    @property
    def StudyProgramme_Programme2(self):
        return self.__StudyProgramme_Programme2

    @StudyProgramme_Programme2.setter
    def StudyProgramme_Programme2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StudyProgramme_Programme__StudyProgramme_Programme2", None)
        self.__StudyProgramme_Programme2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StudyProgramme_Specialization"):
                    opp_val = getattr(item, "StudyProgramme_Specialization", None)
                    
                    if opp_val == self:
                        setattr(item, "StudyProgramme_Specialization", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StudyProgramme_Specialization"):
                    opp_val = getattr(item, "StudyProgramme_Specialization", None)
                    
                    setattr(item, "StudyProgramme_Specialization", self)
                    

    @property
    def StudyProgramme_Programme20(self):
        return self.__StudyProgramme_Programme20

    @StudyProgramme_Programme20.setter
    def StudyProgramme_Programme20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_StudyProgramme_Programme__StudyProgramme_Programme20", None)
        self.__StudyProgramme_Programme20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "StudyProgramme_Department"):
                opp_val = getattr(old_value, "StudyProgramme_Department", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "StudyProgramme_Department"):
                opp_val = getattr(value, "StudyProgramme_Department", None)
                if opp_val is None:
                    setattr(value, "StudyProgramme_Department", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
