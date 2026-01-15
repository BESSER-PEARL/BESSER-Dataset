from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Gender(Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"


############################################
# Definition of Classes
############################################

class people_Universe:

    pass
class people_Person:

    def __init__(self, gender: str, name: str, people_Person: "people_Person" = None, people_Person0: set["people_Person"] = None, people_Person4: "people_Person" = None, people_Person2: set["people_Person"] = None, people_Person7: "people_Person" = None, people_Person5: "people_Person" = None, people_Person10: "people_Person" = None, people_Person8: "people_Person" = None, people_Person12: "people_Universe" = None):
        self.gender = gender
        self.name = name
        self.people_Person = people_Person
        self.people_Person0 = people_Person0 if people_Person0 is not None else set()
        self.people_Person4 = people_Person4
        self.people_Person2 = people_Person2 if people_Person2 is not None else set()
        self.people_Person7 = people_Person7
        self.people_Person5 = people_Person5
        self.people_Person10 = people_Person10
        self.people_Person8 = people_Person8
        self.people_Person12 = people_Person12
        
    @property
    def gender(self) -> str:
        return self.__gender

    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def people_Person(self):
        return self.__people_Person

    @people_Person.setter
    def people_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_people_Person__people_Person", None)
        self.__people_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "people_Person0"):
                opp_val = getattr(old_value, "people_Person0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "people_Person0"):
                opp_val = getattr(value, "people_Person0", None)
                if opp_val is None:
                    setattr(value, "people_Person0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def people_Person0(self):
        return self.__people_Person0

    @people_Person0.setter
    def people_Person0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_people_Person__people_Person0", None)
        self.__people_Person0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "people_Person"):
                    opp_val = getattr(item, "people_Person", None)
                    
                    if opp_val == self:
                        setattr(item, "people_Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "people_Person"):
                    opp_val = getattr(item, "people_Person", None)
                    
                    setattr(item, "people_Person", self)
                    

    @property
    def people_Person12(self):
        return self.__people_Person12

    @people_Person12.setter
    def people_Person12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_people_Person__people_Person12", None)
        self.__people_Person12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "people_Universe"):
                opp_val = getattr(old_value, "people_Universe", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "people_Universe"):
                opp_val = getattr(value, "people_Universe", None)
                if opp_val is None:
                    setattr(value, "people_Universe", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def people_Person7(self):
        return self.__people_Person7

    @people_Person7.setter
    def people_Person7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_people_Person__people_Person7", None)
        self.__people_Person7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "people_Person5"):
                opp_val = getattr(old_value, "people_Person5", None)
                if opp_val == self:
                    setattr(old_value, "people_Person5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "people_Person5"):
                opp_val = getattr(value, "people_Person5", None)
                setattr(value, "people_Person5", self)

    @property
    def people_Person4(self):
        return self.__people_Person4

    @people_Person4.setter
    def people_Person4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_people_Person__people_Person4", None)
        self.__people_Person4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "people_Person2"):
                opp_val = getattr(old_value, "people_Person2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "people_Person2"):
                opp_val = getattr(value, "people_Person2", None)
                if opp_val is None:
                    setattr(value, "people_Person2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def people_Person5(self):
        return self.__people_Person5

    @people_Person5.setter
    def people_Person5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_people_Person__people_Person5", None)
        self.__people_Person5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "people_Person7"):
                opp_val = getattr(old_value, "people_Person7", None)
                if opp_val == self:
                    setattr(old_value, "people_Person7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "people_Person7"):
                opp_val = getattr(value, "people_Person7", None)
                setattr(value, "people_Person7", self)

    @property
    def people_Person10(self):
        return self.__people_Person10

    @people_Person10.setter
    def people_Person10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_people_Person__people_Person10", None)
        self.__people_Person10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "people_Person8"):
                opp_val = getattr(old_value, "people_Person8", None)
                if opp_val == self:
                    setattr(old_value, "people_Person8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "people_Person8"):
                opp_val = getattr(value, "people_Person8", None)
                setattr(value, "people_Person8", self)

    @property
    def people_Person2(self):
        return self.__people_Person2

    @people_Person2.setter
    def people_Person2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_people_Person__people_Person2", None)
        self.__people_Person2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "people_Person4"):
                    opp_val = getattr(item, "people_Person4", None)
                    
                    if opp_val == self:
                        setattr(item, "people_Person4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "people_Person4"):
                    opp_val = getattr(item, "people_Person4", None)
                    
                    setattr(item, "people_Person4", self)
                    

    @property
    def people_Person8(self):
        return self.__people_Person8

    @people_Person8.setter
    def people_Person8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_people_Person__people_Person8", None)
        self.__people_Person8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "people_Person10"):
                opp_val = getattr(old_value, "people_Person10", None)
                if opp_val == self:
                    setattr(old_value, "people_Person10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "people_Person10"):
                opp_val = getattr(value, "people_Person10", None)
                setattr(value, "people_Person10", self)

    def child(self, childName: str) -> str:
        # TODO: Implement child method
        pass
