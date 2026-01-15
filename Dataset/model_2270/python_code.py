from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class university_Student:

    def __init__(self, id: str, students: set["university_Course"] = None, university_Student: "university_University" = None, Student: "university_Course" = None):
        self.id = id
        self.students = students if students is not None else set()
        self.university_Student = university_Student
        self.Student = Student
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def university_Student(self):
        return self.__university_Student

    @university_Student.setter
    def university_Student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Student__university_Student", None)
        self.__university_Student = value
        
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
    def Student(self):
        return self.__Student

    @Student.setter
    def Student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Student__Student", None)
        self.__Student = value
        
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

    @property
    def students(self):
        return self.__students

    @students.setter
    def students(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_university_Student__students", None)
        self.__students = value if value is not None else set()
        
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
                    

class university_Course:

    def __init__(self, name: str, Course: "university_Student" = None, university_Course: "university_University" = None, courses: set["university_Student"] = None):
        self.name = name
        self.Course = Course
        self.university_Course = university_Course
        self.courses = courses if courses is not None else set()
        
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
                if hasattr(item, "Student"):
                    opp_val = getattr(item, "Student", None)
                    
                    if opp_val == self:
                        setattr(item, "Student", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Student"):
                    opp_val = getattr(item, "Student", None)
                    
                    setattr(item, "Student", self)
                    

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
            if hasattr(old_value, "students"):
                opp_val = getattr(old_value, "students", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "students"):
                opp_val = getattr(value, "students", None)
                if opp_val is None:
                    setattr(value, "students", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class university_University:

    def __init__(self, name: str, university_University: set["university_Student"] = None, university_University4: set["university_Course"] = None):
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
                if hasattr(item, "university_Student"):
                    opp_val = getattr(item, "university_Student", None)
                    
                    if opp_val == self:
                        setattr(item, "university_Student", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "university_Student"):
                    opp_val = getattr(item, "university_Student", None)
                    
                    setattr(item, "university_Student", self)
                    
