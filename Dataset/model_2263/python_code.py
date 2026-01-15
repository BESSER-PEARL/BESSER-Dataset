from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class mteach_Topic:

    def __init__(self, title: str, Topic: "mteach_Course" = None, topics: "mteach_Course" = None):
        self.title = title
        self.Topic = Topic
        self.topics = topics
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def Topic(self):
        return self.__Topic

    @Topic.setter
    def Topic(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mteach_Topic__Topic", None)
        self.__Topic = value
        
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
    def topics(self):
        return self.__topics

    @topics.setter
    def topics(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mteach_Topic__topics", None)
        self.__topics = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Course4"):
                opp_val = getattr(old_value, "Course4", None)
                if opp_val == self:
                    setattr(old_value, "Course4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Course4"):
                opp_val = getattr(value, "Course4", None)
                setattr(value, "Course4", self)

class mteach_Course:

    def __init__(self, name: str, time: int, coefficient: float, Course: "mteach_Professor" = None, course: set["mteach_Topic"] = None, teachedCourses: "mteach_Professor" = None, Course4: "mteach_Topic" = None):
        self.name = name
        self.time = time
        self.coefficient = coefficient
        self.Course = Course
        self.course = course if course is not None else set()
        self.teachedCourses = teachedCourses
        self.Course4 = Course4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def time(self) -> int:
        return self.__time

    @time.setter
    def time(self, time: int):
        self.__time = time

    @property
    def coefficient(self) -> float:
        return self.__coefficient

    @coefficient.setter
    def coefficient(self, coefficient: float):
        self.__coefficient = coefficient

    @property
    def Course(self):
        return self.__Course

    @Course.setter
    def Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mteach_Course__Course", None)
        self.__Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "professor"):
                opp_val = getattr(old_value, "professor", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "professor"):
                opp_val = getattr(value, "professor", None)
                if opp_val is None:
                    setattr(value, "professor", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Course4(self):
        return self.__Course4

    @Course4.setter
    def Course4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mteach_Course__Course4", None)
        self.__Course4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "topics"):
                opp_val = getattr(old_value, "topics", None)
                if opp_val == self:
                    setattr(old_value, "topics", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "topics"):
                opp_val = getattr(value, "topics", None)
                setattr(value, "topics", self)

    @property
    def teachedCourses(self):
        return self.__teachedCourses

    @teachedCourses.setter
    def teachedCourses(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mteach_Course__teachedCourses", None)
        self.__teachedCourses = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Professor"):
                opp_val = getattr(old_value, "Professor", None)
                if opp_val == self:
                    setattr(old_value, "Professor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Professor"):
                opp_val = getattr(value, "Professor", None)
                setattr(value, "Professor", self)

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mteach_Course__course", None)
        self.__course = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Topic"):
                    opp_val = getattr(item, "Topic", None)
                    
                    if opp_val == self:
                        setattr(item, "Topic", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Topic"):
                    opp_val = getattr(item, "Topic", None)
                    
                    setattr(item, "Topic", self)
                    

class mteach_Professor:

    def __init__(self, lastName: str, firstName: str, professor: set["mteach_Course"] = None, Professor: "mteach_Course" = None):
        self.lastName = lastName
        self.firstName = firstName
        self.professor = professor if professor is not None else set()
        self.Professor = Professor
        
    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def Professor(self):
        return self.__Professor

    @Professor.setter
    def Professor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mteach_Professor__Professor", None)
        self.__Professor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "teachedCourses"):
                opp_val = getattr(old_value, "teachedCourses", None)
                if opp_val == self:
                    setattr(old_value, "teachedCourses", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "teachedCourses"):
                opp_val = getattr(value, "teachedCourses", None)
                setattr(value, "teachedCourses", self)

    @property
    def professor(self):
        return self.__professor

    @professor.setter
    def professor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mteach_Professor__professor", None)
        self.__professor = value if value is not None else set()
        
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
                    
