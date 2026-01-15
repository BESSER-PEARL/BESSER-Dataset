from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class university_University:

    def __init__(self, name: str, university_University: set["university_Professor"] = None, university_University4: set["university_Course"] = None):
        self.name = name
        self.university_University = university_University if university_University is not None else set()
        self.university_University4 = university_University4 if university_University4 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def university_University(self):
        return self.__university_University

    @university_University.setter
    def university_University(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_University__university_University", None)
        self.__university_University = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "university_Professor"):
                    opp_val = getattr(item, "university_Professor", None)
                    
                    if opp_val == self:
                        setattr(item, "university_Professor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "university_Professor"):
                    opp_val = getattr(item, "university_Professor", None)
                    
                    setattr(item, "university_Professor", self)
                    

    @property
    def university_University4(self):
        return self.__university_University4

    @university_University4.setter
    def university_University4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_University__university_University4", None)
        self.__university_University4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "university_Course"):
                    opp_val = getattr(item, "university_Course", None)
                    
                    if opp_val == self:
                        setattr(item, "university_Course", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "university_Course"):
                    opp_val = getattr(item, "university_Course", None)
                    
                    setattr(item, "university_Course", self)
                    

class university_Professor:

    def __init__(self, name: str, Professor: "university_Course" = None, professors: set["university_Course"] = None, university_Professor: "university_University" = None):
        self.name = name
        self.Professor = Professor
        self.professors = professors if professors is not None else set()
        self.university_Professor = university_Professor
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def university_Professor(self):
        return self.__university_Professor

    @university_Professor.setter
    def university_Professor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Professor__university_Professor", None)
        self.__university_Professor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "university_University"):
                opp_val = getattr(old_value, "university_University", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "university_University"):
                opp_val = getattr(value, "university_University", None)
                if opp_val is None:
                    setattr(value, "university_University", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def professors(self):
        return self.__professors

    @professors.setter
    def professors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Professor__professors", None)
        self.__professors = value if value is not None else set()
        
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
    def Professor(self):
        return self.__Professor

    @Professor.setter
    def Professor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Professor__Professor", None)
        self.__Professor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "courses"):
                opp_val = getattr(old_value, "courses", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "courses"):
                opp_val = getattr(value, "courses", None)
                if opp_val is None:
                    setattr(value, "courses", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class university_Course:

    def __init__(self, name: str, courses: set["university_Professor"] = None, Course: "university_Professor" = None, university_Course: "university_University" = None):
        self.name = name
        self.courses = courses if courses is not None else set()
        self.Course = Course
        self.university_Course = university_Course
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Course__courses", None)
        self.__courses = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Professor"):
                    opp_val = getattr(item, "Professor", None)
                    
                    if opp_val == self:
                        setattr(item, "Professor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Professor"):
                    opp_val = getattr(item, "Professor", None)
                    
                    setattr(item, "Professor", self)
                    

    @property
    def Course(self):
        return self.__Course

    @Course.setter
    def Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Course__Course", None)
        self.__Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "professors"):
                opp_val = getattr(old_value, "professors", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "professors"):
                opp_val = getattr(value, "professors", None)
                if opp_val is None:
                    setattr(value, "professors", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def university_Course(self):
        return self.__university_Course

    @university_Course.setter
    def university_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Course__university_Course", None)
        self.__university_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "university_University4"):
                opp_val = getattr(old_value, "university_University4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "university_University4"):
                opp_val = getattr(value, "university_University4", None)
                if opp_val is None:
                    setattr(value, "university_University4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
