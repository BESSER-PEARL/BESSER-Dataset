from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class myDsl_School:

    def __init__(self, name: str, myDsl_School2: set["myDsl_Person"] = None, myDsl_School: "myDsl_SchoolModel" = None):
        self.name = name
        self.myDsl_School2 = myDsl_School2 if myDsl_School2 is not None else set()
        self.myDsl_School = myDsl_School
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_School(self):
        return self.__myDsl_School

    @myDsl_School.setter
    def myDsl_School(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_School__myDsl_School", None)
        self.__myDsl_School = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_SchoolModel"):
                opp_val = getattr(old_value, "myDsl_SchoolModel", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_SchoolModel"):
                opp_val = getattr(value, "myDsl_SchoolModel", None)
                if opp_val is None:
                    setattr(value, "myDsl_SchoolModel", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def myDsl_School2(self):
        return self.__myDsl_School2

    @myDsl_School2.setter
    def myDsl_School2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_School__myDsl_School2", None)
        self.__myDsl_School2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_Person"):
                    opp_val = getattr(item, "myDsl_Person", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_Person"):
                    opp_val = getattr(item, "myDsl_Person", None)
                    
                    setattr(item, "myDsl_Person", self)
                    

class myDsl_SchoolModel:

    pass
class Person:

    pass
class myDsl_Teacher(Person):

    pass
class myDsl_Student(Person):

    def __init__(self, registrationNum: int, myDsl_Student: set["myDsl_Teacher"] = None):
        self.registrationNum = registrationNum
        self.myDsl_Student = myDsl_Student if myDsl_Student is not None else set()
        
    @property
    def registrationNum(self) -> int:
        return self.__registrationNum

    @registrationNum.setter
    def registrationNum(self, registrationNum: int):
        self.__registrationNum = registrationNum

    @property
    def myDsl_Student(self):
        return self.__myDsl_Student

    @myDsl_Student.setter
    def myDsl_Student(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Student__myDsl_Student", None)
        self.__myDsl_Student = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "myDsl_Teacher"):
                    opp_val = getattr(item, "myDsl_Teacher", None)
                    
                    if opp_val == self:
                        setattr(item, "myDsl_Teacher", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "myDsl_Teacher"):
                    opp_val = getattr(item, "myDsl_Teacher", None)
                    
                    setattr(item, "myDsl_Teacher", self)
                    

class myDsl_Person:

    def __init__(self, name: str, myDsl_Person: "myDsl_School" = None):
        self.name = name
        self.myDsl_Person = myDsl_Person
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def myDsl_Person(self):
        return self.__myDsl_Person

    @myDsl_Person.setter
    def myDsl_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_myDsl_Person__myDsl_Person", None)
        self.__myDsl_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "myDsl_School2"):
                opp_val = getattr(old_value, "myDsl_School2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "myDsl_School2"):
                opp_val = getattr(value, "myDsl_School2", None)
                if opp_val is None:
                    setattr(value, "myDsl_School2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
