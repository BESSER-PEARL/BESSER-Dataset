from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class TUWien_Student:

    def __init__(self, name: str, id: int, student: set["TUWien_Course"] = None, Student: "TUWien_Course" = None, TUWien_Student: "TUWien_University" = None):
        self.name = name
        self.id = id
        self.student = student if student is not None else set()
        self.Student = Student
        self.TUWien_Student = TUWien_Student
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def Student(self):
        return self.__Student

    @Student.setter
    def Student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TUWien_Student__Student", None)
        self.__Student = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course"):
                opp_val = getattr(old_value, "course", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course"):
                opp_val = getattr(value, "course", None)
                if opp_val is None:
                    setattr(value, "course", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def student(self):
        return self.__student

    @student.setter
    def student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TUWien_Student__student", None)
        self.__student = value if value is not None else set()
        
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
    def TUWien_Student(self):
        return self.__TUWien_Student

    @TUWien_Student.setter
    def TUWien_Student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TUWien_Student__TUWien_Student", None)
        self.__TUWien_Student = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TUWien_University2"):
                opp_val = getattr(old_value, "TUWien_University2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TUWien_University2"):
                opp_val = getattr(value, "TUWien_University2", None)
                if opp_val is None:
                    setattr(value, "TUWien_University2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class TUWien_Course:

    def __init__(self, id: str, name: str, Course: "TUWien_Student" = None, course: set["TUWien_Student"] = None, TUWien_Course: "TUWien_University" = None):
        self.id = id
        self.name = name
        self.Course = Course
        self.course = course if course is not None else set()
        self.TUWien_Course = TUWien_Course
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def TUWien_Course(self):
        return self.__TUWien_Course

    @TUWien_Course.setter
    def TUWien_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TUWien_Course__TUWien_Course", None)
        self.__TUWien_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "TUWien_University"):
                opp_val = getattr(old_value, "TUWien_University", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "TUWien_University"):
                opp_val = getattr(value, "TUWien_University", None)
                if opp_val is None:
                    setattr(value, "TUWien_University", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TUWien_Course__course", None)
        self.__course = value if value is not None else set()
        
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
    def Course(self):
        return self.__Course

    @Course.setter
    def Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TUWien_Course__Course", None)
        self.__Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "student"):
                opp_val = getattr(old_value, "student", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "student"):
                opp_val = getattr(value, "student", None)
                if opp_val is None:
                    setattr(value, "student", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class TUWien_University:

    def __init__(self, name: str, TUWien_University: set["TUWien_Course"] = None, TUWien_University2: set["TUWien_Student"] = None):
        self.name = name
        self.TUWien_University = TUWien_University if TUWien_University is not None else set()
        self.TUWien_University2 = TUWien_University2 if TUWien_University2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def TUWien_University2(self):
        return self.__TUWien_University2

    @TUWien_University2.setter
    def TUWien_University2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TUWien_University__TUWien_University2", None)
        self.__TUWien_University2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TUWien_Student"):
                    opp_val = getattr(item, "TUWien_Student", None)
                    
                    if opp_val == self:
                        setattr(item, "TUWien_Student", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TUWien_Student"):
                    opp_val = getattr(item, "TUWien_Student", None)
                    
                    setattr(item, "TUWien_Student", self)
                    

    @property
    def TUWien_University(self):
        return self.__TUWien_University

    @TUWien_University.setter
    def TUWien_University(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TUWien_University__TUWien_University", None)
        self.__TUWien_University = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "TUWien_Course"):
                    opp_val = getattr(item, "TUWien_Course", None)
                    
                    if opp_val == self:
                        setattr(item, "TUWien_Course", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "TUWien_Course"):
                    opp_val = getattr(item, "TUWien_Course", None)
                    
                    setattr(item, "TUWien_Course", self)
                    
