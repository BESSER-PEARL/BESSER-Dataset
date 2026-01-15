from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class education_Course:

    def __init__(self, name: str, education_Course2: "education_Teacher" = None, education_Course: set["education_Student"] = None):
        self.name = name
        self.education_Course2 = education_Course2
        self.education_Course = education_Course if education_Course is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def education_Course2(self):
        return self.__education_Course2

    @education_Course2.setter
    def education_Course2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_education_Course__education_Course2", None)
        self.__education_Course2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "education_Teacher"):
                opp_val = getattr(old_value, "education_Teacher", None)
                if opp_val == self:
                    setattr(old_value, "education_Teacher", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "education_Teacher"):
                opp_val = getattr(value, "education_Teacher", None)
                setattr(value, "education_Teacher", self)

    @property
    def education_Course(self):
        return self.__education_Course

    @education_Course.setter
    def education_Course(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_education_Course__education_Course", None)
        self.__education_Course = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "education_Student"):
                    opp_val = getattr(item, "education_Student", None)
                    
                    if opp_val == self:
                        setattr(item, "education_Student", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "education_Student"):
                    opp_val = getattr(item, "education_Student", None)
                    
                    setattr(item, "education_Student", self)
                    

    def finish(self, finishdate: str):
        # TODO: Implement finish method
        pass

    def start(self, startdate: str):
        # TODO: Implement start method
        pass

class Person:

    pass
class education_Teacher(Person):

    pass
class education_Student(Person):

    pass
class education_Person:

    def __init__(self, firstname: str, lastname: str):
        self.firstname = firstname
        self.lastname = lastname
        
    @property
    def firstname(self) -> str:
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

    @property
    def lastname(self) -> str:
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname
