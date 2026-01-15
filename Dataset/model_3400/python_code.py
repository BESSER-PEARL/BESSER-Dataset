from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Person_Person:

    def __init__(self, firstName: str, lastName: str, Person_Person: "Person_Model" = None, Person_Person3: "Person_Person" = None, Person_Person1: set["Person_Person"] = None):
        self.firstName = firstName
        self.lastName = lastName
        self.Person_Person = Person_Person
        self.Person_Person3 = Person_Person3
        self.Person_Person1 = Person_Person1 if Person_Person1 is not None else set()
        
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
    def Person_Person3(self):
        return self.__Person_Person3

    @Person_Person3.setter
    def Person_Person3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Person_Person__Person_Person3", None)
        self.__Person_Person3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Person_Person1"):
                opp_val = getattr(old_value, "Person_Person1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Person_Person1"):
                opp_val = getattr(value, "Person_Person1", None)
                if opp_val is None:
                    setattr(value, "Person_Person1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Person_Person1(self):
        return self.__Person_Person1

    @Person_Person1.setter
    def Person_Person1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Person_Person__Person_Person1", None)
        self.__Person_Person1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person_Person3"):
                    opp_val = getattr(item, "Person_Person3", None)
                    
                    if opp_val == self:
                        setattr(item, "Person_Person3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person_Person3"):
                    opp_val = getattr(item, "Person_Person3", None)
                    
                    setattr(item, "Person_Person3", self)
                    

    @property
    def Person_Person(self):
        return self.__Person_Person

    @Person_Person.setter
    def Person_Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Person_Person__Person_Person", None)
        self.__Person_Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Person_Model"):
                opp_val = getattr(old_value, "Person_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Person_Model"):
                opp_val = getattr(value, "Person_Model", None)
                if opp_val is None:
                    setattr(value, "Person_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Person_Model:

    pass