from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class edu_Take_Course:

    pass
class edu_Student:

    def __init__(self, id: int, name: str, date_of_birth: date, edu_Student: "edu_Take_Course" = None):
        self.id = id
        self.name = name
        self.date_of_birth = date_of_birth
        self.edu_Student = edu_Student
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id


    @property
    def date_of_birth(self):
        return self.__date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth: date):
        self.__date_of_birth = date_of_birth


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def edu_Student(self):
        return self.__edu_Student

    @edu_Student.setter
    def edu_Student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Student__edu_Student", None)
        self.__edu_Student = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Take_Course"):
                opp_val = getattr(old_value, "edu_Take_Course", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Take_Course"):
                opp_val = getattr(value, "edu_Take_Course", None)
                if opp_val is None:
                    setattr(value, "edu_Take_Course", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def getAge(self) :
        # TODO: Implement getAge method
        pass

class edu_Course:

    def __init__(self, id: int, name: str, edu_Course: "edu_Take_Course" = None):
        self.id = id
        self.name = name
        self.edu_Course = edu_Course
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def edu_Course(self):
        return self.__edu_Course

    @edu_Course.setter
    def edu_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_edu_Course__edu_Course", None)
        self.__edu_Course = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "edu_Take_Course2"):
                opp_val = getattr(old_value, "edu_Take_Course2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "edu_Take_Course2"):
                opp_val = getattr(value, "edu_Take_Course2", None)
                if opp_val is None:
                    setattr(value, "edu_Take_Course2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
