from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class Person:

    pass
class Friends_Woman(Person):

    pass
class Friends_Man(Person):

    pass
class Friends_Classroom:

    def __init__(self, id: int, Friends_Classroom: "Friends_Person" = None, Friends_Classroom5: set["Friends_Person"] = None):
        self.id = id
        self.Friends_Classroom = Friends_Classroom
        self.Friends_Classroom5 = Friends_Classroom5 if Friends_Classroom5 is not None else set()
        
    @property
    def id(self) -> int:
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def Friends_Classroom(self):
        return self.__Friends_Classroom

    @Friends_Classroom.setter
    def Friends_Classroom(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Friends_Classroom__Friends_Classroom", None)
        self.__Friends_Classroom = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Friends_Person3"):
                opp_val = getattr(old_value, "Friends_Person3", None)
                if opp_val == self:
                    setattr(old_value, "Friends_Person3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Friends_Person3"):
                opp_val = getattr(value, "Friends_Person3", None)
                setattr(value, "Friends_Person3", self)

    @property
    def Friends_Classroom5(self):
        return self.__Friends_Classroom5

    @Friends_Classroom5.setter
    def Friends_Classroom5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Friends_Classroom__Friends_Classroom5", None)
        self.__Friends_Classroom5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Friends_Person6"):
                    opp_val = getattr(item, "Friends_Person6", None)
                    
                    if opp_val == self:
                        setattr(item, "Friends_Person6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Friends_Person6"):
                    opp_val = getattr(item, "Friends_Person6", None)
                    
                    setattr(item, "Friends_Person6", self)
                    

class Friends_Person(ABC):

    def __init__(self, name: str, Friends_Person: "Friends_Person" = None, Friends_Person0: set["Friends_Person"] = None, Friends_Person3: "Friends_Classroom" = None, Friends_Person6: "Friends_Classroom" = None):
        self.name = name
        self.Friends_Person = Friends_Person
        self.Friends_Person0 = Friends_Person0 if Friends_Person0 is not None else set()
        self.Friends_Person3 = Friends_Person3
        self.Friends_Person6 = Friends_Person6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Friends_Person(self):
        return self.__Friends_Person

    @Friends_Person.setter
    def Friends_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Friends_Person__Friends_Person", None)
        self.__Friends_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Friends_Person0"):
                opp_val = getattr(old_value, "Friends_Person0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Friends_Person0"):
                opp_val = getattr(value, "Friends_Person0", None)
                if opp_val is None:
                    setattr(value, "Friends_Person0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Friends_Person0(self):
        return self.__Friends_Person0

    @Friends_Person0.setter
    def Friends_Person0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Friends_Person__Friends_Person0", None)
        self.__Friends_Person0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Friends_Person"):
                    opp_val = getattr(item, "Friends_Person", None)
                    
                    if opp_val == self:
                        setattr(item, "Friends_Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Friends_Person"):
                    opp_val = getattr(item, "Friends_Person", None)
                    
                    setattr(item, "Friends_Person", self)
                    

    @property
    def Friends_Person6(self):
        return self.__Friends_Person6

    @Friends_Person6.setter
    def Friends_Person6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Friends_Person__Friends_Person6", None)
        self.__Friends_Person6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Friends_Classroom5"):
                opp_val = getattr(old_value, "Friends_Classroom5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Friends_Classroom5"):
                opp_val = getattr(value, "Friends_Classroom5", None)
                if opp_val is None:
                    setattr(value, "Friends_Classroom5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Friends_Person3(self):
        return self.__Friends_Person3

    @Friends_Person3.setter
    def Friends_Person3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Friends_Person__Friends_Person3", None)
        self.__Friends_Person3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Friends_Classroom"):
                opp_val = getattr(old_value, "Friends_Classroom", None)
                if opp_val == self:
                    setattr(old_value, "Friends_Classroom", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Friends_Classroom"):
                opp_val = getattr(value, "Friends_Classroom", None)
                setattr(value, "Friends_Classroom", self)
